from fastapi import FastAPI, File, UploadFile
import numpy as np
from PIL import Image
from tensorflow.keras.applications.efficientnet import EfficientNetB0, preprocess_input
from tensorflow.keras.preprocessing import image as keras_image
from sklearn.metrics.pairwise import cosine_similarity
import os
import io
from embeddings import create_embedding
from filter import load_embeddings, find_similar_images

app = FastAPI()

# Load the pre-trained EfficientNetB0 model
model = EfficientNetB0(weights='imagenet', include_top=False, pooling='avg')

def create_embedding(image):
    img = Image.fromarray(image).resize((224, 224))
    img_array = keras_image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    embedding = model.predict(img_array)
    return embedding

def load_embeddings(directory):
    embeddings = []
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith('.npy'):
            embedding = np.load(os.path.join(directory, filename))
            embeddings.append(embedding)
            filenames.append(filename)
    return np.vstack(embeddings), filenames

output_dir = 'data/embeddings'
train_embeddings, train_filenames = load_embeddings(output_dir)

def find_similar_images(input_embedding, embeddings, filenames, top_n=10):
    similarities = cosine_similarity(input_embedding, embeddings)[0]
    top_indices = np.argsort(similarities)[-top_n:][::-1]
    return [filenames[i] for i in top_indices]

@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    image = keras_image.img_to_array(Image.open(io.BytesIO(contents)))
    
    input_embedding = create_embedding(image)
    similar_images = find_similar_images(input_embedding, train_embeddings, train_filenames, top_n=10)
    
    return {"similar_images": similar_images}