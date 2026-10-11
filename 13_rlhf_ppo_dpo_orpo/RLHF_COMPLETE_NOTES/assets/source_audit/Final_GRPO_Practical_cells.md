# Final_GRPO_Practical.ipynb
Metadata: {"colab": {"provenance": [], "gpuType": "T4"}, "kernelspec": {"name": "python3", "display_name": "Python 3"}, "language_info": {"name": "python"}, "accelerator": "GPU", "widgets": {"application/vnd.jupyter.widget-state+json": {"version_major": 2, "version_minor": 0, "state": {"2971b9e9cf7e41f7b02a4c232f59b3f8": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_cc1b218708414c88a23934ebd3647999", "IPY_MODEL_3867d72b0f434b8e9d1959a8c329e15e", "IPY_MODEL_f161441bcc1f47198d0273a5ec9e36f9"], "layout": "IPY_MODEL_0fb39f5c6d454999a844b5587d9f655c"}}, "cc1b218708414c88a23934ebd3647999": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_c84792d8f9dd468aa0fd895d3c40f8e6", "placeholder": "\u200b", "style": "IPY_MODEL_88e0dbf785be424fbfc9e7659730750c", "value": "Map:\u2007100%"}}, "3867d72b0f434b8e9d1959a8c329e15e": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_98ee8f1d90de41729f05b20219d18309", "max": 8, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_bf8796c5c045497b9cc45230c952dc4b", "value": 8}}, "f161441bcc1f47198d0273a5ec9e36f9": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_0287f6e392b24057bcea5a76a2452324", "placeholder": "\u200b", "style": "IPY_MODEL_b677e767d0314018a9b3a78319b2bb49", "value": "\u20078/8\u2007[00:00&lt;00:00,\u2007166.25\u2007examples/s]"}}, "0fb39f5c6d454999a844b5587d9f655c": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "c84792d8f9dd468aa0fd895d3c40f8e6": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "88e0dbf785be424fbfc9e7659730750c": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "98ee8f1d90de41729f05b20219d18309": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "bf8796c5c045497b9cc45230c952dc4b": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "0287f6e392b24057bcea5a76a2452324": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "b677e767d0314018a9b3a78319b2bb49": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "bf62e234e41045b7b6adf349a6783109": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_336e893ea31648e8a1f79adf0330f082", "IPY_MODEL_0f5906f003b24611a4722bdfb07db416", "IPY_MODEL_828e1959a9544dfe804c878a51ec7867"], "layout": "IPY_MODEL_cd78509decbb4a9c990d3b78123eefab"}}, "336e893ea31648e8a1f79adf0330f082": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_aaed1073e3194d369a49fc85cbb4c85b", "placeholder": "\u200b", "style": "IPY_MODEL_cf8d50885a9e4cfc93ba550220daa922", "value": "Loading\u2007weights:\u2007100%"}}, "0f5906f003b24611a4722bdfb07db416": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_f5328081d7f14870a0f8c18dda2d5266", "max": 272, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_9df1f95732ec4f918037384b46c3e130", "value": 272}}, "828e1959a9544dfe804c878a51ec7867": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_a9f7aceb132d4d8ba2a4beb34508d404", "placeholder": "\u200b", "style": "IPY_MODEL_a00229f9eeb44c98ab275dd1e3d5c2d2", "value": "\u2007272/272\u2007[00:00&lt;00:00,\u2007564.14it/s]"}}, "cd78509decbb4a9c990d3b78123eefab": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "aaed1073e3194d369a49fc85cbb4c85b": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "cf8d50885a9e4cfc93ba550220daa922": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "f5328081d7f14870a0f8c18dda2d5266": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "9df1f95732ec4f918037384b46c3e130": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "a9f7aceb132d4d8ba2a4beb34508d404": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "a00229f9eeb44c98ab275dd1e3d5c2d2": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "37d043f17e4845c7bee48b18c05a313b": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_75f8682d61f245ae9ceab4f8b14b5e9a", "IPY_MODEL_d71808230d4746daa451c6aa1f8985eb", "IPY_MODEL_0de3ad9c0ba841648a68178f09e9c0bd"], "layout": "IPY_MODEL_33edf4e4693d4bc7a9c4e7b80e6fe298"}}, "75f8682d61f245ae9ceab4f8b14b5e9a": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_482ac3d9915447c78d696567045ab691", "placeholder": "\u200b", "style": "IPY_MODEL_eda5b1f150d542eaadc1696cb03d0a97", "value": "Loading\u2007weights:\u2007100%"}}, "d71808230d4746daa451c6aa1f8985eb": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_3d3197d6e0554d21b0cf7d304b9fcdc4", "max": 272, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_0ad533240285473098beefed7addd126", "value": 272}}, "0de3ad9c0ba841648a68178f09e9c0bd": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_d603d668ba73498084332ad29350d97a", "placeholder": "\u200b", "style": "IPY_MODEL_42d89ae6f8944bdaa8abec16730ee0f4", "value": "\u2007272/272\u2007[00:00&lt;00:00,\u2007980.37it/s]"}}, "33edf4e4693d4bc7a9c4e7b80e6fe298": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "482ac3d9915447c78d696567045ab691": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "eda5b1f150d542eaadc1696cb03d0a97": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "3d3197d6e0554d21b0cf7d304b9fcdc4": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "0ad533240285473098beefed7addd126": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "d603d668ba73498084332ad29350d97a": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "42d89ae6f8944bdaa8abec16730ee0f4": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}}}}}

