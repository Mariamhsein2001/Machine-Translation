# 🚀 Machine Translation System 

Welcome to the Machine Translation System repository! This project is designed to help you easily deploy and use a state-of-the-art translation model with Gradio and Flask.It uses Bi-directional LSTM architecture to translate english to french sentences . 

## 🚀 Project Overview

This repository is divided into two main parts:

1. **Gradio Deployment**: A simple, interactive web interface for testing the translation model using Gradio.
2. **Translator Core**: The heart of the system, including the model, tokenizer,dockerfile and Flask web application for more extensive deployment.

Let's dive into the details!


## 🌟 Gradio Deployment

The `gradio` folder makes it super easy to test the translation model with a user-friendly interface. 

### 🚀 Steps to Deploy with Gradio

1. **Run the Notebook**: Open `gradio/Gradio.ipynb` in Google Colab and run the collab.
2. **Upload Your Model**: Place the trained model zip folder(model.zip) in the collab notebook .
3. **Interact with the model**

## 🔧 Translator Core

The `translator` folder is the backbone of our translation system, handling the model logic and serving it through a Flask web application.

### 🛠️ Core Components

#### **model folder** contains  :
  1.  **model.py**: Defines the `Translator` class with model loading and translation functions.
  2.  **model_bidirectional.h5** : the model weights and architecture
  3.  **tokenzier** : the english and french tokenizer
- 

#### 📱 Flask Web Application

- **app.py**: The main application script to run the Flask server.
- **templates/index.html**: A sleek HTML interface for the translation web app.
- **static/style.css**: Custom styles to make the interface look awesome.

#### 🐳 Docker Deployment

Want to deploy with Docker? We've got you covered!

- **Dockerfile**: Creates a Docker image for the Flask application.

### 🚀 Running the Application

1. Build the Docker image:
   ```bash
   docker build -t machine_translation:latest .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 machine_translation:latest
   ```

## 📚 Conclusion

This repository provides a seamless setup for deploying and testing a machine translation model using Gradio and Flask. Whether you're running it locally or deploying in the cloud with Docker, you're all set to explore the power of translation technology!

Feel free to fork, modify, and enhance this project. Contributions and feedback are always welcome. Happy translating! 🌍💬

For any questions or issues, reach out via GitHub issues or contact us directly. Let's make translation technology accessible to everyone! 🚀🌟
