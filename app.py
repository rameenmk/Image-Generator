import gradio as gr
from transformers import BlipProcessor, BlipForConditionalGeneration
from diffusers import StableDiffusionPipeline
from PIL import Image
import torch

# Load captioning model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
caption_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load Stable Diffusion model
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float32).to("cpu")
pipe.safety_checker = lambda images, **kwargs: (images, False)  # Disable safety checker

# Generate caption from image
def captioner(image):
    if image is None:
        return "Please upload an image."
    inputs = processor(image, return_tensors="pt")
    outputs = caption_model.generate(**inputs)
    return processor.decode(outputs[0], skip_special_tokens=True)

# Generate image from caption
def generate_image_from_caption(caption):
    if not caption or caption.strip() == "":
        return Image.new("RGB", (512, 512), color="gray")
    try:
        result = pipe(prompt=caption, num_inference_steps=25, guidance_scale=7.5)
        return result.images[0]
    except Exception as e:
        print("Error:", str(e))
        return Image.new("RGB", (512, 512), color="red")

# Gradio app
with gr.Blocks() as demo:
    gr.Markdown("# 🧠 Image Captioning ➜ 🎨 Caption to Image App")
    gr.Markdown("Upload an image to generate a caption. Modify the caption if needed, then generate a new image from that text!")

    with gr.Row():
        image_input = gr.Image(label="Upload Image", type="pil")
        caption_button = gr.Button("Generate Caption")
        caption_output = gr.Textbox(label="Generated Caption")

    with gr.Row():
        modified_caption = gr.Textbox(label="Modify Caption (Optional)")
        generate_button = gr.Button("Generate Image from Caption")
        image_output = gr.Image(label="Generated Image")

    caption_button.click(fn=captioner, inputs=image_input, outputs=caption_output)
    caption_output.change(fn=lambda text: text, inputs=caption_output, outputs=modified_caption)
    generate_button.click(fn=generate_image_from_caption, inputs=modified_caption, outputs=image_output)

demo.launch()
