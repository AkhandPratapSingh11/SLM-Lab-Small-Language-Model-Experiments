#!/usr/bin/env python3
"""
YouTube Playlist Transcript Downloader
=======================================
Extracts transcripts from all videos in a YouTube playlist and saves them
in multiple formats (Clean Text, Timestamped Text, and Structured JSON).
Ideal for building datasets for LLM / SLM fine-tuning, RAG, and summarization.

Author: Antigravity
Directory: SLM_Experiment/Transcript
"""

import argparse
import json
import os
import re
import sys
import time
from typing import Any, Dict, List, Optional
import urllib.parse
import urllib.request


# =====================================================================
# Dependency Availability Check
# =====================================================================

try:
    from youtube_transcript_api import (
        YouTubeTranscriptApi,
        TranscriptsDisabled,
        NoTranscriptFound,
        CouldNotRetrieveTranscript,
        VideoUnavailable,
    )
    HAS_YOUTUBE_TRANSCRIPT_API = True
except ImportError:
    HAS_YOUTUBE_TRANSCRIPT_API = False

try:
    import yt_dlp
    HAS_YT_DLP = True
except ImportError:
    HAS_YT_DLP = False


# =====================================================================
# Helper Utilities
# =====================================================================

def sanitize_filename(name: str, max_length: int = 100) -> str:
    """Sanitize video/playlist titles for safe filesystem usage."""
    # Remove invalid characters
    sanitized = re.sub(r'[\\/*?:"<>|]', "", name)
    # Replace multiple whitespaces/tabs with single space
    sanitized = re.sub(r"\s+", " ", sanitized).strip()
    # Truncate if too long
    if len(sanitized) > max_length:
        sanitized = sanitized[:max_length].rstrip()
    return sanitized or "untitled"


def format_timestamp(seconds: float) -> str:
    """Convert float seconds to HH:MM:SS or MM:SS format."""
    total_seconds = int(seconds)
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    secs = total_seconds % 60
    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def extract_playlist_id(url_or_id: str) -> str:
    """Extract playlist ID from varied YouTube URL formats or return raw ID."""
    url_or_id = url_or_id.strip()
    # Check if already a pure ID
    if re.fullmatch(r"^[a-zA-Z0-9_-]+$", url_or_id) and not url_or_id.startswith("http"):
        return url_or_id
    
    parsed = urllib.parse.urlparse(url_or_id)
    query_params = urllib.parse.parse_qs(parsed.query)
    if "list" in query_params:
        return query_params["list"][0]
    
    # Regex fallback
    match = re.search(r"[?&]list=([a-zA-Z0-9_-]+)", url_or_id)
    if match:
        return match.group(1)
    
    return url_or_id


# =====================================================================
# Playlist Video Extraction
# =====================================================================

