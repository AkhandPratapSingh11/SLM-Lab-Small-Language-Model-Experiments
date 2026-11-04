# YouTube Playlist Transcript Extractor

This tool extracts transcripts from all videos in a YouTube playlist and saves them in multiple structured formats. It is specifically designed to create high-quality training and evaluation datasets for Small Language Models (SLMs), Large Language Models (LLMs), RAG pipelines, and summarization tasks.

---

## 🚀 Features

- **Automated Video Extraction**: Extracts all video IDs, titles, and metadata from any playlist URL or ID (supports `yt-dlp` and built-in fallback parser).
- **Multiple Output Formats**:
  - **Clean Plain Text (`.txt`)**: Continuous, unpunctuated or formatted text (perfect for LLM prompts, embeddings, RAG, and fine-tuning datasets).
  - **Timestamped Text (`_timestamped.txt`)**: Readable format with timestamps `[HH:MM:SS]`.
  - **Structured JSON (`.json`)**: Full segment-level metadata including `start`, `duration`, and segment text.
- **Aggregated Dataset Generation**:
  - `all_transcripts_combined.txt`: Single file combining all playlist videos with separators.
  - `all_transcripts.jsonl`: Line-delimited JSON format ready for model fine-tuning pipelines.
- **Language & Translation Support**: Prefers manual subtitles, falls back to auto-generated captions, and supports fallback translation.
- **Summary Report**: Exports `download_summary.json` with success/failure statistics for each video.

---

## 📦 Installation

Ensure you have the required dependencies installed:

```bash
pip install -r requirements.txt
```

*(Or individually:)*
```bash
pip install youtube-transcript-api yt-dlp requests
```

---

## 💻 Usage

### 1. Simple Command Line Execution

Pass the playlist URL or ID directly:

```bash
python3 youtube_playlist_transcript.py "https://www.youtube.com/playlist?list=PLrAXtmErZgOdP_8GzqqA4uxxGzBi3qc46"
```

Or pass just the playlist ID:

```bash
python3 youtube_playlist_transcript.py PLrAXtmErZgOdP_8GzqqA4uxxGzBi3qc46
```

### 2. Interactive Mode

If executed with no arguments, it will prompt you for the playlist URL:

```bash
python3 youtube_playlist_transcript.py
```

### 3. Custom Output Directory & Options

```bash
python3 youtube_playlist_transcript.py \
    --url "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID" \
    --output-dir "./my_transcripts" \
    --languages "en,hi" \
    --format all \
    --delay 0.5
```

### 4. CLI Arguments Reference

| Option | Flag | Description | Default |
| :--- | :--- | :--- | :--- |
| `playlist_url` | Positional | YouTube playlist URL or ID | Prompt if omitted |
| `--url` | `-u` | YouTube playlist URL or ID | None |
| `--output-dir` | `-o` | Base directory to save output files | `./transcripts` |
| `--languages` | `-l` | Comma-separated preferred language codes | `en,hi` |
| `--format` | `-f` | Output format per video: `txt` (single file), `timestamped`, `json`, or `all` | `txt` |
| `--no-combine` | | Disable `all_transcripts_combined.txt` and `.jsonl` | False |
| `--delay` | | Polite delay in seconds between video requests | `0.5` |

---

## 🐍 Python Import Example

You can also import and use it in your own Python notebooks or scripts:

```python
from youtube_playlist_transcript import YouTubePlaylistTranscriptFetcher

fetcher = YouTubePlaylistTranscriptFetcher(
    output_dir="./transcripts",
    languages=["en", "hi"],
    save_formats=["txt", "json"],
    combine_dataset=True
)

summary = fetcher.run("https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID")
print(summary)
```

