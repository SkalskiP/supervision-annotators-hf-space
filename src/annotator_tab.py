import os

import gradio as gr
from gradio import ColorPicker

from src.annotators.annotators import annotator


def annotator_tab(gr: gr):
    with gr.Tab("Image Annotator(YoloV8)"):
        models = gr.Dropdown(
            [
                "yolov8n-seg.pt",
                "yolov8s-seg.pt",
                "yolov8m-seg.pt",
                "yolov8l-seg.pt",
                "yolov8x-seg.pt",
            ],
            type="value",
            value="yolov8s-seg.pt",
            label="Select Model:",
        )

        annotators_list = gr.CheckboxGroup(
            choices=[
                "BoundingBox",
                "Mask",
                "Halo",
                "Ellipse",
                "BoxCorner",
                "Circle",
                "Label",
                "Blur",
                "Pixelate",
                "HeatMap",
                "Dot",
                "Triangle",
            ],
            value=["BoundingBox", "Mask"],
            label="Select Annotators:",
        )

        gr.Markdown("## Color Picker 🎨")
        with gr.Row(variant="panel"):
            with gr.Column():
                colorbb = gr.ColorPicker(value="#A351FB", label="BoundingBox")
                colormask = gr.ColorPicker(value="#A351FB", label="Mask")
                colorellipse = gr.ColorPicker(value="#A351FB", label="Ellipse")
            with gr.Column():
                colorbc = gr.ColorPicker(value="#A351FB", label="BoxCorner")
                colorcir = gr.ColorPicker(value="#A351FB", label="Circle")
                colorlabel = gr.ColorPicker(value="#A351FB", label="Label")
            with gr.Column():
                colorhalo = gr.ColorPicker(value="#A351FB", label="Halo")
                colordot = gr.ColorPicker(value="#A351FB", label="Dot")
                colortri = gr.ColorPicker(value="#A351FB", label="Triangle")

        with gr.Row():
            with gr.Column():
                with gr.Tab("Input image"):
                    image_input = gr.Image(type="numpy", show_label=False)
            with gr.Column():
                with gr.Tab("Result image"):
                    image_output = gr.Image(type="numpy", show_label=False)
        image_button = gr.Button(value="Annotate it!", variant="primary")

        image_button.click(
            annotator,
            inputs=[
                image_input,
                models,
                annotators_list,
                colorbb,
                colormask,
                colorellipse,
                colorbc,
                colorcir,
                colorlabel,
                colorhalo,
                colortri,
                colordot,
            ],
            outputs=image_output,
        )

        gr.Markdown("## Image Examples 🖼️")
        gr.Examples(
            examples=[
                os.path.join(os.path.abspath(""), "./assets/city.jpg"),
                os.path.join(os.path.abspath(""), "./assets/household.jpg"),
                os.path.join(os.path.abspath(""), "./assets/industry.jpg"),
                os.path.join(os.path.abspath(""), "./assets/retail.jpg"),
                os.path.join(os.path.abspath(""), "./assets/aerodefence.jpg"),
                "https://media.roboflow.com/efficient-sam/corgi.jpg",
                "https://media.roboflow.com/efficient-sam/horses.jpg",
                "https://media.roboflow.com/efficient-sam/bears.jpg",
            ],
            inputs=image_input,
            outputs=image_output,
            fn=annotator,
            cache_examples=False,
        )

        annotators_list.change(
            fn=annotator,
            inputs=[
                image_input,
                models,
                annotators_list,
                colorbb,
                colormask,
                colorellipse,
                colorbc,
                colorcir,
                colorlabel,
                colorhalo,
                colortri,
                colordot,
            ],
            outputs=image_output,
        )

        def change_color(color: ColorPicker):
            color.change(
                fn=annotator,
                inputs=[
                    image_input,
                    models,
                    annotators_list,
                    colorbb,
                    colormask,
                    colorellipse,
                    colorbc,
                    colorcir,
                    colorlabel,
                    colorhalo,
                    colortri,
                    colordot,
                ],
                outputs=image_output,
            )

        colors = [
            colorbb,
            colormask,
            colorellipse,
            colorbc,
            colorcir,
            colorlabel,
            colorhalo,
            colortri,
            colordot,
        ]

        for color in colors:
            change_color(color)