## Cell 1 [code] execution_count=None
!pip install -q -U datasets transformers trl peft accelerate bitsandbytes
!pip uninstall -y torchao

## Cell 2 [markdown] execution_count=None
torchao is an optional PyTorch optimization/quantization package. Our GRPO practical does not need it. But PEFT detects the old installed torchao version and throws a compatibility error. So we remove torchao to avoid this conflict.

## Cell 3 [code] execution_count=None
import re
import torch
from difflib import SequenceMatcher
from datasets import Dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, PeftModel
from trl import GRPOConfig, GRPOTrainer

## Cell 4 [markdown] execution_count=None
| Code component         | Story character                                    |
| ---------------------- | -------------------------------------------------- |
| `SmolLM-135M-Instruct` | The AI student                                     |
| Dataset prompts        | Exam questions                                     |
| `reference_answer`     | Teacher’s answer key                               |
| Reward functions       | Three teachers/judges                              |

## Cell 5 [code] execution_count=None
data = [
    {
        "prompt": "Explain reinforcement learning in simple terms.",
        "reference_answer": "Reinforcement learning is a type of machine learning where an agent learns by taking actions, receiving rewards or penalties, and improving over time.",
    },
    {
        "prompt": "Write a polite email for delayed delivery.",
        "reference_answer": "We apologize for the delay in your delivery. Your order is on the way, and we appreciate your patience and understanding.",
    },
    {
        "prompt": "What is a neural network?",
        "reference_answer": "A neural network is a machine learning model inspired by the human brain. It learns patterns from data using layers of connected nodes.",
    },
    {
        "prompt": "Explain overfitting in ML.",
        "reference_answer": "Overfitting happens when a model learns the training data too closely, including noise, and performs poorly on new unseen data.",
    },
    {
        "prompt": "Explain supervised learning in simple terms.",
        "reference_answer": "Supervised learning is a machine learning method where a model learns from labeled examples and then predicts outputs for new data.",
    },
    {
        "prompt": "What is gradient descent?",
        "reference_answer": "Gradient descent is an optimization method that helps a model reduce its error by slowly adjusting its parameters in the right direction.",
    },
    {
        "prompt": "Explain classification in machine learning.",
        "reference_answer": "Classification is a machine learning task where the model assigns input data to predefined categories or classes.",
    },
    {
        "prompt": "Write a simple apology message.",
        "reference_answer": "I am sorry for the inconvenience. Thank you for your patience and understanding.",
    },
]

## Cell 6 [markdown] execution_count=None
Prompt goes to model

↓

Model generates answers

↓

Reward function compares answers with reference_answer

↓

Good answer gets high reward

↓

Bad answer gets low reward

↓

GRPO updates model


## Cell 7 [markdown] execution_count=None
In GRPO, our dataset mainly provides prompts. The model generates multiple answers for each prompt, then reward functions compare those answers with reference answers and give scores. GRPO does not directly copy the reference answer like SFT; it learns by getting higher rewards for better completions.

## Cell 8 [code] execution_count=None
def format_prompt(example):
    return {
        "prompt": f"Question: {example['prompt']}\nAnswer in simple English:"
    }

## Cell 9 [code] execution_count=None
dataset = Dataset.from_list(data)
dataset = dataset.map(format_prompt)
OUTPUT 1: display_data

Map:   0%|          | 0/8 [00:00<?, ? examples/s]

{}
OUTPUT 2: execute_result

Dataset({
    features: ['prompt', 'reference_answer'],
    num_rows: 8
})

{}

## Cell 10 [code] execution_count=None
dataset

## Cell 11 [markdown] execution_count=None
{
    'prompt': 'Question: Explain reinforcement learning in simple terms.\nAnswer in simple English:',
    'reference_answer': 'Reinforcement learning is a type of machine learning where an agent learns by taking actions, receiving rewards or penalties, and improving over time.'
}

