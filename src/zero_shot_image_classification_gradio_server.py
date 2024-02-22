# -*- coding: utf-8 -*-
# @place: Pudong, Shanghai
# @file: zero_shot_image_classification_gradio_server.py
# @time: 2024/2/22 11:04
import pandas as pd
import gradio as gr
from PIL import Image
import requests
from transformers import CLIPProcessor, CLIPModel


model_path = "/data-ai/usr/lmj/models/clip-vit-base-patch32"
model = CLIPModel.from_pretrained(model_path)
processor = CLIPProcessor.from_pretrained(model_path)
print("load model...")


def image_predict(image_url, prompts):
    image = Image.open(requests.get(image_url, stream=True).raw)
    labels = prompts.split(',')
    inputs = processor(text=labels, images=image, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image
    probs = logits_per_image.softmax(dim=1).detach().numpy().tolist()[0]
    return image, gr.BarPlot(
        value=pd.DataFrame(
            {
                "label": labels,
                "prob": probs,
            }
        ),
        x="label",
        y="prob",
        width=400,
        color='label',
        title="Zero Shot Image Classification",
        tooltip=["label", "prob"],
        y_lim=[0, 1]
    )


if __name__ == '__main__':
    with gr.Blocks() as demo:
        with gr.Row():
            with gr.Column():
                image_urls = gr.TextArea(lines=1, placeholder="Enter image urls", label="Images")
                prompt = gr.TextArea(lines=3, placeholder="Enter image urls", label="Images")
            with gr.Column():
                search_image = gr.Image(type='pil')
                plot = gr.BarPlot()
                submit = gr.Button("Classify")
        submit.click(fn=image_predict,
                     inputs=[image_urls, prompt],
                     outputs=[search_image, plot])
    demo.launch(server_name="0.0.0.0", server_port=50073)
