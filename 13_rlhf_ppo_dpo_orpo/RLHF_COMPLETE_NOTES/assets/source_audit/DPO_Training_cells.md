# DPO_Training.ipynb
Metadata: {"accelerator": "GPU", "colab": {"gpuType": "T4", "provenance": []}, "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python", "version": "3.x"}, "widgets": {"application/vnd.jupyter.widget-state+json": {"version_major": 2, "version_minor": 0, "state": {"e193e8ef65ca47bb9c0262250d4a9b50": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_c4b3dcce05ff4aa39372361cb053695a", "IPY_MODEL_f4484c91a25443b996154a859bb40d4f", "IPY_MODEL_df05256b6d9c4da1b337e8842ba47cb7"], "layout": "IPY_MODEL_b4a8a9277858494fa8e388024f142124"}}, "c4b3dcce05ff4aa39372361cb053695a": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_30c24962dabb4eb498be962b153f9aac", "placeholder": "\u200b", "style": "IPY_MODEL_8324c0c1b4f344aba2dcbe51e1adc270", "value": "Map:\u2007100%"}}, "f4484c91a25443b996154a859bb40d4f": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_9ff3af14b4434f288891f131e40c5c73", "max": 4, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_cf4a00e3866c4f76b50b42361ee17768", "value": 4}}, "df05256b6d9c4da1b337e8842ba47cb7": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_e220794ee7ce44aa89b6555d51f5fff3", "placeholder": "\u200b", "style": "IPY_MODEL_7cdfd67582704c64870453803eda8fe3", "value": "\u20074/4\u2007[00:00&lt;00:00,\u2007229.65\u2007examples/s]"}}, "b4a8a9277858494fa8e388024f142124": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "30c24962dabb4eb498be962b153f9aac": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "8324c0c1b4f344aba2dcbe51e1adc270": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "9ff3af14b4434f288891f131e40c5c73": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "cf4a00e3866c4f76b50b42361ee17768": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "e220794ee7ce44aa89b6555d51f5fff3": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "7cdfd67582704c64870453803eda8fe3": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "fc3fed37d7da4a568c7fde7b0f4ebf71": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_9fb9930dce414877b8a630739a9de220", "IPY_MODEL_470da8d12de14376897969bf6111d68b", "IPY_MODEL_a295869057c7405996a006a259f9c1c0"], "layout": "IPY_MODEL_4b0c6bbc67d14bec899d374655ccb994"}}, "9fb9930dce414877b8a630739a9de220": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_8aeb15f2f35b424f8d512d00b5ea3b0b", "placeholder": "\u200b", "style": "IPY_MODEL_8b985837fe3844b2ae0243cfb3385154", "value": "config.json:\u2007100%"}}, "470da8d12de14376897969bf6111d68b": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_b1952c319fd34e179555a897afbe0f8a", "max": 659, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_0419bc85b03246c2a25d9b8d31a78c72", "value": 659}}, "a295869057c7405996a006a259f9c1c0": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_24025a7fd25440628044aaa69a502969", "placeholder": "\u200b", "style": "IPY_MODEL_0273e54f77424d258583b5d421aeb6b5", "value": "\u2007659/659\u2007[00:00&lt;00:00,\u200736.0kB/s]"}}, "4b0c6bbc67d14bec899d374655ccb994": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "8aeb15f2f35b424f8d512d00b5ea3b0b": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "8b985837fe3844b2ae0243cfb3385154": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "b1952c319fd34e179555a897afbe0f8a": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "0419bc85b03246c2a25d9b8d31a78c72": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "24025a7fd25440628044aaa69a502969": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "0273e54f77424d258583b5d421aeb6b5": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "a7a4514f2c02435599518c5a98c70732": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_36a7893e37334e6383dcedc3e0a51be3", "IPY_MODEL_ea99e9d456544e8381d739355f0ceb81", "IPY_MODEL_83468bcbea5848528cc12bb8f22c63c6"], "layout": "IPY_MODEL_46377ebf514a470ba293f3376a87f691"}}, "36a7893e37334e6383dcedc3e0a51be3": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_cdfcbe5084a44dd6bf46378c3eb06e47", "placeholder": "\u200b", "style": "IPY_MODEL_d077189671e942e881d36efa30a885e8", "value": "tokenizer_config.json:\u2007100%"}}, "ea99e9d456544e8381d739355f0ceb81": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_01f898acafd542f28aa70ed81d5eefb1", "max": 7305, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_3926a6830d1d4f7fb51a3dc358de4005", "value": 7305}}, "83468bcbea5848528cc12bb8f22c63c6": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_0db5d9eb05924d6ba430d9e36ee85e8a", "placeholder": "\u200b", "style": "IPY_MODEL_b44c89874186492aa48fb769b7f78045", "value": "\u20077.30k/7.30k\u2007[00:00&lt;00:00,\u2007633kB/s]"}}, "46377ebf514a470ba293f3376a87f691": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "cdfcbe5084a44dd6bf46378c3eb06e47": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "d077189671e942e881d36efa30a885e8": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "01f898acafd542f28aa70ed81d5eefb1": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "3926a6830d1d4f7fb51a3dc358de4005": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "0db5d9eb05924d6ba430d9e36ee85e8a": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "b44c89874186492aa48fb769b7f78045": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "330853c7437e439cbcebf41f3c51f364": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_09d891839d564ed1b1dda75b91a91cda", "IPY_MODEL_96c0012eb0114c7ab9796c3b05f853d1", "IPY_MODEL_088f3c5647e14bc38b862f6fcb479fce"], "layout": "IPY_MODEL_828be22d8e38495d90c330fb66107acd"}}, "09d891839d564ed1b1dda75b91a91cda": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_2ff3535c27744b8a8203753868ef8330", "placeholder": "\u200b", "style": "IPY_MODEL_a133420d1cf74efba1cbf4578881e2d7", "value": "vocab.json:\u2007100%"}}, "96c0012eb0114c7ab9796c3b05f853d1": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_6fa7a0e97fbb48d092671075c416702d", "max": 2776833, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_a2ce736237ae44fea41194c302753a96", "value": 2776833}}, "088f3c5647e14bc38b862f6fcb479fce": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_e1aceac2219f48b981b8f78203be22b4", "placeholder": "\u200b", "style": "IPY_MODEL_957816c3a5f24ce6a82cd6713c7e66be", "value": "\u20072.78M/2.78M\u2007[00:00&lt;00:00,\u200711.4MB/s]"}}, "828be22d8e38495d90c330fb66107acd": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "2ff3535c27744b8a8203753868ef8330": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "a133420d1cf74efba1cbf4578881e2d7": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "6fa7a0e97fbb48d092671075c416702d": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "a2ce736237ae44fea41194c302753a96": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "e1aceac2219f48b981b8f78203be22b4": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "957816c3a5f24ce6a82cd6713c7e66be": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "ad6ddb5e49bd43e689b350fa5973a832": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_7fe3d7459ae347a2b23000b69b5c4767", "IPY_MODEL_a5a3fc581d0e417a8e7db2566d21c806", "IPY_MODEL_6e1ae5c079ce456ea63a874f31c85640"], "layout": "IPY_MODEL_91eb943fbad646028631db391f4ca2fb"}}, "7fe3d7459ae347a2b23000b69b5c4767": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_6ed5f18f1e0d48c6abecc32ae7376d36", "placeholder": "\u200b", "style": "IPY_MODEL_460b5648f73e4fb6829406b677e78c1d", "value": "merges.txt:\u2007100%"}}, "a5a3fc581d0e417a8e7db2566d21c806": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_4074ade85e52448d96da492f5e973e8a", "max": 1671839, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_ffc04c45c06745968b17cef413fbd5e3", "value": 1671839}}, "6e1ae5c079ce456ea63a874f31c85640": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_4718895e98004eaca0d0af6dce75952d", "placeholder": "\u200b", "style": "IPY_MODEL_de4587b7b6a04ec8847152b7bd8907c6", "value": "\u20071.67M/1.67M\u2007[00:00&lt;00:00,\u200714.3MB/s]"}}, "91eb943fbad646028631db391f4ca2fb": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "6ed5f18f1e0d48c6abecc32ae7376d36": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "460b5648f73e4fb6829406b677e78c1d": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "4074ade85e52448d96da492f5e973e8a": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "ffc04c45c06745968b17cef413fbd5e3": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "4718895e98004eaca0d0af6dce75952d": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "de4587b7b6a04ec8847152b7bd8907c6": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "f3264597e2b545c6a91150b17ae06275": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_c1b929d4fd4b4c88928c340bb8d725b3", "IPY_MODEL_e1f37b5ad2c5403bb72655b5828145c8", "IPY_MODEL_77bfd8b4db7f4d7691abc68e8aa5e620"], "layout": "IPY_MODEL_8fd5e126760a4afab0de13ce091f2905"}}, "c1b929d4fd4b4c88928c340bb8d725b3": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_9f2fc303bd96427e9c0d62d64ffbbb01", "placeholder": "\u200b", "style": "IPY_MODEL_730abcedbbf7471b839b1a1a062bb4f4", "value": "tokenizer.json:\u2007100%"}}, "e1f37b5ad2c5403bb72655b5828145c8": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_3c749dd3465646faa01e15603186bb7f", "max": 7031645, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_6ed328d77788473bb0df0be610fd7ef4", "value": 7031645}}, "77bfd8b4db7f4d7691abc68e8aa5e620": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_77cd372bec384332be2f3e23e49f9c62", "placeholder": "\u200b", "style": "IPY_MODEL_f0538af32d8f4e55b281932669ddcda2", "value": "\u20077.03M/7.03M\u2007[00:00&lt;00:00,\u200723.1MB/s]"}}, "8fd5e126760a4afab0de13ce091f2905": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "9f2fc303bd96427e9c0d62d64ffbbb01": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "730abcedbbf7471b839b1a1a062bb4f4": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "3c749dd3465646faa01e15603186bb7f": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "6ed328d77788473bb0df0be610fd7ef4": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "77cd372bec384332be2f3e23e49f9c62": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "f0538af32d8f4e55b281932669ddcda2": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "3ea40d474dd14a9a91cf9ee063d0d93e": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_f542288c15ae4723a909b396db1e5622", "IPY_MODEL_1d3bb3ad26d54ded9ca6b1fd0df358ee", "IPY_MODEL_5fd8a4d900ba4ea89b72c811f1604920"], "layout": "IPY_MODEL_49a3258eb20b4c1380fe1cafbd93237e"}}, "f542288c15ae4723a909b396db1e5622": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_9b0b4a9ba0ae4c79a8d8dd9e2248a087", "placeholder": "\u200b", "style": "IPY_MODEL_046264ef2b364e8e947c078b9846e01f", "value": "model.safetensors:\u2007reconstructing\u2007file:\u2007100%"}}, "1d3bb3ad26d54ded9ca6b1fd0df358ee": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_468b5af5666640f292b1db6348015c3c", "max": 988097824, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_7deab19ff29740a198691b13816401b4", "value": 988097824}}, "5fd8a4d900ba4ea89b72c811f1604920": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_7d645feb75e141fd861bcb8720bc2001", "placeholder": "\u200b", "style": "IPY_MODEL_591113173d1d47fd9298660f4bf5d7a3", "value": "\u2007\u2007988MB\u2007/\u2007\u2007988MB,\u200751.2MB/s\u2007\u2007"}}, "49a3258eb20b4c1380fe1cafbd93237e": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "9b0b4a9ba0ae4c79a8d8dd9e2248a087": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "046264ef2b364e8e947c078b9846e01f": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "468b5af5666640f292b1db6348015c3c": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "7deab19ff29740a198691b13816401b4": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "7d645feb75e141fd861bcb8720bc2001": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "591113173d1d47fd9298660f4bf5d7a3": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "ae73299ac1e94f6a9e5bd1cc22cf0287": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_1b02adebae5f44d4810dfe9699c73182", "IPY_MODEL_0254d7564f6d4c4cb2e00cff13adcabc", "IPY_MODEL_9e994ca6dac447b980952e85f136237d"], "layout": "IPY_MODEL_8f14b2ae532440b6a1de0f718980b281"}}, "1b02adebae5f44d4810dfe9699c73182": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_c108d6b56acf464988bfaeef838813ef", "placeholder": "\u200b", "style": "IPY_MODEL_1ef41b9b3eab4ec483f4cb8e4cee5658", "value": "model.safetensors:\u2007downloading\u2007bytes:\u2007"}}, "0254d7564f6d4c4cb2e00cff13adcabc": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_0f3bd3ed261e4c4a996d543cd6d9bb02", "max": 988097824, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_a77e03ea04934d5ebb988eb6e46dbc5d", "value": 854045206}}, "9e994ca6dac447b980952e85f136237d": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_5e1125a8a9f6429b84bb49287c1fabde", "placeholder": "\u200b", "style": "IPY_MODEL_7530690bd9324ec29ac73ebb532fe6ca", "value": "\u2007\u2007854MB,\u200769.1MB/s\u2007\u2007"}}, "8f14b2ae532440b6a1de0f718980b281": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "c108d6b56acf464988bfaeef838813ef": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "1ef41b9b3eab4ec483f4cb8e4cee5658": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "0f3bd3ed261e4c4a996d543cd6d9bb02": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "a77e03ea04934d5ebb988eb6e46dbc5d": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "5e1125a8a9f6429b84bb49287c1fabde": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "7530690bd9324ec29ac73ebb532fe6ca": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "19d3f8bb964145b09a1bc3c1525ff4f1": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_6054a92fa4ac46a8b7d26b3f3d6a0ced", "IPY_MODEL_098462434049403da0ea2b3e1bab85bb", "IPY_MODEL_11de8fee05bb414484beee70547ec770"], "layout": "IPY_MODEL_50f2744356db40928f30a456c9911fb7"}}, "6054a92fa4ac46a8b7d26b3f3d6a0ced": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_a4c464b76ccf42408699476c768ee831", "placeholder": "\u200b", "style": "IPY_MODEL_554619caa87949d68f7b144daaccbe19", "value": "Loading\u2007weights:\u2007100%"}}, "098462434049403da0ea2b3e1bab85bb": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_de744e0be387470ebbb423e35902151e", "max": 290, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_5f0a89e8cd2047d1814bd62b5814769d", "value": 290}}, "11de8fee05bb414484beee70547ec770": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_a8b5699079da415eae51bcbcd388bb9a", "placeholder": "\u200b", "style": "IPY_MODEL_30fdd840ef6c42f2a73b1489438864a1", "value": "\u2007290/290\u2007[00:00&lt;00:00,\u2007552.19it/s]"}}, "50f2744356db40928f30a456c9911fb7": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "a4c464b76ccf42408699476c768ee831": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "554619caa87949d68f7b144daaccbe19": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "de744e0be387470ebbb423e35902151e": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "5f0a89e8cd2047d1814bd62b5814769d": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "a8b5699079da415eae51bcbcd388bb9a": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "30fdd840ef6c42f2a73b1489438864a1": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "66c5bec3828f48e0bf7c4dc1965d3ba3": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_d4d809a282934510b7af08a458ba06f7", "IPY_MODEL_ca96c2b2b3e44f1c88d64053fc457279", "IPY_MODEL_453e2a2456384650b733c1d362375993"], "layout": "IPY_MODEL_aa8a2b54706141548f0e5844c9e980fd"}}, "d4d809a282934510b7af08a458ba06f7": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_9495b8bc7969426bb6727d9dedc399c3", "placeholder": "\u200b", "style": "IPY_MODEL_97e1d908faf449e38dce7851a56c8cb7", "value": "generation_config.json:\u2007100%"}}, "ca96c2b2b3e44f1c88d64053fc457279": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_c290b3e1fd7b465abea4ebe297fb4c7f", "max": 242, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_5dae17d180f041b187266af3d59b5608", "value": 242}}, "453e2a2456384650b733c1d362375993": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_5f7cfcf2d82949a4a9d842c2916bbd91", "placeholder": "\u200b", "style": "IPY_MODEL_9ae8659d79d04722a21ba2e152f07e8e", "value": "\u2007242/242\u2007[00:00&lt;00:00,\u200725.4kB/s]"}}, "aa8a2b54706141548f0e5844c9e980fd": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "9495b8bc7969426bb6727d9dedc399c3": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "97e1d908faf449e38dce7851a56c8cb7": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "c290b3e1fd7b465abea4ebe297fb4c7f": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "5dae17d180f041b187266af3d59b5608": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "5f7cfcf2d82949a4a9d842c2916bbd91": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "9ae8659d79d04722a21ba2e152f07e8e": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "5f7f061e649f41c3a9dfadd0b00093b0": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_cb09347159cb4ed797503526707c968f", "IPY_MODEL_52761cf0f0344f63b13c55cde73bf7cd", "IPY_MODEL_0d8745f3313840bab7312166b4dcb9e8"], "layout": "IPY_MODEL_e0a650b020484b83b1167bd344b81ca6"}}, "cb09347159cb4ed797503526707c968f": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_209e4d1b6b484c20a04763210839fbd3", "placeholder": "\u200b", "style": "IPY_MODEL_1a042d2b63a74f9090980094bea92527", "value": "Tokenizing\u2007train\u2007dataset:\u2007100%"}}, "52761cf0f0344f63b13c55cde73bf7cd": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_65e1144321f244f6ba568ec8b1107b43", "max": 3, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_8140459eaebc4b7683c98cb207453d74", "value": 3}}, "0d8745f3313840bab7312166b4dcb9e8": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_bb11d71c35ea4b0da6727d83f0ceff19", "placeholder": "\u200b", "style": "IPY_MODEL_3cf215ae8dfa4ca5a1152e9ea3400ed5", "value": "\u20073/3\u2007[00:00&lt;00:00,\u200768.81\u2007examples/s]"}}, "e0a650b020484b83b1167bd344b81ca6": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "209e4d1b6b484c20a04763210839fbd3": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "1a042d2b63a74f9090980094bea92527": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "65e1144321f244f6ba568ec8b1107b43": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "8140459eaebc4b7683c98cb207453d74": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "bb11d71c35ea4b0da6727d83f0ceff19": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "3cf215ae8dfa4ca5a1152e9ea3400ed5": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "164f7e7ad1d340e3ae81c70648b4fe11": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_354e662fc1134b969813ad52c82239e8", "IPY_MODEL_d90be6e381d14186aa689eac79dd9b7e", "IPY_MODEL_57eecd5c2c414c439aae06ca0fbd9dfd"], "layout": "IPY_MODEL_24fe349cc9924f6781a0e05158f2dd3c"}}, "354e662fc1134b969813ad52c82239e8": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_3b069d596435442b975a93f4be509ea4", "placeholder": "\u200b", "style": "IPY_MODEL_1f348bdace3043bb976ca156f0997c08", "value": "Tokenizing\u2007eval\u2007dataset:\u2007100%"}}, "d90be6e381d14186aa689eac79dd9b7e": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_cc47e220cf7649ada2d92e9dd95c19d4", "max": 1, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_c9cd7fdb29944ae4a9e41c0a9acf2e9b", "value": 1}}, "57eecd5c2c414c439aae06ca0fbd9dfd": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_7e6945fe854e46fdbb308e15e7cb2f13", "placeholder": "\u200b", "style": "IPY_MODEL_8fb61b0c095d464790a7695575102b04", "value": "\u20071/1\u2007[00:00&lt;00:00,\u200750.03\u2007examples/s]"}}, "24fe349cc9924f6781a0e05158f2dd3c": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "3b069d596435442b975a93f4be509ea4": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "1f348bdace3043bb976ca156f0997c08": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "cc47e220cf7649ada2d92e9dd95c19d4": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "c9cd7fdb29944ae4a9e41c0a9acf2e9b": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "7e6945fe854e46fdbb308e15e7cb2f13": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "8fb61b0c095d464790a7695575102b04": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "cb34f3848c75436798e20600f9ef9625": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_5407cd7335a04412bf3dc99e7e270b5f", "IPY_MODEL_b0197371d7a64bf6a441631877170d67", "IPY_MODEL_0ba757ad77b8439299265606ba475410"], "layout": "IPY_MODEL_555a66f928dd4cb5a5695b7b69487aab"}}, "5407cd7335a04412bf3dc99e7e270b5f": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_98ee478f413042aea1dfbde4654dd0bf", "placeholder": "\u200b", "style": "IPY_MODEL_87c12e5adf934586b6c92db2019567b4", "value": "Loading\u2007weights:\u2007100%"}}, "b0197371d7a64bf6a441631877170d67": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_eac5110224da42c087dd7c76e029b21e", "max": 290, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_1edb02242372410b9eefa1e96296e1b9", "value": 290}}, "0ba757ad77b8439299265606ba475410": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_704ac466de694570b56dfad835359aa6", "placeholder": "\u200b", "style": "IPY_MODEL_ad63f29d557046b4bc3361f1313fa9f5", "value": "\u2007290/290\u2007[00:00&lt;00:00,\u2007681.60it/s]"}}, "555a66f928dd4cb5a5695b7b69487aab": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "98ee478f413042aea1dfbde4654dd0bf": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "87c12e5adf934586b6c92db2019567b4": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "eac5110224da42c087dd7c76e029b21e": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "1edb02242372410b9eefa1e96296e1b9": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "704ac466de694570b56dfad835359aa6": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "ad63f29d557046b4bc3361f1313fa9f5": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}}}}}

