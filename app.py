import os
from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import torch
from transformers import CLIPProcessor, CLIPModel
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

device = "cuda" if torch.cuda.is_available() else "cpu"
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(device)
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

captions = [
    "A cute puppy playing on the grass",
    "A bowl of fresh fruit on the table",
    "A group of people hiking in the mountains",
    "A futuristic city skyline at night",
    "A woman working on a laptop in a cafe",
    "A plate of sushi rolls on a wooden table",
    "A sunset over a calm beach",
    "A basketball player dunking a ball"
]

def recommend_caption(image_path, captions):
    image = Image.open(image_path).convert("RGB")
    inputs = processor(text=captions, images=image, return_tensors="pt", padding=True).to(device)
    outputs = model(**inputs)
    image_embeds = outputs.image_embeds
    text_embeds = outputs.text_embeds
    similarities = cosine_similarity(image_embeds.cpu().detach().numpy(), text_embeds.cpu().detach().numpy())
    best_caption_idx = similarities[0].argmax()
    return captions[best_caption_idx], similarities[0][best_caption_idx]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]
        if file.filename == "":
            return redirect(request.url)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)
        caption, score = recommend_caption(file_path, captions)
        return render_template("index.html", caption=caption, score=score, image=file.filename)
    return render_template("index.html", caption=None)

if __name__ == "__main__":
    app.run(debug=True)