## Cell 12 [code] execution_count=None
model_id = "HuggingFaceTB/SmolLM-135M-Instruct"

## Cell 13 [code] execution_count=None
tokenizer = AutoTokenizer.from_pretrained(model_id)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

tokenizer.padding_side = "left"

## Cell 14 [code] execution_count=None
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto",
)

model.config.pad_token_id = tokenizer.pad_token_id
OUTPUT 1: stream
[transformers] `torch_dtype` is deprecated! Use `dtype` instead!



{}
OUTPUT 2: display_data

Loading weights:   0%|          | 0/272 [00:00<?, ?it/s]

{}

## Cell 15 [code] execution_count=None
lora_config = LoraConfig(
    task_type="CAUSAL_LM",
    r=8,
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
)

## Cell 16 [markdown] execution_count=None
1. Rule-based/verifiable reward

2. Reward model

3. Existing/built-in reward functions

## Cell 17 [markdown] execution_count=None
| Approach                                    | What it means                                                            | Where it is used                                      | Example                                                          | Practical meaning                                                     |
| ------------------------------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------- | ---------------------------------------------------------------- | --------------------------------------------------------------------- |
| **1. Rule-based / Verifiable Reward**       | We write clear rules to check whether the model output is correct or not | Math, coding, JSON/XML format, exact-answer tasks     | Final answer is correct or not, code test cases passed or failed | Simple and reliable when the answer can be verified                   |
| **2. Reward Model**                         | A separate model gives a score to the generated output                   | Open-ended answers, helpfulness, preference alignment | How helpful, safe, clear, or preferred the answer is             | Human preference is converted into a model-based score                |
| **3. Built-in / Reusable Reward Functions** | We use existing reward functions or reusable custom functions            | Demos, standard tasks, formatting, accuracy checks    | Accuracy reward, format reward, length reward                    | We do not need to write every reward function from scratch every time |


## Cell 18 [markdown] execution_count=None
| Component                | PPO                        | GRPO                                                        |
| ------------------------ | -------------------------- | ----------------------------------------------------------- |
| **Policy model**         | Present                    | Present                                                     |
| **Reward model**         | Present                    | can be used                                       |
| **Reference model**      | Present                    | Present                                                     |
| **Value / Critic model** | Present                    | **Not required**                                            |
| **Baseline**             | Comes from the value model | Comes from the average reward of multiple generated answers |


## Cell 19 [code] execution_count=None
#Text cleaning
def normalize_text(text: str) -> str:
    text = str(text).lower().strip()
    text = re.sub(r"\s+", " ", text)
    return text

## Cell 20 [markdown] execution_count=None
"   Reinforcement   Learning IS useful. "

"reinforcement learning is useful."

## Cell 21 [code] execution_count=None
#This function safely extracts the answer text from either a normal string or chat-message format, and converts unknown formats into a string.
def get_completion_text(completion):
    """
    Works for normal string completions.
    Also safe if completion comes in chat/message format.
    """
    if isinstance(completion, str):
        return completion

    if isinstance(completion, list):
        try:
            return completion[-1]["content"]
        except Exception:
            return str(completion)

    return str(completion)

## Cell 22 [code] execution_count=None
#It cleans both texts, compares their character/word sequence using SequenceMatcher, and returns a similarity score from 0 to 1—1 means identical and 0 means completely different.
def similarity_score(a: str, b: str) -> float:
    return SequenceMatcher(None, normalize_text(a), normalize_text(b)).ratio()

## Cell 23 [code] execution_count=None
# This function extracts unique words of at least 3 letters from both texts and returns the fraction of reference-text words (b) that also appear in the generated text (a).

# Example:

# a = "Machine learning uses data"
# b = "Machine learning learns from data"

# Common words: machine, learning, data

# So the score is:

# 3 common words ÷ 5 reference words = 0.6

def keyword_overlap_score(a: str, b: str) -> float:
    a_words = set(re.findall(r"[a-zA-Z]{3,}", normalize_text(a)))
    b_words = set(re.findall(r"[a-zA-Z]{3,}", normalize_text(b)))

    if not b_words:
        return 0.0

    return len(a_words & b_words) / len(b_words)

## Cell 24 [code] execution_count=None
# It acts like a teacher that compares the model’s answer with the answer key and gives marks out of 5.
def correctness_reward(prompts, completions, reference_answer=None, **kwargs):
    """
    Rewards answer similarity with reference answer.
    This is okay for demo, but not ideal for real production RL.
    """
    rewards = []

    if reference_answer is None:
        return [0.0 for _ in completions]

    for completion, ref in zip(completions, reference_answer):
        text = get_completion_text(completion)

        sim = similarity_score(text, ref)
        overlap = keyword_overlap_score(text, ref)

        # Combined correctness reward: 0 to 5
        score = (2.5 * sim) + (2.5 * overlap)
        rewards.append(float(score))

    return rewards

