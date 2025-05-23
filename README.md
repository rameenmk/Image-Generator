# 🎨 Text-to-Image Generator using Stable Diffusion (Gradio App)

[![Live on Hugging Face](https://img.shields.io/badge/Live-HuggingFace-blue?logo=huggingface)](https://huggingface.co/spaces/rameenmk/image-generator)

This repository demonstrates a text-to-image generation application built with the `runwayml/stable-diffusion-v1-5` model. The interface is developed using the Gradio library, enabling users to input natural language prompts and receive AI-generated images in real-time.

## Project Objective

The goal of this project is to provide an intuitive and accessible interface for exploring text-to-image synthesis using state-of-the-art diffusion models. This application serves as a foundation for further experimentation in creative AI, visual storytelling, and generative design.

---

## Live Application

You can access and interact with the deployed version of this application via Hugging Face Spaces

---

## Key Features

- Generates high-resolution 512x512 pixel images based on user-provided text prompts.
- Uses Stable Diffusion v1.5, a robust latent diffusion model known for producing photorealistic outputs.
- Includes a clean and responsive Gradio web interface.
- Runs both locally and in hosted environments (e.g., Hugging Face Spaces).

---

## Libraries and Frameworks

| Library         | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `diffusers`     | Hugging Face library for diffusion-based generative models                 |
| `transformers`  | Required for tokenizer/model handling during inference                     |
| `torch`         | PyTorch deep learning framework; backend for Stable Diffusion              |
| `Pillow`        | Python Imaging Library used for image processing and formatting            |
| `Gradio`        | Lightweight Python library for creating web-based machine learning demos   |

Note: It is built entirely on the PyTorch ecosystem.

---

## Model Description

**Model:** `runwayml/stable-diffusion-v1-5`  
- Developed by Stability AI and integrated via Hugging Face
- Uses a latent diffusion process to convert text prompts into images
- Designed for high-performance, general-purpose text-to-image tasks

### Input
Natural language text prompt (e.g., "A futuristic city skyline at night")

### Output
Generated image in PNG format with resolution 512x512

### Parameters Used
- `num_inference_steps`: 25 (controls the quality and speed of generation)
- `guidance_scale`: 7.5 (influences prompt adherence)

---

## System Requirements

| Resource       | Minimum                          | Recommended                        |
|----------------|-----------------------------------|------------------------------------|
| RAM            | 8 GB                              | 16 GB or higher                    |
| GPU            | NVIDIA GTX 1060 6GB               | NVIDIA RTX 3060 or better (>=8GB) |
| Storage        | 5 GB (for model files)            | 10 GB (with cache)                 |
| OS             | Linux, Windows, or macOS          | Latest Python 3.8+ supported       |

Note: On CPU-only machines, image generation may take 30–90 seconds per image. A dedicated GPU is recommended for practical use.

---

## How to Run Locally

### Clone the Repository
```bash
git clone https://github.com/rameenmk/image-generator.git
cd image-generator
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Start the Application
```bash
python app.py
```

The application will launch at `http://127.0.0.1:7860`

---

## Folder Structure

| File              | Description                                 |
|-------------------|---------------------------------------------|
| `app.py`          | Contains the Gradio application logic       |
| `requirements.txt`| Lists all required Python packages          |
| `README.md`       | Project documentation                       |

---

## Use Cases

- Visual storytelling and content creation
- Rapid prototyping for creative industries
- Educational demonstrations in AI and ML
- Experimentation with generative design systems

---

## Limitations and Ethical Considerations
- Generated content may not always reflect prompt intent accurately.
- Biases present in training data can influence outputs.
- Consider responsible use, especially when creating public-facing media.

---
