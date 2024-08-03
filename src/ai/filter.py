import tensorflow as tf
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras.preprocessing import image as keras_image
from PIL import Image
import numpy as np
import os
from sklearn.metrics.pairwise import cosine_similarity



# Function to create embeddings
def create_embedding(image):
    # Resize image to the input size required by EfficientNetB0
    img = Image.fromarray(image).resize((224, 224))

    # Convert image to array and preprocess it
    img_array = keras_image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Generate embeddings
    embedding = model.predict(img_array)
    return embedding

# Load the pre-trained EfficientNetB0 model
model = EfficientNetB0(weights='imagenet', include_top=False, pooling='avg')

# Function to load embeddings from files
def load_embeddings(directory):
    embeddings = []
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith('.npy'):
            embedding = np.load(os.path.join(directory, filename))
            embeddings.append(embedding)
            filenames.append(filename)
    return np.vstack(embeddings), filenames

# Load embeddings for train and test sets
# Specify the directory where you want to get the images
output_dir = 'data/embeddings'

train_embeddings, train_filenames = load_embeddings(os.path.join(output_dir, 'train'))
test_embeddings, test_filenames = load_embeddings(os.path.join(output_dir, 'test'))

# Function to find top N similar images
def find_similar_images(input_image, embeddings, filenames, top_n=100):
    input_embedding = create_embedding(input_image)
    similarities = cosine_similarity(input_embedding, embeddings)[0]
    top_indices = np.argsort(similarities)[-top_n:][::-1]
    return [filenames[i] for i in top_indices]

# Example usage
input_image = test_embeddings[0]  # Replace with any input image you want
similar_images = find_similar_images(input_image, train_embeddings, train_filenames, top_n=100)

#TODO Getting actual image
# input_image = "data/sample_images/image.jpg"
# image_embeding = create_embedding(input_image)
# similar_images = find_similar_images(image_embeding, train_embeddings, train_filenames, top_n=100)

print("Top 100 similar images:")
for img in similar_images:
    print(img)