## Cell 25 [code] execution_count=None
# It acts like a teacher who rewards complete and properly written answers and penalizes short, vague, or unhelpful answers.
def helpfulness_reward(prompts, completions, **kwargs):
    """
    Rewards answers that look useful and complete.
    Penalizes vague/unhelpful responses.
    """
    rewards = []

    bad_phrases = [
        "i don't know",
        "no idea",
        "maybe",
        "not sure",
        "random magic",
    ]

    for completion in completions:
        text = get_completion_text(completion)
        text_norm = normalize_text(text)

        score = 0.0

        # Good answer length
        if 40 <= len(text) <= 260:
            score += 1.0
        elif len(text) < 20:
            score -= 1.0
        elif len(text) > 350:
            score -= 0.5

        # Sentence-like response
        if "." in text or "," in text:
            score += 0.5

        # Penalize vague responses
        if any(bp in text_norm for bp in bad_phrases):
            score -= 1.5

        rewards.append(float(score))

    return rewards

## Cell 26 [code] execution_count=None
# It acts like a teacher who rewards readable, properly sized answers and penalizes unclear or repetitive output.
def clarity_reward(prompts, completions, **kwargs):
    """
    Rewards readable English-style answers.
    """
    rewards = []

    for completion in completions:
        text = get_completion_text(completion)
        text_norm = normalize_text(text)

        score = 0.0

        # Has alphabetic content
        if re.search(r"[A-Za-z]", text):
            score += 0.5

        # Not too short / not too long
        if 30 <= len(text) <= 280:
            score += 0.5
        else:
            score -= 0.5

        # Penalize repeated junk
        if re.search(r"(.)\1{8,}", text_norm):
            score -= 1.0

        rewards.append(float(score))

    return rewards

## Cell 27 [markdown] execution_count=None
In GRPO, the model does not directly learn from a fixed label like SFT. It generates multiple answers, and then reward functions score those answers. This code is only creating those reward functions: correctness checks similarity with the reference answer, helpfulness checks whether the answer is useful, and clarity checks whether the answer is readable. GRPOTrainer uses these scores to improve the model.

## Cell 28 [markdown] execution_count=None
In GRPO, reward function is the teacher signal. For a demo, we can manually write simple rewards like correctness, helpfulness, and clarity. But in real systems, we do not keep writing unlimited reward functions manually. We usually use verifiable rewards, test cases, exact answer matching, LLM-as-judge, or a trained reward model. GRPO only needs a reward score; how we produce that reward depends on the task

## Cell 29 [code] execution_count=None
training_args = GRPOConfig(
    output_dir="grpo_output",

    learning_rate=1e-5,

    # Important:
    # In TRL GRPO, per_device_train_batch_size should be divisible by num_generations.
    # So we keep both as 4 for simple single-GPU Colab demo.
    per_device_train_batch_size=4,
    gradient_accumulation_steps=1,
    num_generations=4,

    max_completion_length=80,

    temperature=0.9,
    top_p=0.95,

    # KL penalty. 0.0 is default in recent TRL GRPO, but 0.01 is okay for teaching demo.
    beta=0.01,

    max_steps=10,

    logging_steps=1,
    save_steps=10,

    remove_unused_columns=False,
    report_to="none",

    gradient_checkpointing=False,

    fp16=torch.cuda.is_available(),
)

## Cell 30 [code] execution_count=None
trainer = GRPOTrainer(
    model=model,
    processing_class=tokenizer,
    reward_funcs=[
        correctness_reward,
        helpfulness_reward,
        clarity_reward,
    ],
    args=training_args,
    train_dataset=dataset,
    peft_config=lora_config,
)

## Cell 31 [code] execution_count=None
import trl
import inspect
from trl import GRPOConfig

