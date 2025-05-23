# 🧠 Image Captioning & 🎨 Generation App

[![Live on Hugging Face](https://img.shields.io/badge/Live-HuggingFace-blue?logo=huggingface)](https://huggingface.co/spaces/rameenmk/image-generator)

This interactive Gradio app lets users:
1. **Upload an image** and generate a meaningful caption using a BLIP (Bootstrapped Language-Image Pretraining) model.
2. **Modify the generated caption** if desired.
3. **Generate a new image** from that caption using Stable Diffusion v1.5.

---

## 🚀 Live Demo

Try it now 👉 [Live on Hugging Face Spaces](https://huggingface.co/spaces/rameenmk/image-generator)

---

## ✨ Features

- 🖼️ Image-to-caption generation with `Salesforce/blip-image-captioning-base`
- 📝 Editable captions to fine-tune output prompts
- 🎨 Text-to-image generation using `runwayml/stable-diffusion-v1-5`
- ⚡ Powered by Gradio for real-time interaction
- 🔒 Safety checker disabled for simpler setup (can be re-enabled)

---

## 🛠️ How to Run Locally

Clone this repository and install dependencies:

```bash
git clone https://github.com/rameenmk/image-generator.git
cd image-generator
pip install -r requirements.txt
python app.py
```

---

## 🧠 Models Used

- **Captioning Model:** [`Salesforce/blip-image-captioning-base`](https://huggingface.co/Salesforce/blip-image-captioning-base)
- **Image Generation Model:** [`runwayml/stable-diffusion-v1-5`](https://huggingface.co/runwayml/stable-diffusion-v1-5)

---

## 📁 Project Structure

| File              | Description                                |
|-------------------|--------------------------------------------|
| `app.py`          | Main Gradio application                    |
| `requirements.txt`| Required Python packages                   |
| `README.md`       | Project overview and usage instructions    |

---

## 👩‍💻 Author

**Rameen Mustafa**  
MS in Business Analytics, UMass Amherst  
📫 rmustafa@umass.edu  
🔗 [GitHub](https://github.com/rameenmk)

---

## 📅 Last Updated

> Backdated for portfolio alignment (Nov 2023)

---
