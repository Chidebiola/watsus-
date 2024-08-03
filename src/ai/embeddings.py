import tensorflow as tf
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras.preprocessing import image as keras_image
from PIL import Image
import numpy as np
import os

# Function to save an image
def save_image(image, label, index, output_dir):
    img = Image.fromarray(image)
    filename = f"{output_dir}/img_{index}_label_{label}.png"
    os.makedirs(output_dir, exist_ok=True)
    img.save(filename)

# Function to create embeddings
def create_embedding(image):
    img = Image.fromarray(image).resize((224, 224))
    img_array = keras_image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    embedding = model.predict(img_array)
    return embedding

# Load the fashion_mnist dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()

# Specify the directory where you want to save the images
output_dir = 'data/embeddings'

# Load the pre-trained EfficientNetB0 model
model = EfficientNetB0(weights='imagenet', include_top=False, pooling='avg')

# Iterate over the training set and save the images and embeddings
for i, (image, label) in enumerate(zip(x_train[::3], y_train[::3])):  # Select every other 3 images
    save_image(image, label, i, os.path.join(output_dir, 'train'))
    embedding = create_embedding(image)
    np.save(os.path.join(output_dir, 'train', f'embedding_{i}.npy'), embedding)

# Iterate over the testing set and save the images and embeddings
for i, (image, label) in enumerate(zip(x_test[::3], y_test[::3])):  # Select every other image
    save_image(image, label, i, os.path.join(output_dir, 'test'))
    embedding = create_embedding(image)
    np.save(os.path.join(output_dir, 'test', f'embedding_{i}.npy'), embedding)