print("TRL version:", trl.__version__)
print(inspect.signature(GRPOConfig.__init__))
OUTPUT 1: stream
TRL version: 1.7.0
(self, output_dir: str | None = None, per_device_train_batch_size: int = 8, num_train_epochs: float = 3.0, max_steps: int = -1, learning_rate: float = 1e-06, lr_scheduler_type: transformers.trainer_utils.SchedulerType | str = 'linear', lr_scheduler_kwargs: dict | str | None = None, warmup_steps: float = 0, optim: transformers.training_args.OptimizerNames | str = 'adamw_torch_fused', optim_args: str | None = None, weight_decay: float = 0.0, adam_beta1: float = 0.9, adam_beta2: float = 0.999, adam_epsilon: float = 1e-08, optim_target_modules: None | str | list[str] = None, gradient_accumulation_steps: int = 1, average_tokens_across_devices: bool = True, max_grad_norm: float = 1.0, label_smoothing_factor: float = 0.0, bf16: bool | None = None, fp16: bool = False, bf16_full_eval: bool = False, fp16_full_eval: bool = False, tf32: bool | None = None, gradient_checkpointing: bool = True, gradient_checkpointing_kwargs: dict[str, typing.Any] | str | None = None, torch_compile: bool = False, torch_compile_backend: str | None = None, torch_compile_mode: str | None = None, use_liger_kernel: bool = False, liger_kernel_config: dict[str, bool] | None = None, use_cache: bool = False, neftune_noise_alpha: float | None = None, torch_empty_cache_steps: int | None = None, auto_find_batch_size: bool = False, logging_strategy: transformers.trainer_utils.IntervalStrategy | str = 'steps', logging_steps: float = 10, logging_first_step: bool = False, log_on_each_node: bool = True, logging_nan_inf_filter: bool = True, include_num_input_tokens_seen: str | bool = 'no', log_level: str = 'passive', log_level_replica: str = 'warning', disable_tqdm: bool | None = None, report_to: None | str | list[str] = 'none', run_name: str | None = None, project: str = 'huggingface', trackio_space_id: str | None = None, trackio_bucket_id: str | None = None, trackio_static_space_id: Union[str, NoneType, Literal[False]] = None, eval_strategy: transformers.trainer_utils.IntervalStrategy | str = 'no', eval_steps: float | None = None, eval_delay: float = 0, per_device_eval_batch_size: int = 8, prediction_loss_only: bool = False, eval_on_start: bool = False, eval_do_concat_batches: bool = True, eval_use_gather_object: bool = False, eval_accumulation_steps: int | None = None, include_for_metrics: list[str] = <factory>, batch_eval_metrics: bool = False, save_only_model: bool = False, save_strategy: transformers.trainer_utils.SaveStrategy | str = 'steps', save_steps: float = 500, save_on_each_node: bool = False, save_total_limit: int | None = None, enable_jit_checkpoint: bool = False, push_to_hub: bool = False, hub_token: str | None = None, hub_private_repo: bool | None = None, hub_model_id: str | None = None, hub_strategy: transformers.trainer_utils.HubStrategy | str = 'every_save', hub_always_push: bool = False, hub_revision: str | None = None, load_best_model_at_end: bool = False, metric_for_best_model: str | None = None, greater_is_better: bool | None = None, ignore_data_skip: bool = False, restore_callback_states_from_checkpoint: bool = False, full_determinism: bool = False, seed: int = 42, data_seed: int | None = None, use_cpu: bool = False, accelerator_config: dict | str | None = None, parallelism_config: accelerate.parallelism_config.ParallelismConfig | None = None, dataloader_drop_last: bool = False, dataloader_num_workers: int = 0, dataloader_pin_memory: bool = True, dataloader_persistent_workers: bool = False, dataloader_prefetch_factor: int | None = None, remove_unused_columns: bool | None = False, label_names: list[str] | None = None, train_sampling_strategy: str = 'random', length_column_name: str = 'length', ddp_find_unused_parameters: bool | None = None, ddp_bucket_cap_mb: int | None = None, ddp_broadcast_buffers: bool | None = None, ddp_static_graph: bool | None = None, ddp_backend: str | None = None, ddp_timeout: int = 1800, fsdp: str | None = None, fsdp_config: dict[str, typing.Any] | str | None = None, deepspeed: dict | str | None = None, debug: str | list[transformers.debug_utils.DebugOption] = '', skip_memory_metrics: bool = True, do_train: bool = False, do_eval: bool = False, do_predict: bool = False, resume_from_checkpoint: str | None = None, warmup_ratio: float | None = None, logging_dir: str | None = None, local_rank: int = -1, model_init_kwargs: dict[str, typing.Any] | str | None = None, trust_remote_code: bool = False, router_aux_loss_coef: float = 0.001, disable_dropout: bool = False, cast_lm_head_to_fp32: bool = False, num_generations: int | None = 8, num_generations_eval: int | None = None, max_completion_length: int | None = 256, ds3_gather_for_generation: bool = True, shuffle_dataset: bool | None = True, pad_to_multiple_of: int | None = None, generation_batch_size: int | None = None, steps_per_generation: int | None = None, temperature: float = 1.0, top_p: float = 1.0, top_k: int = 0, min_p: float | None = None, generation_kwargs: dict | None = None, chat_template_kwargs: dict | None = None, repetition_penalty: float = 1.0, cache_implementation: str | None = None, use_vllm: bool = False, vllm_mode: str = 'colocate', vllm_model_impl: str = 'vllm', vllm_enable_sleep_mode: bool = False, vllm_structured_outputs_regex: str | None = None, vllm_server_base_url: str | None = None, vllm_server_host: str = '0.0.0.0', vllm_server_port: int = 8000, vllm_server_timeout: float = 240.0, vllm_group_port: int = 51216, vllm_gpu_memory_utilization: float = 0.3, vllm_max_model_length: int | None = None, vllm_tensor_parallel_size: int = 1, beta: float = 0.0, num_iterations: int = 1, epsilon: float = 0.2, delta: float | None = None, epsilon_high: float | None = None, sapo_temperature_neg: float = 1.05, sapo_temperature_pos: float = 1.0, vespo_k_pos: float = 2.0, vespo_lambda_pos: float = 3.0, vespo_k_neg: float = 3.0, vespo_lambda_neg: float = 2.0, importance_sampling_level: str = 'token', reward_weights: list[float] | None = None, multi_objective_aggregation: str = 'sum_then_normalize', scale_rewards: str = 'group', loss_type: str = 'dapo', mask_truncated_completions: bool = False, sync_ref_model: bool = False, ref_model_mixup_alpha: float = 0.6, ref_model_sync_steps: int = 512, top_entropy_quantile: float = 1.0, max_tool_calling_iterations: int | None = None, vllm_importance_sampling_correction: bool = True, vllm_importance_sampling_mode: str = 'sequence_mask', vllm_importance_sampling_clip_max: float | None = 3.0, vllm_importance_sampling_clip_min: float | None = None, off_policy_mask_threshold: float | None = None, use_bias_correction_kl: bool = False, log_completions: bool = False, num_completions_to_print: int | None = None, log_unique_prompts: bool = False, log_completions_hub_repo: str | None = None, use_transformers_continuous_batching: bool = False, transformers_continuous_batching_config: dict | None = None, use_transformers_paged: bool = False, vllm_importance_sampling_cap: float | None = None) -> None