## Cell 1 [markdown] execution_count=None
# Direct Preference Optimization (DPO) with Qwen2.5-0.5B-Instruct

This notebook provides a clean, end-to-end DPO training pipeline using:

- **TRL `DPOTrainer`**
- **Qwen2.5-0.5B-Instruct**
- **LoRA / optional 4-bit QLoRA**
- A small inline preference dataset, a local JSON file, or UltraFeedback
- Train/evaluation split
- Correct CUDA, BF16, and FP16 handling
- Correct PEFT adapter loading for inference
- Before/after evaluation and generation

> **Important:** The four inline examples are useful for demonstrating the pipeline, but they are far too small for meaningful model alignment. Use a larger, carefully reviewed preference dataset for a real project.

## Cell 2 [markdown] execution_count=None
## What was wrong or incomplete in the original code?

1. The inline list of four examples was displayed but never assigned to a dataset, so it was not used.
2. `bf16=torch.cuda.is_available()` is unsafe because not every CUDA GPU supports BF16.
3. `fp16=not torch.cuda.is_available()` incorrectly enables FP16 on CPU.
4. The entire 63K-row UltraFeedback dataset was trained for three epochs, which is heavy for a teaching notebook.
5. There was no evaluation split or pre/post-training evaluation.
6. A LoRA checkpoint should be loaded as a PEFT model for reliable inference.
7. The inference cell decoded the prompt together with the generated answer instead of decoding only newly generated tokens.
8. `bitsandbytes` was installed but the original model was not actually loaded in 4-bit.

