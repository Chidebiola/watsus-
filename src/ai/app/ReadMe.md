# Image Similarity Search API

This FastAPI-based application allows users to upload an image and find the 10 most similar images from a pre-defined dataset. The similarity is determined by comparing the embeddings of the uploaded image against a collection of precomputed embeddings stored locally.

## Features

- Accepts image uploads through a POST request.
- Generates embeddings for the uploaded image using a pre-trained EfficientNetB0 model.
- Compares the generated embedding against a dataset of precomputed embeddings to find the most similar images.
- Returns the filenames of the 10 most similar images.

## Getting Started

### Prerequisites

- Python 3.8+
- FastAPI
- Uvicorn (ASGI server)
- TensorFlow
- Pillow
- NumPy
- scikit-learn

### Installation

First, clone the repository:

```bash
git clone https://github.com/Chidebiola/watsus-.git
cd watsus
```

Then, install the required packages: You may wanna create a virtual env first

```bash
pip install fastapi uvicorn tensorflow pillow numpy scikit-learn
```

### Running the Application

Start the FastAPI server with Uvicorn:

```bash
uvicorn app.app:app --reload
```

This will start the server on `http://localhost:8000`. You can access the interactive API documentation by navigating to `http://localhost:8000/docs` in your web browser.

## Usage

To find similar images, send a POST request to the `/upload-image/` endpoint with an image file. The API will respond with the filenames of the 10 most similar images from the dataset.

Example using `curl`:

```bash
curl -X 'POST' \
  'http://localhost:8000/upload-image/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@path_to_your_image.jpg;type=image/jpeg'
```

Replace `path_to_your_image.jpg` with the actual path to the image you want to upload.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs, enhancements, or documentation improvements.