{}

## Cell 32 [code] execution_count=None
trainer.train()
OUTPUT 1: display_data

<IPython.core.display.HTML object>

    <div>
      
      <progress value='10' max='10' style='width:300px; height:20px; vertical-align: middle;'></progress>
      [10/10 00:53, Epoch 1/2]
    </div>
    <table border="1" class="dataframe">
  <thead>
 <tr style="text-align: left;">
      <th>Step</th>
      <th>Training Loss</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>-0.000000</td>
    </tr>
    <tr>
      <td>2</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <td>3</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <td>4</td>
      <td>0.299315</td>
    </tr>
    <tr>
      <td>5</td>
      <td>0.160381</td>
    </tr>
    <tr>
      <td>6</td>
      <td>-0.008093</td>
    </tr>
    <tr>
      <td>7</td>
      <td>0.028336</td>
    </tr>
    <tr>
      <td>8</td>
      <td>-0.000001</td>
    </tr>
    <tr>
      <td>9</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <td>10</td>
      <td>0.153412</td>
    </tr>
  </tbody>
</table><p>
{}
OUTPUT 2: execute_result

TrainOutput(global_step=10, training_loss=0.06333511250093551, metrics={'train_runtime': 65.4125, 'train_samples_per_second': 0.612, 'train_steps_per_second': 0.153, 'total_flos': 0.0, 'train_loss': 0.06333511250093551, 'epoch': 1.25})

{}

## Cell 33 [code] execution_count=None
trainer.save_model("grpo_output_final")
tokenizer.save_pretrained("grpo_output_final")
OUTPUT 1: execute_result

('grpo_output_final/tokenizer_config.json',
 'grpo_output_final/chat_template.jinja',
 'grpo_output_final/tokenizer.json')

{}

## Cell 34 [code] execution_count=None
base_model_id = "HuggingFaceTB/SmolLM-135M-Instruct"
adapter_path = "grpo_output_final"

tokenizer = AutoTokenizer.from_pretrained(adapter_path)

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

base_model = AutoModelForCausalLM.from_pretrained(
    base_model_id,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto",
)

model = PeftModel.from_pretrained(base_model, adapter_path)
model.eval()
OUTPUT 1: display_data

Loading weights:   0%|          | 0/272 [00:00<?, ?it/s]

{}
OUTPUT 2: execute_result