def get_playlist_videos_with_ytdlp(playlist_url: str) -> Dict[str, Any]:
    """Extract playlist video details using yt-dlp."""
    ydl_opts = {
        "extract_flat": True,
        "skip_download": True,
        "quiet": True,
        "no_warnings": True,
        "ignoreerrors": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(playlist_url, download=False)
        if not info:
            raise ValueError(f"Could not retrieve playlist info from {playlist_url}")
        
        playlist_title = info.get("title") or "YouTube_Playlist"
        raw_entries = info.get("entries") or []
        
        videos = []
        for idx, entry in enumerate(raw_entries, 1):
            if not entry:
                continue
            video_id = entry.get("id")
            if not video_id:
                continue
            videos.append({
                "index": idx,
                "video_id": video_id,
                "title": entry.get("title") or f"Video_{idx}",
                "url": f"https://www.youtube.com/watch?v={video_id}",
                "duration": entry.get("duration"),
                "uploader": entry.get("uploader"),
            })
            
        return {
            "playlist_id": info.get("id"),
            "playlist_title": playlist_title,
            "videos": videos,
        }


def get_playlist_videos_fallback(playlist_id: str) -> Dict[str, Any]:
    """Fallback playlist extractor using YouTube HTML scraping without third-party dependencies."""
    playlist_url = f"https://www.youtube.com/playlist?list={playlist_id}"
    req = urllib.request.Request(
        playlist_url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        raise RuntimeError(f"Failed to fetch playlist page: {e}")

    # Extract ytInitialData
    pattern = r"var\s+ytInitialData\s*=\s*({.*?});</script>"
    match = re.search(pattern, html, re.DOTALL)
    if not match:
        # Alternative pattern
        pattern2 = r"ytInitialData\s*=\s*({.+?});"
        match = re.search(pattern2, html)
        if not match:
            raise RuntimeError("Could not find ytInitialData in playlist HTML.")

    try:
        data = json.loads(match.group(1))
    except Exception as e:
        raise RuntimeError(f"Error parsing ytInitialData JSON: {e}")

    # Playlist Title
    playlist_title = "YouTube_Playlist"
    try:
        playlist_title = (
            data.get("metadata", {})
            .get("playlistMetadataRenderer", {})
            .get("title", "YouTube_Playlist")
        )
    except Exception:
        pass

    # Extract video items
    videos = []
    video_ids_seen = set()

    def search_videos(obj: Any):
        if isinstance(obj, dict):
            if "playlistVideoRenderer" in obj:
                pvr = obj["playlistVideoRenderer"]
                vid = pvr.get("videoId")
                if vid and vid not in video_ids_seen:
                    video_ids_seen.add(vid)
                    title = "Unknown"
                    title_obj = pvr.get("title", {})
                    if "runs" in title_obj and title_obj["runs"]:
                        title = title_obj["runs"][0].get("text", "Unknown")
                    elif "simpleText" in title_obj:
                        title = title_obj.get("simpleText", "Unknown")
                    
                    videos.append({
                        "index": len(videos) + 1,
                        "video_id": vid,
                        "title": title,
                        "url": f"https://www.youtube.com/watch?v={vid}",
                        "duration": None,
                        "uploader": None,
                    })
            for v in obj.values():
                search_videos(v)
        elif isinstance(obj, list):
            for item in obj:
                search_videos(item)

    search_videos(data)
    return {
        "playlist_id": playlist_id,
        "playlist_title": playlist_title,
        "videos": videos,
    }


def get_playlist_info(playlist_url_or_id: str) -> Dict[str, Any]:
    """Retrieve playlist details and videos, choosing the best available engine."""
    playlist_id = extract_playlist_id(playlist_url_or_id)
    canonical_url = f"https://www.youtube.com/playlist?list={playlist_id}"

    if HAS_YT_DLP:
        try:
            return get_playlist_videos_with_ytdlp(canonical_url)
        except Exception as e:
            print(f"[Warning] yt-dlp playlist extraction encountered an issue ({e}). Trying fallback scraper...")

    return get_playlist_videos_fallback(playlist_id)


# =====================================================================
# Transcript Extraction
# =====================================================================

def fetch_transcript_for_video(
    video_id: str,
    languages: List[str] = ["en", "en-US", "en-GB", "hi"],
) -> Dict[str, Any]:
    """
    Fetch transcript using youtube-transcript-api.
    Prefers manually uploaded transcripts, then falls back to auto-generated transcripts,
    and then attempts translation if needed.
    """
    if not HAS_YOUTUBE_TRANSCRIPT_API:
        raise ImportError(
            "The 'youtube-transcript-api' package is required to fetch transcripts.\n"
            "Install it using: pip install youtube-transcript-api"
        )

    try:
        if hasattr(YouTubeTranscriptApi, "list_transcripts"):
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        else:
            api = YouTubeTranscriptApi()
            transcript_list = api.list(video_id)

        transcript = None
        source_type = "unknown"
        language_code = "en"

        # 1. Try finding manually created transcript in requested languages
        try:
            transcript = transcript_list.find_manually_created_transcript(languages)
            source_type = "manual"
            language_code = transcript.language_code
        except Exception:
            pass

        # 2. Try finding generated transcript in requested languages
        if not transcript:
            try:
                transcript = transcript_list.find_generated_transcript(languages)
                source_type = "generated"
                language_code = transcript.language_code
            except Exception:
                pass

        # 3. Fallback: Take whatever first transcript exists
        if not transcript:
            try:
                transcript = next(iter(transcript_list))
                source_type = "fallback"
                language_code = transcript.language_code
                
                # If it's not English and can be translated to English, you can optionally translate
                if language_code not in languages and getattr(transcript, "is_translatable", False):
                    try:
                        transcript = transcript.translate("en")
                        language_code = "en (translated)"
                        source_type = "translated"
                    except Exception:
                        pass
            except Exception as e:
                return {"success": False, "error": f"No transcript available: {e}"}

        fetched = transcript.fetch()
        if hasattr(fetched, "to_raw_data"):
            raw_data = fetched.to_raw_data()
        elif isinstance(fetched, list):
            raw_data = [
                {
                    "text": getattr(item, "text", item.get("text", "") if isinstance(item, dict) else str(item)),
                    "start": getattr(item, "start", item.get("start", 0.0) if isinstance(item, dict) else 0.0),
                    "duration": getattr(item, "duration", item.get("duration", 0.0) if isinstance(item, dict) else 0.0),
                }
                for item in fetched
            ]
        else:
            raw_data = list(fetched)
        
        # Build clean representations
        clean_text_segments = []
        timestamped_segments = []
        
        for item in raw_data:
            if isinstance(item, dict):
                text = item.get("text", "")
                start_sec = item.get("start", 0.0)
            else:
                text = getattr(item, "text", "")
                start_sec = getattr(item, "start", 0.0)

            text = text.replace("\n", " ").strip()
            if not text:
                continue
            time_str = format_timestamp(start_sec)
            
            clean_text_segments.append(text)
            timestamped_segments.append(f"[{time_str}] {text}")

        plain_text = " ".join(clean_text_segments)
        timestamped_text = "\n".join(timestamped_segments)

        return {
            "success": True,
            "language": language_code,
            "source_type": source_type,
            "segments_count": len(raw_data),
            "raw_segments": raw_data,
            "plain_text": plain_text,
            "timestamped_text": timestamped_text,
        }

    except TranscriptsDisabled:
        return {"success": False, "error": "Transcripts are disabled for this video."}
    except NoTranscriptFound:
        return {"success": False, "error": "No matching transcript found."}
    except VideoUnavailable:
        return {"success": False, "error": "Video is unavailable or private."}
    except Exception as e:
        return {"success": False, "error": str(e)}


# =====================================================================
# Main Downloader Class
# =====================================================================

class YouTubePlaylistTranscriptFetcher:
    """Manages the end-to-end extraction and export of playlist transcripts."""

    def __init__(
        self,
        output_dir: str = "transcripts",
        languages: Optional[List[str]] = None,
        save_formats: Optional[List[str]] = None,
        combine_dataset: bool = True,
        delay_seconds: float = 0.5,
    ):
        self.base_output_dir = output_dir
        self.languages = languages or ["en", "en-US", "en-GB", "hi"]
        self.save_formats = save_formats or ["txt"]
        self.combine_dataset = combine_dataset
        self.delay_seconds = delay_seconds

    def run(self, playlist_url_or_id: str) -> Dict[str, Any]:
        """Execute extraction on the provided playlist."""
        print("\n" + "=" * 65)
        print("  YouTube Playlist Transcript Downloader")
        print("=" * 65)

        # 1. Inspect dependencies
        if not HAS_YOUTUBE_TRANSCRIPT_API:
            print("\n[ERROR] Missing required library: 'youtube-transcript-api'.")
            print("Please install it with:")
            print("    pip install youtube-transcript-api yt-dlp\n")
            sys.exit(1)

        print(f"\n[1/3] Fetching playlist metadata...")
        playlist_data = get_playlist_info(playlist_url_or_id)
        
        playlist_title = playlist_data.get("playlist_title", "YouTube_Playlist")
        playlist_id = playlist_data.get("playlist_id", "unknown_playlist")
        videos = playlist_data.get("videos", [])
        total_videos = len(videos)

        print(f"      Playlist Name : {playlist_title}")
        print(f"      Playlist ID   : {playlist_id}")
        print(f"      Total Videos  : {total_videos}")

        if total_videos == 0:
            print("\n[Warning] No videos found in the specified playlist.")
            return playlist_data

        # 2. Setup directory
        safe_title = sanitize_filename(playlist_title)
        playlist_dir = os.path.join(self.base_output_dir, f"{safe_title}_{playlist_id}")
        os.makedirs(playlist_dir, exist_ok=True)
        print(f"      Output Folder : {os.path.abspath(playlist_dir)}")

        # 3. Process each video
        print(f"\n[2/3] Extracting transcripts (Language preference: {', '.join(self.languages)})...")
        results = []
        combined_texts = []
        combined_json_records = []

        success_count = 0
        failure_count = 0

        for idx, vid in enumerate(videos, 1):
            vid_id = vid["video_id"]
            vid_title = vid["title"]
            safe_vid_title = sanitize_filename(f"{idx:02d}_{vid_title}")

            print(f"\n -> [{idx}/{total_videos}] {vid_title} ({vid_id})")
            
            transcript_result = fetch_transcript_for_video(vid_id, languages=self.languages)
            
            if transcript_result.get("success"):
                success_count += 1
                lang = transcript_result.get("language")
                stype = transcript_result.get("source_type")
                seg_count = transcript_result.get("segments_count")
                print(f"    ✓ Found ({stype}, lang={lang}, segments={seg_count})")

                # Save formats
                file_stem = os.path.join(playlist_dir, safe_vid_title)

                if "txt" in self.save_formats:
                    txt_path = f"{file_stem}.txt"
                    with open(txt_path, "w", encoding="utf-8") as f:
                        f.write(transcript_result["plain_text"])

                if "timestamped" in self.save_formats:
                    ts_path = f"{file_stem}_timestamped.txt"
                    with open(ts_path, "w", encoding="utf-8") as f:
                        f.write(transcript_result["timestamped_text"])

                if "json" in self.save_formats:
                    json_path = f"{file_stem}.json"
                    record = {
                        "video_id": vid_id,
                        "title": vid_title,
                        "url": vid["url"],
                        "language": lang,
                        "source_type": stype,
                        "segments": transcript_result["raw_segments"],
                        "full_text": transcript_result["plain_text"],
                    }
                    with open(json_path, "w", encoding="utf-8") as f:
                        json.dump(record, f, indent=2, ensure_ascii=False)

                # Keep in memory for combined outputs
                combined_texts.append(
                    f"======================================================================\n"
                    f"VIDEO {idx}: {vid_title}\n"
                    f"URL: {vid['url']}\n"
                    f"======================================================================\n\n"
                    f"{transcript_result['plain_text']}\n\n"
                )

                combined_json_records.append({
                    "index": idx,
                    "video_id": vid_id,
                    "title": vid_title,
                    "url": vid["url"],
                    "language": lang,
                    "full_text": transcript_result["plain_text"],
                })

                results.append({
                    "video_id": vid_id,
                    "title": vid_title,
                    "status": "success",
                    "language": lang,
                    "source_type": stype,
                })
            else:
                failure_count += 1
                err = transcript_result.get("error", "Unknown error")
                print(f"    ✗ Skipped: {err}")
                results.append({
                    "video_id": vid_id,
                    "title": vid_title,
                    "status": "failed",
                    "error": err,
                })

            if self.delay_seconds > 0 and idx < total_videos:
                time.sleep(self.delay_seconds)

        # 4. Save combined files (ideal for datasets & LLM training)
        print(f"\n[3/3] Finalizing output files...")
        if self.combine_dataset and combined_texts:
            comb_txt_path = os.path.join(playlist_dir, "all_transcripts_combined.txt")
            with open(comb_txt_path, "w", encoding="utf-8") as f:
                f.writelines(combined_texts)
            print(f"      Combined Text File : {os.path.basename(comb_txt_path)}")

            comb_jsonl_path = os.path.join(playlist_dir, "all_transcripts.jsonl")
            with open(comb_jsonl_path, "w", encoding="utf-8") as f:
                for rec in combined_json_records:
                    f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            print(f"      Combined JSONL     : {os.path.basename(comb_jsonl_path)}")

        # Save summary report
        summary_path = os.path.join(playlist_dir, "download_summary.json")
        with open(summary_path, "w", encoding="utf-8") as f:
            json.dump({
                "playlist_id": playlist_id,
                "playlist_title": playlist_title,
                "total_videos": total_videos,
                "successful": success_count,
                "failed": failure_count,
                "videos": results,
            }, f, indent=2, ensure_ascii=False)

        print("\n" + "=" * 65)
        print("  Summary Report")
        print("=" * 65)
        print(f"  Total Videos Checked : {total_videos}")
        print(f"  Successfully Fetched : {success_count}")
        print(f"  Unavailable / Failed : {failure_count}")
        print(f"  Saved in             : {os.path.abspath(playlist_dir)}")
        print("=" * 65 + "\n")

        return {
            "playlist_dir": playlist_dir,
            "total": total_videos,
            "success": success_count,
            "failed": failure_count,
        }


# =====================================================================
# Command-Line Interface
# =====================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Download transcripts of all videos in a YouTube playlist."
    )
    parser.add_argument(
        "playlist_url",
        nargs="?",
        default=None,
        help="YouTube playlist URL (e.g. https://www.youtube.com/playlist?list=PL...) or playlist ID",
    )
    parser.add_argument(
        "-u", "--url",
        dest="url_opt",
        help="Alternative flag to provide YouTube playlist URL/ID",
    )
    parser.add_argument(
        "-o", "--output-dir",
        default="transcripts",
        help="Directory to save downloaded transcripts (default: ./transcripts)",
    )
    parser.add_argument(
        "-l", "--languages",
        default="en,hi",
        help="Comma-separated preferred language codes (default: 'en,hi')",
    )
    parser.add_argument(
        "-f", "--format",
        choices=["txt", "timestamped", "json", "all"],
        default="txt",
        help="Output format to save per video: 'txt' (default: single clean text file), 'timestamped', 'json', or 'all'",
    )
    parser.add_argument(
        "--no-combine",
        action="store_true",
        help="Disable creation of aggregated all_transcripts_combined.txt and .jsonl",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Polite delay in seconds between video requests (default: 0.5s)",
    )

    args = parser.parse_args()

    # Determine playlist URL
    target_url = args.playlist_url or args.url_opt
    if not target_url:
        print("\nNo playlist URL was provided as an argument.")
        try:
            target_url = input("Enter YouTube Playlist URL or ID: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nAborted.")
            sys.exit(0)

    if not target_url:
        print("Error: A valid YouTube Playlist URL or ID is required.")
        sys.exit(1)

    lang_list = [l.strip() for l in args.languages.split(",") if l.strip()]
    save_formats = ["txt", "timestamped", "json"] if args.format == "all" else [args.format]

    fetcher = YouTubePlaylistTranscriptFetcher(
        output_dir=args.output_dir,
        languages=lang_list,
        save_formats=save_formats,
        combine_dataset=not args.no_combine,
        delay_seconds=args.delay,
    )
    fetcher.run(target_url)


if __name__ == "__main__":
    main()