## Cell 3 [markdown] execution_count=None
## 1. Install dependencies

## Cell 4 [code] execution_count=1
%pip install -q -U transformers datasets trl peft accelerate bitsandbytes sentencepiece
OUTPUT 1: stream
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m11.6/11.6 MB[0m [31m84.0 MB/s[0m eta [36m0:00:00[0m
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m555.1/555.1 kB[0m [31m38.8 MB/s[0m eta [36m0:00:00[0m
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m863.2/863.2 kB[0m [31m40.9 MB/s[0m eta [36m0:00:00[0m
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m60.7/60.7 MB[0m [31m11.2 MB/s[0m eta [36m0:00:00[0m
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m50.1/50.1 MB[0m [31m15.9 MB/s[0m eta [36m0:00:00[0m
[?25h


{}

## Cell 5 [markdown] execution_count=None
> After the installation cell finishes, restart the Colab runtime once if Colab asks you to do so. Then continue from the imports cell.

## Cell 6 [markdown] execution_count=None
## 2. Imports and reproducibility

## Cell 7 [code] execution_count=2
import gc
import json
import os
import random
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import transformers
import datasets
import trl
import peft

from datasets import Dataset, load_dataset
from peft import LoraConfig, AutoPeftModelForCausalLM
from transformers import AutoTokenizer, BitsAndBytesConfig, set_seed
from trl import DPOConfig, DPOTrainer

SEED = 42
set_seed(SEED)
random.seed(SEED)
np.random.seed(SEED)

print("PyTorch:", torch.__version__)
print("Transformers:", transformers.__version__)
print("Datasets:", datasets.__version__)
print("TRL:", trl.__version__)
print("PEFT:", peft.__version__)
OUTPUT 1: stream
PyTorch: 2.11.0+cu128
Transformers: 5.14.1
Datasets: 5.0.0
TRL: 1.8.0
PEFT: 0.19.1



{}

## Cell 8 [markdown] execution_count=None
## 3. Configuration

## Cell 9 [code] execution_count=3
MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"
OUTPUT_DIR = "outputs/qwen2_5_0_5b_dpo_lora"

# Dataset options:
#   "inline"        -> uses the four examples included below
#   "json"          -> loads a local JSON file containing prompt/chosen/rejected
#   "ultrafeedback" -> loads a subset of trl-lib/ultrafeedback_binarized
DATA_SOURCE = "inline"

JSON_PATH = "preference_data.json"
ULTRAFEEDBACK_MAX_SAMPLES = 2_000

# 4-bit QLoRA is enabled automatically on a CUDA GPU.
USE_4BIT_IF_CUDA = True

MAX_LENGTH = 512
TRAIN_BATCH_SIZE = 1
EVAL_BATCH_SIZE = 1
GRADIENT_ACCUMULATION_STEPS = 8
LEARNING_RATE = 5e-5
BETA = 0.1
INLINE_MAX_STEPS = 40

print("Model:", MODEL_NAME)
print("Dataset source:", DATA_SOURCE)
print("Output directory:", OUTPUT_DIR)
OUTPUT 1: stream
Model: Qwen/Qwen2.5-0.5B-Instruct
Dataset source: inline
Output directory: outputs/qwen2_5_0_5b_dpo_lora



{}

## Cell 10 [markdown] execution_count=None
## 4. Detect hardware and select numerical precision

## Cell 11 [code] execution_count=4
HAS_CUDA = torch.cuda.is_available()
SUPPORTS_BF16 = HAS_CUDA and torch.cuda.is_bf16_supported()

USE_BF16 = SUPPORTS_BF16
USE_FP16 = HAS_CUDA and not SUPPORTS_BF16
USE_4BIT = HAS_CUDA and USE_4BIT_IF_CUDA

if USE_BF16:
    COMPUTE_DTYPE = torch.bfloat16
elif USE_FP16:
    COMPUTE_DTYPE = torch.float16
else:
    COMPUTE_DTYPE = torch.float32

if HAS_CUDA:
    print("GPU:", torch.cuda.get_device_name(0))
else:
    print("GPU: not available; CPU training will be slow.")

print("BF16:", USE_BF16)
print("FP16:", USE_FP16)
print("4-bit QLoRA:", USE_4BIT)
print("Compute dtype:", COMPUTE_DTYPE)
OUTPUT 1: stream
GPU: Tesla T4
BF16: True
FP16: False
4-bit QLoRA: True
Compute dtype: torch.bfloat16



{}

## Cell 12 [markdown] execution_count=None
## 5. Build or load the preference dataset

## Cell 13 [code] execution_count=5
INLINE_DATA = [
    {
        "prompt": "Explain what machine learning is in simple words.",
        "chosen": "Machine learning is a way to teach computers to learn patterns from data and make predictions or decisions without being explicitly programmed for every case.",
        "rejected": "Machine learning is a machine that automatically learns everything without data.",
    },
    {
        "prompt": "What is overfitting in machine learning?",
        "chosen": "Overfitting happens when a model memorizes the training data too closely and performs poorly on new unseen data.",
        "rejected": "Overfitting means the model becomes perfect for all types of data.",
    },
    {
        "prompt": "What is the difference between classification and regression?",
        "chosen": "Classification predicts categories or labels, while regression predicts continuous numerical values.",
        "rejected": "Classification and regression are exactly the same thing.",
    },
    {
        "prompt": "What is the purpose of a loss function?",
        "chosen": "A loss function measures how far a model's predictions are from the true values, guiding the model during training.",
        "rejected": "A loss function increases model size and does not affect training.",
    },
]


def convert_plain_text_to_conversational(example):
    """Convert plain prompt/chosen/rejected strings into chat messages."""
    if isinstance(example.get("prompt"), str):
        return {
            "prompt": [{"role": "user", "content": example["prompt"]}],
            "chosen": [{"role": "assistant", "content": example["chosen"]}],
            "rejected": [{"role": "assistant", "content": example["rejected"]}],
        }
    return example


if DATA_SOURCE == "inline":
    dataset = Dataset.from_list(INLINE_DATA)
    dataset = dataset.map(convert_plain_text_to_conversational)

elif DATA_SOURCE == "json":
    json_path = Path(JSON_PATH)
    if not json_path.exists():
        raise FileNotFoundError(
            f"{JSON_PATH!r} was not found. Upload the file or change JSON_PATH."
        )

    dataset = load_dataset("json", data_files=str(json_path), split="train")
    required_columns = {"prompt", "chosen", "rejected"}
    missing = required_columns - set(dataset.column_names)
    if missing:
        raise ValueError(f"The JSON file is missing columns: {sorted(missing)}")

    dataset = dataset.map(convert_plain_text_to_conversational)

elif DATA_SOURCE == "ultrafeedback":
    dataset = load_dataset(
        "trl-lib/ultrafeedback_binarized",
        split="train",
    )
    dataset = dataset.shuffle(seed=SEED)
    sample_count = min(ULTRAFEEDBACK_MAX_SAMPLES, len(dataset))
    dataset = dataset.select(range(sample_count))

else:
    raise ValueError(
        "DATA_SOURCE must be 'inline', 'json', or 'ultrafeedback'."
    )

print(dataset)
print("\nColumns:", dataset.column_names)
print("\nFirst example:")
print(json.dumps(dataset[0], indent=2, ensure_ascii=False))
OUTPUT 1: display_data

Map:   0%|          | 0/4 [00:00<?, ? examples/s]

{}
OUTPUT 2: stream
Dataset({
    features: ['prompt', 'chosen', 'rejected'],
    num_rows: 4
})

Columns: ['prompt', 'chosen', 'rejected']

First example:
{
  "prompt": [
    {
      "role": "user",
      "content": "Explain what machine learning is in simple words."
    }
  ],
  "chosen": [
    {
      "role": "assistant",
      "content": "Machine learning is a way to teach computers to learn patterns from data and make predictions or decisions without being explicitly programmed for every case."
    }
  ],
  "rejected": [
    {
      "role": "assistant",
      "content": "Machine learning is a machine that automatically learns everything without data."
    }
  ]
}



{}

## Cell 14 [markdown] execution_count=None
## 6. Validate and split the dataset

## Cell 15 [code] execution_count=7
required_columns = {"chosen", "rejected"}
missing_columns = required_columns - set(dataset.column_names)

if missing_columns:
    raise ValueError(
        f"DPO requires chosen and rejected columns. Missing: {missing_columns}"
    )

if len(dataset) < 2:
    raise ValueError("At least two preference examples are required.")

test_size = 1 if len(dataset) < 20 else 0.05

split_dataset = dataset.train_test_split(
    test_size=test_size,
    seed=SEED,
)

train_dataset = split_dataset["train"]
eval_dataset = split_dataset["test"]

print("Training examples:", len(train_dataset))
print("Evaluation examples:", len(eval_dataset))
OUTPUT 1: stream
Training examples: 3
Evaluation examples: 1



{}

## Cell 16 [markdown] execution_count=None
## 7. Load and configure the tokenizer

## Cell 17 [code] execution_count=8
tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME,
    trust_remote_code=True,
)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

tokenizer.padding_side = "left"

print("Pad token:", tokenizer.pad_token)
print("EOS token:", tokenizer.eos_token)
print("Padding side:", tokenizer.padding_side)
OUTPUT 1: display_data

config.json:   0%|          | 0.00/659 [00:00<?, ?B/s]

{}
OUTPUT 2: display_data

tokenizer_config.json:   0%|          | 0.00/7.30k [00:00<?, ?B/s]

{}
OUTPUT 3: display_data

vocab.json:   0%|          | 0.00/2.78M [00:00<?, ?B/s]

{}
OUTPUT 4: display_data

merges.txt:   0%|          | 0.00/1.67M [00:00<?, ?B/s]

{}
OUTPUT 5: display_data

tokenizer.json:   0%|          | 0.00/7.03M [00:00<?, ?B/s]

{}
OUTPUT 6: stream
Pad token: <|endoftext|>
EOS token: <|im_end|>
Padding side: left



{}

## Cell 18 [markdown] execution_count=None
## 8. Configure optional 4-bit QLoRA

## Cell 19 [code] execution_count=9
quantization_config = None

if USE_4BIT:
    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=COMPUTE_DTYPE,
        bnb_4bit_use_double_quant=True,
    )

print("Quantization configuration:")
print(quantization_config)
OUTPUT 1: stream
Quantization configuration:
BitsAndBytesConfig {
  "_load_in_4bit": true,
  "_load_in_8bit": false,
  "bnb_4bit_compute_dtype": "bfloat16",
  "bnb_4bit_quant_storage": "uint8",
  "bnb_4bit_quant_type": "nf4",
  "bnb_4bit_use_double_quant": true,
  "llm_int8_enable_fp32_cpu_offload": false,
  "llm_int8_has_fp16_weight": false,
  "llm_int8_skip_modules": null,
  "llm_int8_threshold": 6.0,
  "load_in_4bit": true,
  "load_in_8bit": false,
  "quant_method": "bitsandbytes"
}




{}

## Cell 20 [markdown] execution_count=None
## 9. Configure LoRA

## Cell 21 [code] execution_count=10
peft_config = LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
    target_modules="all-linear",
)

print(peft_config)
OUTPUT 1: stream
LoraConfig(task_type='CAUSAL_LM', peft_type=<PeftType.LORA: 'LORA'>, auto_mapping=None, peft_version='0.19.1', base_model_name_or_path=None, revision=None, inference_mode=False, r=16, target_modules='all-linear', exclude_modules=None, lora_alpha=32, lora_dropout=0.05, fan_in_fan_out=False, bias='none', use_rslora=False, modules_to_save=None, init_lora_weights=True, layers_to_transform=None, layers_pattern=None, rank_pattern={}, alpha_pattern={}, megatron_config=None, megatron_core='megatron.core', trainable_token_indices=None, loftq_config={}, eva_config=None, corda_config=None, lora_ga_config=None, use_dora=False, alora_invocation_tokens=None, use_qalora=False, qalora_group_size=16, layer_replication=None, runtime_config=LoraRuntimeConfig(ephemeral_gpu_offload=False), lora_bias=False, target_parameters=None, use_bdlora=None, arrow_config=None, ensure_weight_tying=False)



{}

## Cell 22 [markdown] execution_count=None
## 10. Configure DPO training

## Cell 23 [code] execution_count=11
model_init_kwargs = {
    "dtype": COMPUTE_DTYPE,
    "trust_remote_code": True,
    "attn_implementation": "sdpa",
}

is_tiny_inline_demo = DATA_SOURCE == "inline"

training_args = DPOConfig(
    output_dir=OUTPUT_DIR,
    num_train_epochs=1.0,
    max_steps=INLINE_MAX_STEPS if is_tiny_inline_demo else -1,
    per_device_train_batch_size=TRAIN_BATCH_SIZE,
    per_device_eval_batch_size=EVAL_BATCH_SIZE,
    gradient_accumulation_steps=GRADIENT_ACCUMULATION_STEPS,
    learning_rate=LEARNING_RATE,
    warmup_ratio=0.1,
    lr_scheduler_type="cosine",
    optim="paged_adamw_8bit" if USE_4BIT else "adamw_torch",
    max_grad_norm=1.0,
    beta=BETA,
    loss_type="sigmoid",
    max_length=MAX_LENGTH,
    truncation_mode="keep_start",
    bf16=USE_BF16,
    fp16=USE_FP16,
    gradient_checkpointing=True,
    gradient_checkpointing_kwargs={"use_reentrant": False},
    use_cache=False,
    eval_strategy="steps",
    eval_steps=10,
    logging_steps=1,
    logging_first_step=True,
    save_strategy="steps",
    save_steps=20,
    save_total_limit=2,
    report_to="none",
    seed=SEED,
    data_seed=SEED,
    model_init_kwargs=model_init_kwargs,
)

print(training_args)
OUTPUT 1: stream
[transformers] warmup_ratio is deprecated and will be removed in v5.2. Use `warmup_steps` instead.



{}
OUTPUT 2: stream
DPOConfig(
accelerator_config={'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None, 'use_configured_state': False},
activation_offloading=False,
adam_beta1=0.9,
adam_beta2=0.999,
adam_epsilon=1e-08,
auto_find_batch_size=False,
average_tokens_across_devices=True,
batch_eval_metrics=False,
beta=0.1,
bf16=True,
bf16_full_eval=False,
data_seed=42,
dataloader_drop_last=False,
dataloader_num_workers=0,
dataloader_persistent_workers=False,
dataloader_pin_memory=True,
dataloader_prefetch_factor=None,
dataset_num_proc=None,
ddp_backend=None,
ddp_broadcast_buffers=None,
ddp_bucket_cap_mb=None,
ddp_find_unused_parameters=None,
ddp_static_graph=None,
ddp_timeout=1800,
debug=[],
deepspeed=None,
disable_dropout=True,
disable_tqdm=False,
discopop_tau=0.05,
do_eval=True,
do_predict=False,
do_train=False,
enable_jit_checkpoint=False,
eval_accumulation_steps=None,
eval_delay=0,
eval_do_concat_batches=True,
eval_on_start=False,
eval_steps=10,
eval_strategy=IntervalStrategy.STEPS,
eval_use_gather_object=False,
f_alpha_divergence_coef=0.5,
f_divergence_type=reverse_kl,
fp16=False,
fp16_full_eval=False,
fsdp=None,
fsdp_config=None,
full_determinism=False,
gradient_accumulation_steps=8,
gradient_checkpointing=True,
gradient_checkpointing_kwargs={'use_reentrant': False},
greater_is_better=None,
hub_always_push=False,
hub_model_id=None,
hub_private_repo=None,
hub_revision=None,
hub_strategy=HubStrategy.EVERY_SAVE,
hub_token=<HUB_TOKEN>,
ignore_data_skip=False,
include_for_metrics=[],
include_num_input_tokens_seen=no,
label_names=None,
label_smoothing=0.0,
label_smoothing_factor=0.0,
ld_alpha=None,
learning_rate=5e-05,
length_column_name=length,
liger_kernel_config=None,
load_best_model_at_end=False,
local_rank=-1,
log_level=passive,
log_level_replica=warning,
log_on_each_node=True,
logging_dir=None,
logging_first_step=True,
logging_nan_inf_filter=True,
logging_steps=1,
logging_strategy=IntervalStrategy.STEPS,
loss_type=['sigmoid'],
loss_weights=None,
lr_scheduler_kwargs=None,
lr_scheduler_type=SchedulerType.COSINE,
max_grad_norm=1.0,
max_length=512,
max_steps=40,
metric_for_best_model=None,
model_init_kwargs={'dtype': torch.bfloat16, 'trust_remote_code': True, 'attn_implementation': 'sdpa'},
neftune_noise_alpha=None,
num_train_epochs=1.0,
optim=OptimizerNames.PAGED_ADAMW_8BIT,
optim_args=None,
optim_target_modules=None,
output_dir=outputs/qwen2_5_0_5b_dpo_lora,
pad_to_multiple_of=None,
pad_token=<PAD_TOKEN>,
padding_free=False,
parallelism_config=None,
per_device_eval_batch_size=1,
per_device_train_batch_size=1,
precompute_ref_batch_size=None,
precompute_ref_log_probs=False,
prediction_loss_only=False,
project=huggingface,
push_to_hub=False,
ref_model_mixup_alpha=0.6,
ref_model_sync_steps=512,
remove_unused_columns=True,
report_to=[],
restore_callback_states_from_checkpoint=False,
resume_from_checkpoint=None,
router_aux_loss_coef=0.001,
run_name=None,
save_on_each_node=False,
save_only_model=False,
save_steps=20,
save_strategy=SaveStrategy.STEPS,
save_total_limit=2,
seed=42,
skip_memory_metrics=True,
sync_ref_model=False,
tf32=None,
torch_compile=False,
torch_compile_backend=None,
torch_compile_mode=None,
torch_empty_cache_steps=None,
trackio_bucket_id=None,
trackio_space_id=None,
trackio_static_space_id=None,
train_sampling_strategy=random,
truncation_mode=keep_start,
trust_remote_code=False,
use_cache=False,
use_cpu=False,
use_liger_kernel=False,
use_weighting=False,
warmup_ratio=0.1,
warmup_steps=0.1,
weight_decay=0.0,
)



{}

## Cell 24 [markdown] execution_count=None
## 11. Create the DPO trainer

`ref_model=None` is intentional. TRL uses the initial policy—the model state before DPO updates—as the reference policy. With PEFT, this avoids loading a separate full trainable copy.

## Cell 25 [code] execution_count=12
trainer = DPOTrainer(
    model=MODEL_NAME,
    ref_model=None,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    processing_class=tokenizer,
    peft_config=peft_config,
    quantization_config=quantization_config,
)

trainer.model.print_trainable_parameters()
OUTPUT 1: display_data

model.safetensors: reconstructing file:   0%|          |  0.00B /  988MB            

{}
OUTPUT 2: display_data

model.safetensors: downloading bytes:           |  0.00B            

{}
OUTPUT 3: display_data

Loading weights:   0%|          | 0/290 [00:00<?, ?it/s]

{}
OUTPUT 4: stream
/usr/local/lib/python3.12/dist-packages/bitsandbytes/backends/cuda/ops.py:213: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
  torch._check_is_size(blocksize)



{}
OUTPUT 5: display_data

generation_config.json:   0%|          | 0.00/242 [00:00<?, ?B/s]

{}
OUTPUT 6: display_data

Tokenizing train dataset:   0%|          | 0/3 [00:00<?, ? examples/s]

{}
OUTPUT 7: display_data

Tokenizing eval dataset:   0%|          | 0/1 [00:00<?, ? examples/s]

{}
OUTPUT 8: stream
trainable params: 8,798,208 || all params: 502,830,976 || trainable%: 1.7497



{}

## Cell 26 [markdown] execution_count=None
## 12. Evaluate before training

## Cell 27 [code] execution_count=13
initial_metrics = trainer.evaluate()
print("Initial evaluation metrics:")
for key, value in initial_metrics.items():
    print(f"{key}: {value}")
OUTPUT 1: display_data

<IPython.core.display.HTML object>

    <div>
      
      <progress value='1' max='1' style='width:300px; height:20px; vertical-align: middle;'></progress>
      [1/1 : < :]
    </div>
    
{}
OUTPUT 2: display_data

<IPython.core.display.HTML object>
<table border="1" class="dataframe">
  <thead>
 <tr style="text-align: left;">
      <th>Training Loss</th>
      <th>Validation Loss</th>
      <th>Step</th>
      <th>Entropy</th>
      <th>Num Tokens</th>
      <th>Logits/chosen</th>
      <th>Logits/rejected</th>
      <th>Mean Token Accuracy</th>
      <th>Rewards/chosen</th>
      <th>Rewards/rejected</th>
      <th>Rewards/accuracies</th>
      <th>Rewards/margins</th>
      <th>Logps/chosen</th>
      <th>Logps/rejected</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>No log</td>
      <td>0.693147</td>
      <td>0</td>
      <td>1.393978</td>
      <td>0.000000</td>
      <td>-2.202759</td>
      <td>-0.573546</td>
      <td>0.583333</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>-51.202583</td>
      <td>-53.960358</td>
    </tr>
  </tbody>
</table><p>
{}
OUTPUT 3: stream
Initial evaluation metrics:
eval_loss: 0.6931471824645996
eval_entropy: 1.3939778804779053
eval_num_tokens: 0.0
eval_logits/chosen: -2.2027589480082193
eval_logits/rejected: -0.5735460008893695
eval_mean_token_accuracy: 0.5833333134651184
eval_rewards/chosen: 0.0
eval_rewards/rejected: 0.0
eval_rewards/accuracies: 0.0
eval_rewards/margins: 0.0
eval_logps/chosen: -51.20258331298828
eval_logps/rejected: -53.960357666015625



{}

## Cell 28 [markdown] execution_count=None
## 13. Train the model

## Cell 29 [code] execution_count=14
train_result = trainer.train()

print("Training completed.")
print("Global steps:", trainer.state.global_step)
print("Training loss:", train_result.training_loss)
OUTPUT 1: stream
[transformers] The tokenizer has new PAD/BOS/EOS tokens that differ from the model config and generation config. The model config and generation config were aligned accordingly, being updated with the tokenizer's values. Updated tokens: {'bos_token_id': None, 'pad_token_id': 151643}.



{}
OUTPUT 2: display_data

<IPython.core.display.HTML object>

    <div>
      
      <progress value='40' max='40' style='width:300px; height:20px; vertical-align: middle;'></progress>
      [40/40 01:39, Epoch 40/40]
    </div>
    <table border="1" class="dataframe">
  <thead>
 <tr style="text-align: left;">
      <th>Step</th>
      <th>Training Loss</th>
      <th>Validation Loss</th>
      <th>Entropy</th>
      <th>Num Tokens</th>
      <th>Logits/chosen</th>
      <th>Logits/rejected</th>
      <th>Mean Token Accuracy</th>
      <th>Rewards/chosen</th>
      <th>Rewards/rejected</th>
      <th>Rewards/accuracies</th>
      <th>Rewards/margins</th>
      <th>Logps/chosen</th>
      <th>Logps/rejected</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>10</td>
      <td>0.001758</td>
      <td>0.349258</td>
      <td>1.024148</td>
      <td>3380.000000</td>
      <td>-3.026045</td>
      <td>-1.219167</td>
      <td>0.583333</td>
      <td>-0.162497</td>
      <td>-1.034734</td>
      <td>1.000000</td>
      <td>0.872237</td>
      <td>-52.827553</td>
      <td>-64.307693</td>
    </tr>
    <tr>
      <td>20</td>
      <td>0.000034</td>
      <td>0.198028</td>
      <td>0.900396</td>
      <td>6760.000000</td>
      <td>-3.343337</td>
      <td>-1.638533</td>
      <td>0.541667</td>
      <td>-0.665060</td>
      <td>-2.183758</td>
      <td>1.000000</td>
      <td>1.518698</td>
      <td>-57.853184</td>
      <td>-75.797943</td>
    </tr>
    <tr>
      <td>30</td>
      <td>0.000018</td>
      <td>0.213789</td>
      <td>0.880276</td>
      <td>10140.000000</td>
      <td>-3.414648</td>
      <td>-1.722823</td>
      <td>0.541667</td>
      <td>-0.850026</td>
      <td>-2.283993</td>
      <td>1.000000</td>
      <td>1.433968</td>
      <td>-59.702843</td>
      <td>-76.800293</td>
    </tr>
    <tr>
      <td>40</td>
      <td>0.000018</td>
      <td>0.182760</td>
      <td>0.885462</td>
      <td>13520.000000</td>
      <td>-3.419253</td>
      <td>-1.713988</td>
      <td>0.541667</td>
      <td>-0.728483</td>
      <td>-2.335294</td>
      <td>1.000000</td>
      <td>1.606812</td>
      <td>-58.487411</td>
      <td>-77.313301</td>
    </tr>
  </tbody>
</table><p>
{}
OUTPUT 3: stream
Training completed.
Global steps: 40
Training loss: 0.07717106491209051



{}

## Cell 30 [markdown] execution_count=None
## 14. Evaluate after training

## Cell 31 [code] execution_count=15
final_metrics = trainer.evaluate()

print("Final evaluation metrics:")
for key, value in final_metrics.items():
    print(f"{key}: {value}")
OUTPUT 1: display_data

<IPython.core.display.HTML object>

    <div>
      
      <progress value='1' max='1' style='width:300px; height:20px; vertical-align: middle;'></progress>
      [1/1 : < :]
    </div>
    
{}
OUTPUT 2: display_data

<IPython.core.display.HTML object>
<table border="1" class="dataframe">
  <thead>
 <tr style="text-align: left;">
      <th>Training Loss</th>
      <th>Validation Loss</th>
      <th>Step</th>
      <th>Entropy</th>
      <th>Num Tokens</th>
      <th>Logits/chosen</th>
      <th>Logits/rejected</th>
      <th>Mean Token Accuracy</th>
      <th>Rewards/chosen</th>
      <th>Rewards/rejected</th>
      <th>Rewards/accuracies</th>
      <th>Rewards/margins</th>
      <th>Logps/chosen</th>
      <th>Logps/rejected</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.000018</td>
      <td>0.182760</td>
      <td>40</td>
      <td>0.885462</td>
      <td>13520.000000</td>
      <td>-3.419253</td>
      <td>-1.713988</td>
      <td>0.541667</td>
      <td>-0.728483</td>
      <td>-2.335294</td>
      <td>1.000000</td>
      <td>1.606812</td>
      <td>-58.487411</td>
      <td>-77.313301</td>
    </tr>
  </tbody>
</table><p>
{}
OUTPUT 3: stream
Final evaluation metrics:
eval_loss: 0.18275976181030273
eval_entropy: 0.8854624032974243
eval_num_tokens: 13520.0
eval_logits/chosen: -3.4192527135213218
eval_logits/rejected: -1.7139877591814314
eval_mean_token_accuracy: 0.5416666865348816
eval_rewards/chosen: -0.7284828424453735
eval_rewards/rejected: -2.335294485092163
eval_rewards/accuracies: 1.0
eval_rewards/margins: 1.6068116426467896
eval_logps/chosen: -58.48741149902344
eval_logps/rejected: -77.31330108642578



{}

## Cell 32 [markdown] execution_count=None
## 15. Inspect the training log

## Cell 33 [code] execution_count=16
history = pd.DataFrame(trainer.state.log_history)
display(history.tail(20))

loss_history = history.dropna(subset=["loss"]) if "loss" in history.columns else pd.DataFrame()
if not loss_history.empty:
    ax = loss_history.plot(
        x="step",
        y="loss",
        title="DPO Training Loss",
        grid=True,
        figsize=(8, 4),
    )
    ax.set_ylabel("Loss")
OUTPUT 1: display_data

        loss  grad_norm  learning_rate   entropy  num_tokens  logits/chosen  \
26  0.000022   0.001114   2.065880e-05  0.413200      8450.0      -3.598195   
27  0.000021   0.001068   1.852952e-05  0.413284      8788.0      -3.609078   
28  0.000020   0.001007   1.644950e-05  0.401417      9126.0      -3.608424   
29  0.000019   0.000965   1.443454e-05  0.401460      9464.0      -3.609897   
30  0.000019   0.000931   1.250000e-05  0.402778      9802.0      -3.607100   
31  0.000018   0.000916   1.066059e-05  0.399192     10140.0      -3.610153   
32       NaN        NaN            NaN       NaN         NaN            NaN   
33  0.000019   0.000961   8.930310e-06  0.402577     10478.0      -3.611563   
34  0.000019   0.000957   7.322330e-06  0.405036     10816.0      -3.610498   
35  0.000018   0.000912   5.848889e-06  0.399434     11154.0      -3.608484   
36  0.000019   0.000942   4.521199e-06  0.401689     11492.0      -3.611997   
37  0.000018   0.000923   3.349365e-06  0.401060     11830.0      -3.614799   
38  0.000018   0.000931   2.342305e-06  0.400728     12168.0      -3.615359   
39  0.000018   0.000923   1.507684e-06  0.401944     12506.0      -3.604412   
40  0.000018   0.000935   8.518543e-07  0.398647     12844.0      -3.603152   
41  0.000018   0.000919   3.798062e-07  0.399343     13182.0      -3.609055   
42  0.000018   0.000919   9.513255e-08  0.399343     13520.0      -3.609055   
43       NaN        NaN            NaN       NaN         NaN            NaN   
44       NaN        NaN            NaN       NaN         NaN            NaN   
45       NaN        NaN            NaN       NaN         NaN            NaN   

    logits/rejected  mean_token_accuracy  rewards/chosen  rewards/rejected  \
26        -3.583806             0.876587        3.162384         -7.857215   
27        -3.590997             0.900397        3.156080         -7.912667   
28        -3.592254             0.876587        3.160409         -7.950314   
29        -3.596299             0.900397        3.168843         -7.999446   
30        -3.597114             0.900397        3.183345         -8.006614   
31        -3.599542             0.900397        3.184234         -8.010313   
32              NaN                  NaN             NaN               NaN   
33        -3.601729             0.900397        3.184252         -8.012849   
34        -3.597572             0.888492        3.167512         -8.010346   
35        -3.608003             0.876587        3.178840         -8.042852   
36        -3.598857             0.900397        3.168098         -8.019814   
37        -3.598867             0.888492        3.187361         -8.011221   
38        -3.604572             0.900397        3.166510         -8.026812   
39        -3.600096             0.876587        3.184926         -8.030901   
40        -3.593766             0.900397        3.193496         -8.028526   
41        -3.590365             0.900397        3.198801         -8.025620   
42        -3.590365             0.900397        3.198801         -8.025620   
43              NaN                  NaN             NaN               NaN   
44              NaN                  NaN             NaN               NaN   
45              NaN                  NaN             NaN               NaN   

    ...  eval_rewards/rejected  eval_rewards/accuracies  eval_rewards/margins  \
26  ...                    NaN                      NaN                   NaN   
27  ...                    NaN                      NaN                   NaN   
28  ...                    NaN                      NaN                   NaN   
29  ...                    NaN                      NaN                   NaN   
30  ...                    NaN                      NaN                   NaN   
31  ...                    NaN                      NaN                   NaN   
32  ...              -2.283993                      1.0              1.433968   
33  ...                    NaN                      NaN                   NaN   
34  ...                    NaN                      NaN                   NaN   
35  ...                    NaN                      NaN                   NaN   
36  ...                    NaN                      NaN                   NaN   
37  ...                    NaN                      NaN                   NaN   
38  ...                    NaN                      NaN                   NaN   
39  ...                    NaN                      NaN                   NaN   
40  ...                    NaN                      NaN                   NaN   
41  ...                    NaN                      NaN                   NaN   
42  ...                    NaN                      NaN                   NaN   
43  ...              -2.335294                      1.0              1.606812   
44  ...                    NaN                      NaN                   NaN   
45  ...              -2.335294                      1.0              1.606812   

    eval_logps/chosen  eval_logps/rejected  train_runtime  \
26                NaN                  NaN            NaN   
27                NaN                  NaN            NaN   
28                NaN                  NaN            NaN   
29                NaN                  NaN            NaN   
30                NaN                  NaN            NaN   
31                NaN                  NaN            NaN   
32         -59.702843           -76.800293            NaN   
33                NaN                  NaN            NaN   
34                NaN                  NaN            NaN   
35                NaN                  NaN            NaN   
36                NaN                  NaN            NaN   
37                NaN                  NaN            NaN   
38                NaN                  NaN            NaN   
39                NaN                  NaN            NaN   
40                NaN                  NaN            NaN   
41                NaN                  NaN            NaN   
42                NaN                  NaN            NaN   
43         -58.487411           -77.313301            NaN   
44                NaN                  NaN       103.8949   
45         -58.487411           -77.313301            NaN   

    train_samples_per_second  train_steps_per_second    total_flos  train_loss  
26                       NaN                     NaN           NaN         NaN  
27                       NaN                     NaN           NaN         NaN  
28                       NaN                     NaN           NaN         NaN  
29                       NaN                     NaN           NaN         NaN  
30                       NaN                     NaN           NaN         NaN  
31                       NaN                     NaN           NaN         NaN  
32                       NaN                     NaN           NaN         NaN  
33                       NaN                     NaN           NaN         NaN  
34                       NaN                     NaN           NaN         NaN  
35                       NaN                     NaN           NaN         NaN  
36                       NaN                     NaN           NaN         NaN  
37                       NaN                     NaN           NaN         NaN  
38                       NaN                     NaN           NaN         NaN  
39                       NaN                     NaN           NaN         NaN  
40                       NaN                     NaN           NaN         NaN  
41                       NaN                     NaN           NaN         NaN  
42                       NaN                     NaN           NaN         NaN  
43                       NaN                     NaN           NaN         NaN  
44                      3.08                   0.385  3.203459e+13    0.077171  
45                       NaN                     NaN           NaN         NaN  

[20 rows x 37 columns]

  <div id="df-7dfe425f-66f8-4055-8968-c2f67da64b01" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>loss</th>
      <th>grad_norm</th>
      <th>learning_rate</th>
      <th>entropy</th>
      <th>num_tokens</th>
      <th>logits/chosen</th>
      <th>logits/rejected</th>
      <th>mean_token_accuracy</th>
      <th>rewards/chosen</th>
      <th>rewards/rejected</th>
      <th>...</th>
      <th>eval_rewards/rejected</th>
      <th>eval_rewards/accuracies</th>
      <th>eval_rewards/margins</th>
      <th>eval_logps/chosen</th>
      <th>eval_logps/rejected</th>
      <th>train_runtime</th>
      <th>train_samples_per_second</th>
      <th>train_steps_per_second</th>
      <th>total_flos</th>
      <th>train_loss</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>26</th>
      <td>0.000022</td>
      <td>0.001114</td>
      <td>2.065880e-05</td>
      <td>0.413200</td>
      <td>8450.0</td>
      <td>-3.598195</td>
      <td>-3.583806</td>
      <td>0.876587</td>
      <td>3.162384</td>
      <td>-7.857215</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>27</th>
      <td>0.000021</td>
      <td>0.001068</td>
      <td>1.852952e-05</td>
      <td>0.413284</td>
      <td>8788.0</td>
      <td>-3.609078</td>
      <td>-3.590997</td>
      <td>0.900397</td>
      <td>3.156080</td>
      <td>-7.912667</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>28</th>
      <td>0.000020</td>
      <td>0.001007</td>
      <td>1.644950e-05</td>
      <td>0.401417</td>
      <td>9126.0</td>
      <td>-3.608424</td>
      <td>-3.592254</td>
      <td>0.876587</td>
      <td>3.160409</td>
      <td>-7.950314</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>29</th>
      <td>0.000019</td>
      <td>0.000965</td>
      <td>1.443454e-05</td>
      <td>0.401460</td>
      <td>9464.0</td>
      <td>-3.609897</td>
      <td>-3.596299</td>
      <td>0.900397</td>
      <td>3.168843</td>
      <td>-7.999446</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>30</th>
      <td>0.000019</td>
      <td>0.000931</td>
      <td>1.250000e-05</td>
      <td>0.402778</td>
      <td>9802.0</td>
      <td>-3.607100</td>
      <td>-3.597114</td>
      <td>0.900397</td>
      <td>3.183345</td>
      <td>-8.006614</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>31</th>
      <td>0.000018</td>
      <td>0.000916</td>
      <td>1.066059e-05</td>
      <td>0.399192</td>
      <td>10140.0</td>
      <td>-3.610153</td>
      <td>-3.599542</td>
      <td>0.900397</td>
      <td>3.184234</td>
      <td>-8.010313</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>32</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>-2.283993</td>
      <td>1.0</td>
      <td>1.433968</td>
      <td>-59.702843</td>
      <td>-76.800293</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>33</th>
      <td>0.000019</td>
      <td>0.000961</td>
      <td>8.930310e-06</td>
      <td>0.402577</td>
      <td>10478.0</td>
      <td>-3.611563</td>
      <td>-3.601729</td>
      <td>0.900397</td>
      <td>3.184252</td>
      <td>-8.012849</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>34</th>
      <td>0.000019</td>
      <td>0.000957</td>
      <td>7.322330e-06</td>
      <td>0.405036</td>
      <td>10816.0</td>
      <td>-3.610498</td>
      <td>-3.597572</td>
      <td>0.888492</td>
      <td>3.167512</td>
      <td>-8.010346</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>35</th>
      <td>0.000018</td>
      <td>0.000912</td>
      <td>5.848889e-06</td>
      <td>0.399434</td>
      <td>11154.0</td>
      <td>-3.608484</td>
      <td>-3.608003</td>
      <td>0.876587</td>
      <td>3.178840</td>
      <td>-8.042852</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>36</th>
      <td>0.000019</td>
      <td>0.000942</td>
      <td>4.521199e-06</td>
      <td>0.401689</td>
      <td>11492.0</td>
      <td>-3.611997</td>
      <td>-3.598857</td>
      <td>0.900397</td>
      <td>3.168098</td>
      <td>-8.019814</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>37</th>
      <td>0.000018</td>
      <td>0.000923</td>
      <td>3.349365e-06</td>
      <td>0.401060</td>
      <td>11830.0</td>
      <td>-3.614799</td>
      <td>-3.598867</td>
      <td>0.888492</td>
      <td>3.187361</td>
      <td>-8.011221</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>38</th>
      <td>0.000018</td>
      <td>0.000931</td>
      <td>2.342305e-06</td>
      <td>0.400728</td>
      <td>12168.0</td>
      <td>-3.615359</td>
      <td>-3.604572</td>
      <td>0.900397</td>
      <td>3.166510</td>
      <td>-8.026812</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>39</th>
      <td>0.000018</td>
      <td>0.000923</td>
      <td>1.507684e-06</td>
      <td>0.401944</td>
      <td>12506.0</td>
      <td>-3.604412</td>
      <td>-3.600096</td>
      <td>0.876587</td>
      <td>3.184926</td>
      <td>-8.030901</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>40</th>
      <td>0.000018</td>
      <td>0.000935</td>
      <td>8.518543e-07</td>
      <td>0.398647</td>
      <td>12844.0</td>
      <td>-3.603152</td>
      <td>-3.593766</td>
      <td>0.900397</td>
      <td>3.193496</td>
      <td>-8.028526</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>41</th>
      <td>0.000018</td>
      <td>0.000919</td>
      <td>3.798062e-07</td>
      <td>0.399343</td>
      <td>13182.0</td>
      <td>-3.609055</td>
      <td>-3.590365</td>
      <td>0.900397</td>
      <td>3.198801</td>
      <td>-8.025620</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>42</th>
      <td>0.000018</td>
      <td>0.000919</td>
      <td>9.513255e-08</td>
      <td>0.399343</td>
      <td>13520.0</td>
      <td>-3.609055</td>
      <td>-3.590365</td>
      <td>0.900397</td>
      <td>3.198801</td>
      <td>-8.025620</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>43</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>-2.335294</td>
      <td>1.0</td>
      <td>1.606812</td>
      <td>-58.487411</td>
      <td>-77.313301</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>44</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>103.8949</td>
      <td>3.08</td>
      <td>0.385</td>
      <td>3.203459e+13</td>
      <td>0.077171</td>
    </tr>
    <tr>
      <th>45</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>-2.335294</td>
      <td>1.0</td>
      <td>1.606812</td>
      <td>-58.487411</td>
      <td>-77.313301</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>20 rows × 37 columns</p>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-7dfe425f-66f8-4055-8968-c2f67da64b01')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-7dfe425f-66f8-4055-8968-c2f67da64b01 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-7dfe425f-66f8-4055-8968-c2f67da64b01');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>


    </div>
  </div>

{}
OUTPUT 2: display_data

<Figure size 800x400 with 1 Axes>

{}

## Cell 34 [markdown] execution_count=None
## 16. Save the LoRA adapter and tokenizer

## Cell 35 [code] execution_count=17
trainer.save_model(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)

print(f"Saved DPO LoRA adapter and tokenizer to: {OUTPUT_DIR}")
print("Saved files:")
for file_name in sorted(os.listdir(OUTPUT_DIR)):
    print(" -", file_name)
OUTPUT 1: stream
Saved DPO LoRA adapter and tokenizer to: outputs/qwen2_5_0_5b_dpo_lora
Saved files:
 - README.md
 - adapter_config.json
 - adapter_model.safetensors
 - chat_template.jinja
 - checkpoint-20
 - checkpoint-40
 - tokenizer.json
 - tokenizer_config.json
 - training_args.bin



{}

## Cell 36 [markdown] execution_count=None
## 17. Release training memory

## Cell 37 [code] execution_count=18
del trainer
gc.collect()

if torch.cuda.is_available():
    torch.cuda.empty_cache()

print("Training objects released.")
OUTPUT 1: stream
Training objects released.



{}

## Cell 38 [markdown] execution_count=None
## 18. Load the trained PEFT adapter for inference

## Cell 39 [code] execution_count=19
inference_load_kwargs = {
    "torch_dtype": COMPUTE_DTYPE,
}

if HAS_CUDA:
    inference_load_kwargs["device_map"] = "auto"

if quantization_config is not None:
    inference_load_kwargs["quantization_config"] = quantization_config

model = AutoPeftModelForCausalLM.from_pretrained(
    OUTPUT_DIR,
    **inference_load_kwargs,
)
model.eval()

tokenizer = AutoTokenizer.from_pretrained(
    OUTPUT_DIR,
    trust_remote_code=True,
)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

tokenizer.padding_side = "left"

print("DPO adapter loaded successfully.")
OUTPUT 1: stream
[transformers] `torch_dtype` is deprecated! Use `dtype` instead!



{}
OUTPUT 2: display_data

Loading weights:   0%|          | 0/290 [00:00<?, ?it/s]

{}
OUTPUT 3: stream
/usr/local/lib/python3.12/dist-packages/bitsandbytes/backends/cuda/ops.py:213: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
  torch._check_is_size(blocksize)



{}
OUTPUT 4: stream
DPO adapter loaded successfully.



{}

## Cell 40 [markdown] execution_count=None
## 19. Generate a response

## Cell 41 [code] execution_count=20
def generate_response(
    prompt: str,
    max_new_tokens: int = 150,
    temperature: float = 0.7,
    top_p: float = 0.9,
) -> str:
    messages = [{"role": "user", "content": prompt}]

    formatted_prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )

    inputs = tokenizer(
        formatted_prompt,
        return_tensors="pt",
    ).to(model.device)

    prompt_token_count = inputs["input_ids"].shape[1]

    generation_kwargs = {
        "max_new_tokens": max_new_tokens,
        "pad_token_id": tokenizer.pad_token_id,
        "eos_token_id": tokenizer.eos_token_id,
    }

    if temperature > 0:
        generation_kwargs.update(
            {
                "do_sample": True,
                "temperature": temperature,
                "top_p": top_p,
            }
        )
    else:
        generation_kwargs["do_sample"] = False

    with torch.inference_mode():
        outputs = model.generate(
            **inputs,
            **generation_kwargs,
        )

    new_tokens = outputs[0, prompt_token_count:]
    return tokenizer.decode(
        new_tokens,
        skip_special_tokens=True,
    ).strip()


prompt = "Explain overfitting in machine learning in simple words."
response = generate_response(prompt)

print("Prompt:")
print(prompt)
print("\nDPO response:")
print(response)
OUTPUT 1: stream
/usr/local/lib/python3.12/dist-packages/bitsandbytes/backends/cuda/ops.py:468: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
  torch._check_is_size(blocksize)



{}
OUTPUT 2: stream
Prompt:
Explain overfitting in machine learning in simple words.

DPO response:
Overfitting happens when your model memorizes the data too much and learns patterns that it hasn't seen during training. It's like if you try to draw a picture of a cat using only one drawing paper instead of multiple ones - you'll end up with a picture of a cat, not a real one. Overfitting makes predictions that don't generalize well to new data.



{}

## Cell 42 [markdown] execution_count=None
## 20. Test several prompts

## Cell 43 [code] execution_count=21
test_prompts = [
    "Explain machine learning in simple words.",
    "What is overfitting?",
    "How are classification and regression different?",
    "What does a loss function do?",
]

for current_prompt in test_prompts:
    print("=" * 80)
    print("PROMPT:", current_prompt)
    print("RESPONSE:", generate_response(current_prompt, temperature=0.3))
OUTPUT 1: stream
================================================================================
PROMPT: Explain machine learning in simple words.
RESPONSE: Machine learning is like teaching computers to learn patterns from data and make predictions or decisions based on that learning. It's used to help computers understand the world around us and make sense of it for us!
================================================================================
PROMPT: What is overfitting?
RESPONSE: Overfitting occurs when a model memorizes the training data too closely and performs poorly on new unseen data. It happens because the model has learned the details of the training set too well, but not enough to generalize well to new data. This can happen due to various reasons such as noise in the training data, lack of diversity in the dataset, or insufficiently large training size. Overfitting can lead to poor generalization performance and high prediction errors.
================================================================================
PROMPT: How are classification and regression different?
RESPONSE: Classification predicts categorical labels or categories, while regression predicts continuous numerical values. The main difference is that classification models use probability estimates to predict the likelihood of each label, while regression models use linear relationships between features and target variables.
================================================================================
PROMPT: What does a loss function do?
RESPONSE: A loss function is a mathematical function used to evaluate the performance of a model and determine how well it has predicted the target labels. It is typically used in training neural networks and is often optimized using techniques like gradient descent.
The primary goal of a loss function is to minimize its value when trained on data, which means that it should be able to capture the differences between predicted and actual labels as closely as possible. The loss function can take various forms, such as mean squared error (MSE), cross-entropy, or categorical cross-entropy, depending on the nature of the prediction task.
In summary, a loss function helps to evaluate the quality of predictions and guide the optimization process for better model performance.



{}

## Cell 44 [markdown] execution_count=None
## 21. Download the trained adapter from Colab

## Cell 45 [code] execution_count=22
import shutil

archive_path = shutil.make_archive(
    base_name="qwen2_5_0_5b_dpo_lora",
    format="zip",
    root_dir=OUTPUT_DIR,
)

print("Created:", archive_path)

# Uncomment in Google Colab:
# from google.colab import files
# files.download(archive_path)
OUTPUT 1: stream
Created: /content/qwen2_5_0_5b_dpo_lora.zip



{}

## Cell 46 [markdown] execution_count=None
## Notes for real training

- Four examples only demonstrate that the pipeline runs; they cannot produce a generally aligned model.
- Prefer thousands of high-quality, diverse, correctly labeled preference pairs.
- Keep the prompt distribution close to the model's SFT distribution.
- Evaluate preference accuracy, reward margins, response quality, safety, and held-out generalization.
- A lower DPO loss alone does not prove that the resulting model is better.
- Inspect chosen and rejected responses for label noise, formatting differences, response-length bias, and data leakage.

## Cell 47 [markdown] execution_count=None
## Official references

- TRL DPO Trainer: https://huggingface.co/docs/trl/dpo_trainer
- TRL PEFT integration: https://huggingface.co/docs/trl/peft_integration
- PEFT AutoPeftModel: https://huggingface.co/docs/peft/package_reference/auto_class
- Transformers bitsandbytes quantization: https://huggingface.co/docs/transformers/quantization/bitsandbytes