PeftModelForCausalLM(
  (base_model): LoraModel(
    (model): LlamaForCausalLM(
      (model): LlamaModel(
        (embed_tokens): Embedding(49152, 576, padding_idx=2)
        (layers): ModuleList(
          (0-29): 30 x LlamaDecoderLayer(
            (self_attn): LlamaAttention(
              (q_proj): lora.Linear(
                (base_layer): Linear(in_features=576, out_features=576, bias=False)
                (lora_dropout): ModuleDict(
                  (default): Dropout(p=0.05, inplace=False)
                )
                (lora_A): ModuleDict(
                  (default): Linear(in_features=576, out_features=8, bias=False)
                )
                (lora_B): ModuleDict(
                  (default): Linear(in_features=8, out_features=576, bias=False)
                )
                (lora_embedding_A): ParameterDict()
                (lora_embedding_B): ParameterDict()
                (lora_magnitude_vector): ModuleDict()
              )
              (k_proj): Linear(in_features=576, out_features=192, bias=False)
              (v_proj): lora.Linear(
                (base_layer): Linear(in_features=576, out_features=192, bias=False)
                (lora_dropout): ModuleDict(
                  (default): Dropout(p=0.05, inplace=False)
                )
                (lora_A): ModuleDict(
                  (default): Linear(in_features=576, out_features=8, bias=False)
                )
                (lora_B): ModuleDict(
                  (default): Linear(in_features=8, out_features=192, bias=False)
                )
                (lora_embedding_A): ParameterDict()
                (lora_embedding_B): ParameterDict()
                (lora_magnitude_vector): ModuleDict()
              )
              (o_proj): Linear(in_features=576, out_features=576, bias=False)
            )
            (mlp): LlamaMLP(
              (gate_proj): Linear(in_features=576, out_features=1536, bias=False)
              (up_proj): Linear(in_features=576, out_features=1536, bias=False)
              (down_proj): Linear(in_features=1536, out_features=576, bias=False)
              (act_fn): SiLUActivation()
            )
            (input_layernorm): LlamaRMSNorm((576,), eps=1e-05)
            (post_attention_layernorm): LlamaRMSNorm((576,), eps=1e-05)
          )
        )
        (norm): LlamaRMSNorm((576,), eps=1e-05)
        (rotary_emb): LlamaRotaryEmbedding()
      )
      (lm_head): Linear(in_features=576, out_features=49152, bias=False)
    )
  )
)

{}

## Cell 35 [code] execution_count=None
def generate_answer(question, max_new_tokens=100):
    prompt = f"Question: {question}\nAnswer in simple English:"

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            pad_token_id=tokenizer.eos_token_id,
        )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

## Cell 36 [code] execution_count=None
print(generate_answer("Explain AI in simple terms."))
OUTPUT 1: stream
Question: Explain AI in simple terms.
Answer in simple English:

**What is Artificial Intelligence (AI)?**

Artificial Intelligence, or AI, refers to the development of computer systems that can perform tasks that typically require human intelligence, such as:

1. **Learning**: AI systems can learn from data, improve their performance over time, and adapt to new situations.
2. **Reasoning**: AI systems can make decisions, solve problems, and draw conclusions based on data and rules.
3. **Perception**: AI systems can interpret



{}

## Cell 37 [markdown] execution_count=None
## GRPO with unsloth

## Cell 38 [code] execution_count=None
!pip install -U unsloth vllm
!pip install -U transformers datasets trl accelerate peft bitsandbytes

## Cell 39 [code] execution_count=None
from unsloth import FastLanguageModel
import torch

max_seq_length = 1024
lora_rank = 16

MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name=MODEL_NAME,
    max_seq_length=max_seq_length,
    load_in_4bit=True,
    fast_inference=True,
    max_lora_rank=lora_rank,
    gpu_memory_utilization=0.6,
)

## Cell 40 [code] execution_count=None
model = FastLanguageModel.get_peft_model(
    model,
    r=lora_rank,
    target_modules=[
        "q_proj", "k_proj", "v_proj", "o_proj",
        "gate_proj", "up_proj", "down_proj",
    ],
    lora_alpha=lora_rank,
    use_gradient_checkpointing="unsloth",
    random_state=3407,
)

## Cell 41 [code] execution_count=None
SYSTEM_PROMPT = """
Respond in the following format:

<reasoning>
Write your step-by-step reasoning here.
</reasoning>
<answer>
Write only the final numeric answer here.
</answer>
"""

XML_COT_FORMAT = """\
<reasoning>
{reasoning}
</reasoning>
<answer>
{answer}
</answer>
"""

## Cell 42 [code] execution_count=None
import re
from datasets import load_dataset, Dataset

def extract_hash_answer(text: str):
    if "####" not in text:
        return None
    return text.split("####")[-1].strip()

def get_gsm8k_questions(split="train") -> Dataset:
    data = load_dataset("openai/gsm8k", "main")[split]

    data = data.map(
        lambda x: {
            "prompt": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": x["question"]},
            ],
            "answer": extract_hash_answer(x["answer"]),
        }
    )

    return data

dataset = get_gsm8k_questions("train")

