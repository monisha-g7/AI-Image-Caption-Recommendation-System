# 📸 AI Image Caption Recommender using CLIP (Flask Web App)

## 🧠 Project Overview
This project is an AI-powered web application that uses **OpenAI's CLIP (Contrastive Language–Image Pre-training)** model to recommend the most relevant caption for an uploaded image. The model calculates **cosine similarity** between the image and a list of **predefined captions** and selects the one that best matches the visual content.

### 🚀 Why This Project?
With the explosion of visual content on platforms like **Instagram, Pinterest, and e-commerce sites**, it's increasingly important to have tools that automatically generate or suggest contextually accurate and engaging captions. This project demonstrates how **multimodal learning (vision + language)** can be applied in real-world scenarios.

---

## ✨ Features
- 🔼 Upload any `.jpg` or `.png` image from your browser
- 🤖 Recommends the best-matching caption using the CLIP model
- 📏 Displays the **cosine similarity score** between the image and captions
- 🌐 Easy-to-use **Flask-based web interface**

---

## 🧰 Technologies Used
- [OpenAI CLIP](https://huggingface.co/openai/clip-vit-base-patch32) (via Hugging Face)
- Flask (Python web framework)
- PyTorch (for model execution)
- scikit-learn (for similarity computation)
- HTML5 (for file upload UI)
- PIL (Image processing)

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/clip-caption-recommender.git
cd clip-caption-recommender
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App
```bash
python app.py
```

Navigate to `http://127.0.0.1:5000` in your browser.

---

## 🖼 Example Output
**Uploaded Image:** A photo of a sunset on a beach  
**Recommended Caption:** `"A sunset over a calm beach"`  
**Similarity Score:** `0.87`

---

## 📁 File Structure
```
CLIP_Caption_FLASK_UI/
├── app.py                  # Flask backend
├── templates/
│   └── index.html          # Web interface
├── uploads/                # Auto-created folder for image uploads
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 📌 Future Improvements
- Support for **user-submitted captions**
- Option to **rank top-N matching captions**
- Integration with **image caption generation models**
- Deployment on **Hugging Face Spaces** or **Render**

---

## 💬 License & Credits
This project is open-source and free to use under the MIT License.  
Built with ❤️ using CLIP by [OpenAI](https://openai.com/) and [Hugging Face Transformers](https://huggingface.co/transformers/).

---

> ✨ _Empower your images with intelligent captions_ ✨
