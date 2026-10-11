# DPO_Training_Final.ipynb
Metadata: {"accelerator": "GPU", "colab": {"gpuType": "T4", "provenance": []}, "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python", "version": "3.x"}, "widgets": {"application/vnd.jupyter.widget-state+json": {"version_major": 2, "version_minor": 0, "state": {"90c76f3fee6342349c8bcb7af5e96898": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_ec0bde568f2f4cdd91ee5a637f06e006", "IPY_MODEL_f7d98208532f40f583a2161f03a965cf", "IPY_MODEL_233699904b8042adab747beef3d14254"], "layout": "IPY_MODEL_9a578aa57dbd4c1fbb2db02b7f9d8fc4"}}, "ec0bde568f2f4cdd91ee5a637f06e006": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_c9a77160fad149f1abfe5f5ce7300b6d", "placeholder": "\u200b", "style": "IPY_MODEL_c81c901ed0d147ef977879c89ad34644", "value": "Map:\u2007100%"}}, "f7d98208532f40f583a2161f03a965cf": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_d7f588045dc54a5fa38378c059e1d69b", "max": 4, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_e9069d56a33546fd8a7cb4597ba99ec0", "value": 4}}, "233699904b8042adab747beef3d14254": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_8b45f7a88a38467f929bf4cb9030bb15", "placeholder": "\u200b", "style": "IPY_MODEL_73c4b203fe7d4e718aa3fa29f24eb308", "value": "\u20074/4\u2007[00:00&lt;00:00,\u2007239.44\u2007examples/s]"}}, "9a578aa57dbd4c1fbb2db02b7f9d8fc4": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "c9a77160fad149f1abfe5f5ce7300b6d": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "c81c901ed0d147ef977879c89ad34644": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "d7f588045dc54a5fa38378c059e1d69b": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "e9069d56a33546fd8a7cb4597ba99ec0": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "8b45f7a88a38467f929bf4cb9030bb15": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "73c4b203fe7d4e718aa3fa29f24eb308": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "c5ce2261c2ea44d98b934b4cec5a344a": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_dce3b5d036254caab256baef68ccd42c", "IPY_MODEL_09fb29da626d4d7192727ae7a3baac8a", "IPY_MODEL_3e3c09b012e54cc7bc82897945d29750"], "layout": "IPY_MODEL_63ba4f16d7174b7c850c300dd10de96c"}}, "dce3b5d036254caab256baef68ccd42c": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_cb6eb1a862f64de08f4faac2d3d12970", "placeholder": "\u200b", "style": "IPY_MODEL_b2c66212dada4a44a3b789b20d211a69", "value": "config.json:\u2007100%"}}, "09fb29da626d4d7192727ae7a3baac8a": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_624081eb4aa743018fa35a7132884618", "max": 659, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_bf0969a68d614948ba0e3e7004d16ec7", "value": 659}}, "3e3c09b012e54cc7bc82897945d29750": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_36a1d465f7d145e692b85248eb2d58dc", "placeholder": "\u200b", "style": "IPY_MODEL_ba9a49fda6bd46e780d2367b3054cb15", "value": "\u2007659/659\u2007[00:00&lt;00:00,\u200750.1kB/s]"}}, "63ba4f16d7174b7c850c300dd10de96c": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "cb6eb1a862f64de08f4faac2d3d12970": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "b2c66212dada4a44a3b789b20d211a69": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "624081eb4aa743018fa35a7132884618": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "bf0969a68d614948ba0e3e7004d16ec7": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "36a1d465f7d145e692b85248eb2d58dc": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "ba9a49fda6bd46e780d2367b3054cb15": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "3c6a578bbb17440b9df1ead2e12432b9": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_d26ce6d9bdea49c9930bea404837326e", "IPY_MODEL_9f0bd6060bd6472e8b6aa6221607fd8b", "IPY_MODEL_4c67933bebca4b3bbb5ebf3d0e5b12af"], "layout": "IPY_MODEL_ce936eebcb66477089e10aed1e4c0fde"}}, "d26ce6d9bdea49c9930bea404837326e": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_c5ab65bf951942978f5d8f79b35c1d75", "placeholder": "\u200b", "style": "IPY_MODEL_cf33121fe50d4a42ad2e97ea62e3592f", "value": "tokenizer_config.json:\u2007100%"}}, "9f0bd6060bd6472e8b6aa6221607fd8b": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_c27542f96df746168eb37086a8ce1d1b", "max": 7305, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_3e6759c5ff454bdda06064894e29bb0d", "value": 7305}}, "4c67933bebca4b3bbb5ebf3d0e5b12af": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_687322293a0243b6abbbf0b455603867", "placeholder": "\u200b", "style": "IPY_MODEL_d68f595eb35041f8b74b039cbbcccb45", "value": "\u20077.30k/7.30k\u2007[00:00&lt;00:00,\u2007665kB/s]"}}, "ce936eebcb66477089e10aed1e4c0fde": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "c5ab65bf951942978f5d8f79b35c1d75": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "cf33121fe50d4a42ad2e97ea62e3592f": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "c27542f96df746168eb37086a8ce1d1b": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "3e6759c5ff454bdda06064894e29bb0d": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "687322293a0243b6abbbf0b455603867": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "d68f595eb35041f8b74b039cbbcccb45": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "a2f6c35505c3415483c5807e34a7e96b": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_ceb9c8622c7146b0a243cd959fff0300", "IPY_MODEL_2958e59e3c464d08a7f5f45d257073e3", "IPY_MODEL_98c6f286049c42c89249ce6b54bd9d11"], "layout": "IPY_MODEL_82cd3cb701924f35b34a20e5af2f8155"}}, "ceb9c8622c7146b0a243cd959fff0300": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_4e2315c282a64683ab48773322de02d9", "placeholder": "\u200b", "style": "IPY_MODEL_029c0ab624ea468998216614de927bed", "value": "vocab.json:\u2007100%"}}, "2958e59e3c464d08a7f5f45d257073e3": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_5d4c71486fa94a4989ee347015c0178f", "max": 2776833, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_b0ff9a1f01a541eb92d6e50e14933e62", "value": 2776833}}, "98c6f286049c42c89249ce6b54bd9d11": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_ec55e5947c3947a98ed462d809e28a69", "placeholder": "\u200b", "style": "IPY_MODEL_b6a51939e0aa434cb56417219c7f08d4", "value": "\u20072.78M/2.78M\u2007[00:00&lt;00:00,\u200715.2MB/s]"}}, "82cd3cb701924f35b34a20e5af2f8155": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "4e2315c282a64683ab48773322de02d9": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "029c0ab624ea468998216614de927bed": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "5d4c71486fa94a4989ee347015c0178f": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "b0ff9a1f01a541eb92d6e50e14933e62": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "ec55e5947c3947a98ed462d809e28a69": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "b6a51939e0aa434cb56417219c7f08d4": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "796857b66bb44ce7bced5ebb0aec5e47": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_a7fbb63192dc4bae9d6bd961f2c68ba7", "IPY_MODEL_0fd755cf87dc47c894bfffaf03abf258", "IPY_MODEL_3765798dcc6c46489440fe68214cf0b9"], "layout": "IPY_MODEL_9a40fc274585413cacdd2d0116e357b1"}}, "a7fbb63192dc4bae9d6bd961f2c68ba7": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_e335143bf7b340e7a0389ac43ac78952", "placeholder": "\u200b", "style": "IPY_MODEL_bd3984f6f1c04194b3088eed6d66863f", "value": "merges.txt:\u2007100%"}}, "0fd755cf87dc47c894bfffaf03abf258": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_7115a39ac9bc472cb27d4563ec7b6bac", "max": 1671839, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_9fbac26e663b4a64bc08b12632a72d02", "value": 1671839}}, "3765798dcc6c46489440fe68214cf0b9": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_dbf555e9441942099ac9ee5b39a0e0ae", "placeholder": "\u200b", "style": "IPY_MODEL_71fc0e70360f442fa4d4c6c0827e4045", "value": "\u20071.67M/1.67M\u2007[00:00&lt;00:00,\u20072.33MB/s]"}}, "9a40fc274585413cacdd2d0116e357b1": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "e335143bf7b340e7a0389ac43ac78952": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "bd3984f6f1c04194b3088eed6d66863f": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "7115a39ac9bc472cb27d4563ec7b6bac": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "9fbac26e663b4a64bc08b12632a72d02": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "dbf555e9441942099ac9ee5b39a0e0ae": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "71fc0e70360f442fa4d4c6c0827e4045": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "cec29b9929fc4c3dbb92a94219e2f2ef": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_e7e1e7b55750492a8d462cb0e976704e", "IPY_MODEL_51c06973eb50489383284da431a1c907", "IPY_MODEL_f011608ad04b4086a5360a2dae3a4fd0"], "layout": "IPY_MODEL_c10eb3a21c7a45dbba410263d737745b"}}, "e7e1e7b55750492a8d462cb0e976704e": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_8fa87d379c9f49f8a4dd5ee2eabd6fc8", "placeholder": "\u200b", "style": "IPY_MODEL_f7d59d5e2cd34d0db4e14ed48533ff0f", "value": "tokenizer.json:\u2007100%"}}, "51c06973eb50489383284da431a1c907": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_c96e65e478c846b980987652fb0810f7", "max": 7031645, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_9659b79a3b06429090264fd01d648603", "value": 7031645}}, "f011608ad04b4086a5360a2dae3a4fd0": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_ddf5d5e4136843e8b82f50f01b184aaf", "placeholder": "\u200b", "style": "IPY_MODEL_c60ba7e44bca486e85f9ee99d580c7dd", "value": "\u20077.03M/7.03M\u2007[00:00&lt;00:00,\u200720.7MB/s]"}}, "c10eb3a21c7a45dbba410263d737745b": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "8fa87d379c9f49f8a4dd5ee2eabd6fc8": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "f7d59d5e2cd34d0db4e14ed48533ff0f": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "c96e65e478c846b980987652fb0810f7": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "9659b79a3b06429090264fd01d648603": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "ddf5d5e4136843e8b82f50f01b184aaf": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "c60ba7e44bca486e85f9ee99d580c7dd": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "a053d9532a6649a1acbaa1a2b449b8d4": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_c113c31e169042a086d7e7d75c699157", "IPY_MODEL_6c11903af73346a29c72a1b1d3101f0c", "IPY_MODEL_85446fb54c644547945a5b88a1577a34"], "layout": "IPY_MODEL_4aebb2f7aef94bd692c3c31ce449f563"}}, "c113c31e169042a086d7e7d75c699157": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_b1f33cac36f94e76927984b5341e1e08", "placeholder": "\u200b", "style": "IPY_MODEL_c87c551a818946fc8c3b2475625005ed", "value": "model.safetensors:\u2007reconstructing\u2007file:\u2007100%"}}, "6c11903af73346a29c72a1b1d3101f0c": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_6bab5fa645fc4516a75350359d21e253", "max": 988097824, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_b21613a037a44958805a65b8552ae197", "value": 988097824}}, "85446fb54c644547945a5b88a1577a34": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_34533212d0ab4a19b6e1ed5a31b6f7ec", "placeholder": "\u200b", "style": "IPY_MODEL_154bd024982c4728897d5e01fdc77fb3", "value": "\u2007\u2007988MB\u2007/\u2007\u2007988MB,\u200768.9MB/s\u2007\u2007"}}, "4aebb2f7aef94bd692c3c31ce449f563": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "b1f33cac36f94e76927984b5341e1e08": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "c87c551a818946fc8c3b2475625005ed": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "6bab5fa645fc4516a75350359d21e253": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "b21613a037a44958805a65b8552ae197": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "34533212d0ab4a19b6e1ed5a31b6f7ec": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "154bd024982c4728897d5e01fdc77fb3": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "cdf0e42ecfad4162870f3a23b7845f37": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_ca8a8aceb5cf4b2594b03be74da960be", "IPY_MODEL_790c71a110b8486bbf5f72c9a5b99f59", "IPY_MODEL_5544d9c7b80448b592f6811a23474c63"], "layout": "IPY_MODEL_c222dc5854e34d73813b259d715e635f"}}, "ca8a8aceb5cf4b2594b03be74da960be": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_a1d646f17ae0408c821b507868df90a9", "placeholder": "\u200b", "style": "IPY_MODEL_36f164387e4e403e984fa99f96a7188e", "value": "model.safetensors:\u2007downloading\u2007bytes:\u2007"}}, "790c71a110b8486bbf5f72c9a5b99f59": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_83beedc0c2224a4db8e491c46cb3d5f1", "max": 988097824, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_e845bc29e10841f3a3c7b02f1169c188", "value": 854045206}}, "5544d9c7b80448b592f6811a23474c63": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_30fbf6bc4ef14efba0bf49e5c45836a6", "placeholder": "\u200b", "style": "IPY_MODEL_f0feaaec4fae46c99de494780deb8bc4", "value": "\u2007\u2007854MB,\u200768.6MB/s\u2007\u2007"}}, "c222dc5854e34d73813b259d715e635f": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "a1d646f17ae0408c821b507868df90a9": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "36f164387e4e403e984fa99f96a7188e": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "83beedc0c2224a4db8e491c46cb3d5f1": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "e845bc29e10841f3a3c7b02f1169c188": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "30fbf6bc4ef14efba0bf49e5c45836a6": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "f0feaaec4fae46c99de494780deb8bc4": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "0e0fd249c0df49a2b6f02491f73c6588": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_078244e70588488f822f20460c2710c5", "IPY_MODEL_1373dce0bafe4b0cb785b1469970e95f", "IPY_MODEL_f550ae471fd04eb3bb37cb3ce7e1891d"], "layout": "IPY_MODEL_49be25bd3cf144f6926c9d1b9605fc99"}}, "078244e70588488f822f20460c2710c5": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_44501e34eff9466582b54a683e8f473e", "placeholder": "\u200b", "style": "IPY_MODEL_c3b651140a78490ca26b4e8f180cacbd", "value": "Loading\u2007weights:\u2007100%"}}, "1373dce0bafe4b0cb785b1469970e95f": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_48a05b712f9848aaaa83898b6e71065f", "max": 290, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_b5b43f89bda1470281e9bacd30bbb9a0", "value": 290}}, "f550ae471fd04eb3bb37cb3ce7e1891d": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_814a8b8edc0843d1a4de575d546940e1", "placeholder": "\u200b", "style": "IPY_MODEL_33fff5eb573a435d82302618ebff90e6", "value": "\u2007290/290\u2007[00:00&lt;00:00,\u2007589.58it/s]"}}, "49be25bd3cf144f6926c9d1b9605fc99": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "44501e34eff9466582b54a683e8f473e": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "c3b651140a78490ca26b4e8f180cacbd": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "48a05b712f9848aaaa83898b6e71065f": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "b5b43f89bda1470281e9bacd30bbb9a0": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "814a8b8edc0843d1a4de575d546940e1": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "33fff5eb573a435d82302618ebff90e6": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "f78929da7e4f49589f63d683c50f935e": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_31e332f0978840e580e7291c0102e281", "IPY_MODEL_9bb8a3eefdd04963bbeca73fd39e6100", "IPY_MODEL_d640e7adaa214af4a4e2e588e4cdbf92"], "layout": "IPY_MODEL_2c6f18fb54a5459696fba14e78ef10c3"}}, "31e332f0978840e580e7291c0102e281": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_bf13f44e2f1b4ebaa3ae531c7d3ca6e3", "placeholder": "\u200b", "style": "IPY_MODEL_4342675615104f57a89e5691127fb341", "value": "generation_config.json:\u2007100%"}}, "9bb8a3eefdd04963bbeca73fd39e6100": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_168d53e0b46e45ff909d146108105965", "max": 242, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_93c1af86526a4d92b36d9864fa755d41", "value": 242}}, "d640e7adaa214af4a4e2e588e4cdbf92": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_28909c3db02b4db4acffe5d0bd505369", "placeholder": "\u200b", "style": "IPY_MODEL_ab4174c0ec1c45e8bdcec6c2da3a6e59", "value": "\u2007242/242\u2007[00:00&lt;00:00,\u200721.2kB/s]"}}, "2c6f18fb54a5459696fba14e78ef10c3": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "bf13f44e2f1b4ebaa3ae531c7d3ca6e3": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "4342675615104f57a89e5691127fb341": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "168d53e0b46e45ff909d146108105965": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "93c1af86526a4d92b36d9864fa755d41": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "28909c3db02b4db4acffe5d0bd505369": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "ab4174c0ec1c45e8bdcec6c2da3a6e59": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "942a26a4f2524fd4ad6442a6926814d1": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_75ce853586334a12a53199a42eec54ce", "IPY_MODEL_693a2ac9883a442baf8366ea14fc2dca", "IPY_MODEL_c09e23a6872c4d5e833211d9d061c8b0"], "layout": "IPY_MODEL_8e6fd43a098c43509ffa2a735b04f932"}}, "75ce853586334a12a53199a42eec54ce": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_7cf8be7208dc461fb63a89bc26825d17", "placeholder": "\u200b", "style": "IPY_MODEL_814dcabdb20e4da7bd53a714acc5258a", "value": "Tokenizing\u2007train\u2007dataset:\u2007100%"}}, "693a2ac9883a442baf8366ea14fc2dca": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_3ed4143d95ee456291e0a4c3b86ec5fe", "max": 3, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_a0a0da6cf9dd47178b8cd544479e021b", "value": 3}}, "c09e23a6872c4d5e833211d9d061c8b0": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_777f873f6cb44e87a45453c82b31b7a0", "placeholder": "\u200b", "style": "IPY_MODEL_2924b9d71c8e4697916f0fd0c97fea10", "value": "\u20073/3\u2007[00:00&lt;00:00,\u200754.41\u2007examples/s]"}}, "8e6fd43a098c43509ffa2a735b04f932": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "7cf8be7208dc461fb63a89bc26825d17": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "814dcabdb20e4da7bd53a714acc5258a": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "3ed4143d95ee456291e0a4c3b86ec5fe": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "a0a0da6cf9dd47178b8cd544479e021b": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "777f873f6cb44e87a45453c82b31b7a0": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "2924b9d71c8e4697916f0fd0c97fea10": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "690d1f4d2b284cee846caf28aa59a5ea": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_23960be2662a4fd1be0cf2754c151824", "IPY_MODEL_e611761b0d3e4f0d9d6b2be7ba1ada03", "IPY_MODEL_de2fe220a0be48aea510473b97a5b04b"], "layout": "IPY_MODEL_3105ef7036c5471f9c6e9c5593536447"}}, "23960be2662a4fd1be0cf2754c151824": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_cfa100663a9346cab9fae9ebaddbcd2c", "placeholder": "\u200b", "style": "IPY_MODEL_930aa8ffb04b4fd48d8192cfbd9ef01d", "value": "Dropping\u2007fully\u2007truncated\u2007examples\u2007from\u2007train\u2007dataset:\u2007100%"}}, "e611761b0d3e4f0d9d6b2be7ba1ada03": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_6048889486154f8db9dccb5c69f5496c", "max": 3, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_b698c8a857ff48b29a6f8ac74a584b26", "value": 3}}, "de2fe220a0be48aea510473b97a5b04b": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_1fc1d04b3296493b98ec04b0aac55a16", "placeholder": "\u200b", "style": "IPY_MODEL_b643569c4d5343b58e422315c984943a", "value": "\u20073/3\u2007[00:00&lt;00:00,\u2007130.39\u2007examples/s]"}}, "3105ef7036c5471f9c6e9c5593536447": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "cfa100663a9346cab9fae9ebaddbcd2c": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "930aa8ffb04b4fd48d8192cfbd9ef01d": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "6048889486154f8db9dccb5c69f5496c": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "b698c8a857ff48b29a6f8ac74a584b26": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "1fc1d04b3296493b98ec04b0aac55a16": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "b643569c4d5343b58e422315c984943a": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "c376293cbda6488eaa8175b0ee35ac52": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_3280301d89e847e4a250ded488acb729", "IPY_MODEL_ca889d38ea954aac881efe996feed971", "IPY_MODEL_090cc0acbd61463595d9cf341c50bd2b"], "layout": "IPY_MODEL_0048806bd5194f71a2c80bfa63672ee6"}}, "3280301d89e847e4a250ded488acb729": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_1c6987eafec94a898a7c6beabf4cf2c5", "placeholder": "\u200b", "style": "IPY_MODEL_1d49dbbbd8de4dc6b467b995506054fd", "value": "Tokenizing\u2007eval\u2007dataset:\u2007100%"}}, "ca889d38ea954aac881efe996feed971": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_1183c747e9204f9c9e539349bf05efcc", "max": 1, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_3060654ec45247f6b2984d83ab1e1906", "value": 1}}, "090cc0acbd61463595d9cf341c50bd2b": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_1e31c1e6ab0646328ec88eb2ba29a585", "placeholder": "\u200b", "style": "IPY_MODEL_cea1d9b737784a20bef9ab59c7f49237", "value": "\u20071/1\u2007[00:00&lt;00:00,\u200736.64\u2007examples/s]"}}, "0048806bd5194f71a2c80bfa63672ee6": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "1c6987eafec94a898a7c6beabf4cf2c5": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "1d49dbbbd8de4dc6b467b995506054fd": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "1183c747e9204f9c9e539349bf05efcc": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "3060654ec45247f6b2984d83ab1e1906": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "1e31c1e6ab0646328ec88eb2ba29a585": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "cea1d9b737784a20bef9ab59c7f49237": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "f6094d6f4b1c43618ee67cf45ec8a8f8": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_400b728e44904e10a1f0ffcd55c427d8", "IPY_MODEL_891634815f014022a5c89573e1dd26a0", "IPY_MODEL_16eb5976f7c9424f8b0b5e8dc3429909"], "layout": "IPY_MODEL_d7267885f7604207bc00eaa018f002cc"}}, "400b728e44904e10a1f0ffcd55c427d8": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_250e762762bf4ff0ba4f6b56b0219157", "placeholder": "\u200b", "style": "IPY_MODEL_f5222f6b82ba453a9693bba5308149f3", "value": "Dropping\u2007fully\u2007truncated\u2007examples\u2007from\u2007eval\u2007dataset:\u2007100%"}}, "891634815f014022a5c89573e1dd26a0": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_cc249a64310d499a97bfc6588af68e9b", "max": 1, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_10e8ed147628450dbccd47a40eb64671", "value": 1}}, "16eb5976f7c9424f8b0b5e8dc3429909": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_82dd641b526a446ebd82b7d3488db9cb", "placeholder": "\u200b", "style": "IPY_MODEL_6e2a8e69a4364620aa637ba5acc3d25b", "value": "\u20071/1\u2007[00:00&lt;00:00,\u200761.16\u2007examples/s]"}}, "d7267885f7604207bc00eaa018f002cc": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "250e762762bf4ff0ba4f6b56b0219157": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "f5222f6b82ba453a9693bba5308149f3": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "cc249a64310d499a97bfc6588af68e9b": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "10e8ed147628450dbccd47a40eb64671": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "82dd641b526a446ebd82b7d3488db9cb": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "6e2a8e69a4364620aa637ba5acc3d25b": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "9456bca59c6046a8bd1e506fc2872154": {"model_module": "@jupyter-widgets/controls", "model_name": "HBoxModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HBoxModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HBoxView", "box_style": "", "children": ["IPY_MODEL_269d0142c9104d60a7ea00021aa1bd1e", "IPY_MODEL_dffc083e20c14828b9d51f1e38ef6d24", "IPY_MODEL_aa2fc301623c4dffb674fcdd9ae4948b"], "layout": "IPY_MODEL_054583a0639d4e0ca40b3147bd855823"}}, "269d0142c9104d60a7ea00021aa1bd1e": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_3abd6bd0b48b4e3c94c92375c38fda7b", "placeholder": "\u200b", "style": "IPY_MODEL_e54c6b7b84a94a9a963eb55cb9ae09c2", "value": "Loading\u2007weights:\u2007100%"}}, "dffc083e20c14828b9d51f1e38ef6d24": {"model_module": "@jupyter-widgets/controls", "model_name": "FloatProgressModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "FloatProgressModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "ProgressView", "bar_style": "success", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_9b6826e933fb4b8393b0f9ac7503e931", "max": 290, "min": 0, "orientation": "horizontal", "style": "IPY_MODEL_89de0ff4594d4ba493ee2d6f06a5393e", "value": 290}}, "aa2fc301623c4dffb674fcdd9ae4948b": {"model_module": "@jupyter-widgets/controls", "model_name": "HTMLModel", "model_module_version": "1.5.0", "state": {"_dom_classes": [], "_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "HTMLModel", "_view_count": null, "_view_module": "@jupyter-widgets/controls", "_view_module_version": "1.5.0", "_view_name": "HTMLView", "description": "", "description_tooltip": null, "layout": "IPY_MODEL_b650992b3a464105aa58ec8e490a965a", "placeholder": "\u200b", "style": "IPY_MODEL_4bc88ef1b87f421c8658bb7876288c00", "value": "\u2007290/290\u2007[00:00&lt;00:00,\u2007681.97it/s]"}}, "054583a0639d4e0ca40b3147bd855823": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "3abd6bd0b48b4e3c94c92375c38fda7b": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "e54c6b7b84a94a9a963eb55cb9ae09c2": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}, "9b6826e933fb4b8393b0f9ac7503e931": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "89de0ff4594d4ba493ee2d6f06a5393e": {"model_module": "@jupyter-widgets/controls", "model_name": "ProgressStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "ProgressStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "bar_color": null, "description_width": ""}}, "b650992b3a464105aa58ec8e490a965a": {"model_module": "@jupyter-widgets/base", "model_name": "LayoutModel", "model_module_version": "1.2.0", "state": {"_model_module": "@jupyter-widgets/base", "_model_module_version": "1.2.0", "_model_name": "LayoutModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "LayoutView", "align_content": null, "align_items": null, "align_self": null, "border": null, "bottom": null, "display": null, "flex": null, "flex_flow": null, "grid_area": null, "grid_auto_columns": null, "grid_auto_flow": null, "grid_auto_rows": null, "grid_column": null, "grid_gap": null, "grid_row": null, "grid_template_areas": null, "grid_template_columns": null, "grid_template_rows": null, "height": null, "justify_content": null, "justify_items": null, "left": null, "margin": null, "max_height": null, "max_width": null, "min_height": null, "min_width": null, "object_fit": null, "object_position": null, "order": null, "overflow": null, "overflow_x": null, "overflow_y": null, "padding": null, "right": null, "top": null, "visibility": null, "width": null}}, "4bc88ef1b87f421c8658bb7876288c00": {"model_module": "@jupyter-widgets/controls", "model_name": "DescriptionStyleModel", "model_module_version": "1.5.0", "state": {"_model_module": "@jupyter-widgets/controls", "_model_module_version": "1.5.0", "_model_name": "DescriptionStyleModel", "_view_count": null, "_view_module": "@jupyter-widgets/base", "_view_module_version": "1.2.0", "_view_name": "StyleView", "description_width": ""}}}}}}

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
[?25l   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m0.0/11.6 MB[0m [31m?[0m eta [36m-:--:--[0m[2K   [91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m[90m╺[0m[90m━━━━━━━━━━━[0m [32m8.2/11.6 MB[0m [31m247.4 MB/s[0m eta [36m0:00:01[0m[2K   [91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m[91m╸[0m [32m11.6/11.6 MB[0m [31m276.6 MB/s[0m eta [36m0:00:01[0m[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m11.6/11.6 MB[0m [31m127.4 MB/s[0m eta [36m0:00:00[0m
[?25h[?25l   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m0.0/559.1 kB[0m [31m?[0m eta [36m-:--:--[0m[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m559.1/559.1 kB[0m [31m47.2 MB/s[0m eta [36m0:00:00[0m
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m889.0/889.0 kB[0m [31m66.1 MB/s[0m eta [36m0:00:00[0m
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m775.8/775.8 kB[0m [31m61.1 MB/s[0m eta [36m0:00:00[0m
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m40.9/40.9 MB[0m [31m19.8 MB/s[0m eta [36m0:00:00[0m
[2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m50.1/50.1 MB[0m [31m19.9 MB/s[0m eta [36m0:00:00[0m
[?25h


{}

## Cell 5 [markdown] execution_count=None
> After the installation cell finishes, restart the Colab runtime once if Colab asks you to do so. Then continue from the imports cell.

## Cell 6 [markdown] execution_count=None
## 2. Imports and reproducibility

## Cell 7 [code] execution_count=5
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
Datasets: 5.0.1
TRL: 1.9.2
PEFT: 0.20.0



{}

## Cell 8 [markdown] execution_count=None
## 3. Configuration

## Cell 9 [code] execution_count=6
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

## Cell 11 [code] execution_count=7
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

## Cell 13 [code] execution_count=8
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

## Cell 15 [code] execution_count=9
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

## Cell 17 [code] execution_count=10
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

## Cell 19 [code] execution_count=11
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

## Cell 21 [code] execution_count=12
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
LoraConfig(task_type='CAUSAL_LM', peft_type=<PeftType.LORA: 'LORA'>, auto_mapping=None, peft_version='0.20.0', base_model_name_or_path=None, revision=None, inference_mode=False, r=16, target_modules='all-linear', exclude_modules=None, lora_alpha=32, lora_dropout=0.05, fan_in_fan_out=False, bias='none', use_rslora=False, modules_to_save=None, init_lora_weights=True, layers_to_transform=None, layers_pattern=None, rank_pattern={}, alpha_pattern={}, megatron_config=None, megatron_core='megatron.core', trainable_token_indices=None, loftq_config={}, eva_config=None, corda_config=None, lora_ga_config=None, use_dora=False, velora_config=None, alora_invocation_tokens=None, use_qalora=False, qalora_group_size=16, monteclora_config=None, layer_replication=None, runtime_config=LoraRuntimeConfig(ephemeral_gpu_offload=False), lora_bias=False, target_parameters=None, use_bdlora=None, arrow_config=None, ensure_weight_tying=False)



{}

## Cell 22 [markdown] execution_count=None
## 10. Configure DPO training

## Cell 23 [code] execution_count=13
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

## Cell 25 [code] execution_count=14
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
OUTPUT 4: display_data

generation_config.json:   0%|          | 0.00/242 [00:00<?, ?B/s]

{}
OUTPUT 5: display_data

Tokenizing train dataset:   0%|          | 0/3 [00:00<?, ? examples/s]

{}
OUTPUT 6: display_data

Dropping fully truncated examples from train dataset:   0%|          | 0/3 [00:00<?, ? examples/s]

{}
OUTPUT 7: display_data

Tokenizing eval dataset:   0%|          | 0/1 [00:00<?, ? examples/s]

{}
OUTPUT 8: display_data

Dropping fully truncated examples from eval dataset:   0%|          | 0/1 [00:00<?, ? examples/s]

{}
OUTPUT 9: stream
trainable params: 8,798,208 || all params: 502,830,976 || trainable%: 1.7497



{}

## Cell 26 [markdown] execution_count=None
## 12. Evaluate before training

## Cell 27 [code] execution_count=15
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

## Cell 29 [code] execution_count=16
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
      [40/40 01:18, Epoch 40/40]
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

## Cell 31 [code] execution_count=18
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

## Cell 33 [code] execution_count=19
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
46       NaN        NaN            NaN       NaN         NaN            NaN   

    logits/rejected  mean_token_accuracy  rewards/chosen  rewards/rejected  \
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
46              NaN                  NaN             NaN               NaN   

    ...  eval_rewards/rejected  eval_rewards/accuracies  eval_rewards/margins  \
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
46  ...              -2.335294                      1.0              1.606812   

    eval_logps/chosen  eval_logps/rejected  train_runtime  \
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
44                NaN                  NaN        81.1224   
45         -58.487411           -77.313301            NaN   
46         -58.487411           -77.313301            NaN   

    train_samples_per_second  train_steps_per_second    total_flos  train_loss  
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
44                     3.945                   0.493  3.203459e+13    0.077171  
45                       NaN                     NaN           NaN         NaN  
46                       NaN                     NaN           NaN         NaN  

[20 rows x 37 columns]

  <div id="df-3894d5ac-bf62-47bd-a788-dd8ccd60f29a" class="colab-df-container">
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
      <td>81.1224</td>
      <td>3.945</td>
      <td>0.493</td>
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
    <tr>
      <th>46</th>
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
    <button class="colab-df-convert" onclick="convertToInteractive('df-3894d5ac-bf62-47bd-a788-dd8ccd60f29a')"
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
        document.querySelector('#df-3894d5ac-bf62-47bd-a788-dd8ccd60f29a button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-3894d5ac-bf62-47bd-a788-dd8ccd60f29a');
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

## Cell 35 [code] execution_count=20
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

## Cell 37 [code] execution_count=21
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

## Cell 39 [code] execution_count=22
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
DPO adapter loaded successfully.



{}

## Cell 40 [markdown] execution_count=None
## 19. Generate a response

## Cell 41 [code] execution_count=23
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
Prompt:
Explain overfitting in machine learning in simple words.

DPO response:
Overfitting happens when your model memorizes the data too much and learns patterns that it hasn't seen during training. It's like if you try to draw a picture of a cat using only one drawing paper instead of multiple ones - you'll end up drawing a bunch of cats instead of just one perfect one. Overfitting makes predictions that don't generalize well to new data.



{}

## Cell 42 [markdown] execution_count=None
## 20. Test several prompts

## Cell 43 [code] execution_count=24
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
RESPONSE: Machine learning is like teaching computers to learn patterns from data and make predictions or decisions based on that learning. It's used to help computers solve problems without being explicitly programmed for each task.
================================================================================
PROMPT: What is overfitting?
RESPONSE: Overfitting occurs when a model memorizes the training data too closely and performs poorly on new unseen data. It happens because the model has learned to fit the training data too closely, rather than generalizing well to new examples.
================================================================================
PROMPT: How are classification and regression different?
RESPONSE: Classification predicts categorical labels or categories, while regression predicts continuous numerical values. 

For example, predicting whether a customer will churn (a category) from their past behavior is classified, such as churn prediction.

On the other hand, predicting how many units of product to order based on historical sales data is regression. 

Both tasks involve making predictions using statistical models that can learn patterns in large datasets. However, they differ in terms of the target variable and the methods used for prediction.
================================================================================
PROMPT: What does a loss function do?
RESPONSE: A loss function is a mathematical function used to evaluate the performance of a model and quantify its errors or predictions. It is commonly used in training neural networks and other models for optimization purposes.
In the context of supervised learning, a loss function measures the difference between the predicted output and the actual target values. It is typically represented as a scalar value that ranges from -1 (negative) to 1 (positive), where 0 indicates perfect prediction.
The goal of training a model with a loss function is to minimize this loss over all training examples, so that the model's predictions are as close as possible to the ground truth labels while minimizing the overall error.
There are several types of loss functions, including cross-entropy, mean squared error, and categorical



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