print(dataset[0])

## Cell 43 [code] execution_count=None
def extract_xml_answer(text: str) -> str:
    if "<answer>" not in text:
        return ""
    answer = text.split("<answer>")[-1]
    answer = answer.split("</answer>")[0]
    return answer.strip()

## Cell 44 [code] execution_count=None
def correctness_reward_func(prompts, completions, answer, **kwargs) -> list[float]:
    responses = [completion[0]["content"] for completion in completions]
    extracted_responses = [extract_xml_answer(r) for r in responses]

    rewards = []
    for model_answer, gold_answer in zip(extracted_responses, answer):
        if model_answer == gold_answer:
            rewards.append(2.0)
        else:
            rewards.append(0.0)

    return rewards

## Cell 45 [code] execution_count=None
def int_reward_func(completions, **kwargs) -> list[float]:
    responses = [completion[0]["content"] for completion in completions]
    extracted_responses = [extract_xml_answer(r) for r in responses]

    return [0.5 if r.isdigit() else 0.0 for r in extracted_responses]

## Cell 46 [code] execution_count=None
def soft_format_reward_func(completions, **kwargs) -> list[float]:
    pattern = r"<reasoning>.*?</reasoning>\s*<answer>.*?</answer>"
    responses = [completion[0]["content"] for completion in completions]
    matches = [re.search(pattern, r, re.DOTALL) for r in responses]

    return [0.5 if match else 0.0 for match in matches]

## Cell 47 [code] execution_count=None
def strict_format_reward_func(completions, **kwargs) -> list[float]:
    pattern = r"^<reasoning>\n.*?\n</reasoning>\n<answer>\n.*?\n</answer>\n$"
    responses = [completion[0]["content"] for completion in completions]
    matches = [re.match(pattern, r, re.DOTALL) for r in responses]

    return [0.5 if match else 0.0 for match in matches]

## Cell 48 [code] execution_count=None
def count_xml(text) -> float:
    count = 0.0

    if text.count("<reasoning>\n") == 1:
        count += 0.125

    if text.count("\n</reasoning>\n") == 1:
        count += 0.125

    if text.count("\n<answer>\n") == 1:
        count += 0.125
        count -= len(text.split("\n</answer>\n")[-1]) * 0.001

    if text.count("\n</answer>") == 1:
        count += 0.125
        count -= (len(text.split("\n</answer>")[-1]) - 1) * 0.001

    return count

def xmlcount_reward_func(completions, **kwargs) -> list[float]:
    contents = [completion[0]["content"] for completion in completions]
    return [count_xml(c) for c in contents]

## Cell 49 [code] execution_count=None
from trl import GRPOConfig, GRPOTrainer

max_prompt_length = 256

training_args = GRPOConfig(
    learning_rate=5e-6,
    adam_beta1=0.9,
    adam_beta2=0.99,
    weight_decay=0.1,
    warmup_ratio=0.1,
    lr_scheduler_type="cosine",
    optim="paged_adamw_8bit",

    logging_steps=1,

    per_device_train_batch_size=1,
    gradient_accumulation_steps=1,

    num_generations=4,  # increase to 6 if GPU memory allows

    max_prompt_length=max_prompt_length,
    max_completion_length=max_seq_length - max_prompt_length,

    max_steps=100,       # demo; use 250+ for better result
    save_steps=100,

    max_grad_norm=0.1,
    report_to="none",
    output_dir="grpo_outputs",
)

## Cell 50 [code] execution_count=None
trainer = GRPOTrainer(
    model=model,
    processing_class=tokenizer,
    reward_funcs=[
        xmlcount_reward_func,
        soft_format_reward_func,
        strict_format_reward_func,
        int_reward_func,
        correctness_reward_func,
    ],
    args=training_args,
    train_dataset=dataset,
)

## Cell 51 [code] execution_count=None
trainer.train()

## Cell 52 [code] execution_count=None
model.save_lora("grpo_saved_lora")

## Cell 53 [code] execution_count=None
from vllm import SamplingParams

test_prompt = tokenizer.apply_chat_template(
    [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "If there are 3 boxes and each box has 4 apples, how many apples are there in total?"},
    ],
    tokenize=False,
    add_generation_prompt=True,
)

sampling_params = SamplingParams(
    temperature=0.7,
    top_p=0.95,
    max_tokens=512,
)

output = model.fast_generate(
    test_prompt,
    sampling_params=sampling_params,
    lora_request=model.load_lora("grpo_saved_lora"),
)[0].outputs[0].text

print(output)

## Cell 54 [code] execution_count=None
model.save_pretrained_merged(
    "grpo_merged_model",
    tokenizer,
    save_method="merged_16bit"
)