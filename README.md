# Rock Paper Scissors Game with Image Recognition

## Overview
This project implements a real-time Rock Paper Scissors game using computer vision and deep learning techniques. The game allows users to play against a computer opponent by making hand gestures in front of a webcam.

## Components
The project consists of the following components:

1. **Data Gathering**: A Python script collects images of hand gestures for training the image recognition model. Users can specify the label name and the number of samples to collect.

2. **Model Training**: The collected images are used to train a convolutional neural network (CNN) model using the Keras deep learning framework. The model architecture includes a pre-trained SqueezeNet followed by additional layers for classification.

3. **Real-time Game Play**: Another Python script allows users to play the Rock Paper Scissors game in real-time. The script captures the user's hand gesture through a webcam, predicts the corresponding move using the trained model, and displays the result against a computer-generated move.

## Key Technologies
- Python
- OpenCV (Open Source Computer Vision Library)
- Keras (Deep Learning Framework)
- Convolutional Neural Networks (CNNs)
- Image Processing
- Real-time Systems Development
- Git Version Control

## Usage
To run the project, follow these steps:

1. **Data Gathering**: Execute the `gather_images.py` script with the label name and the number of samples to collect.

2. **Model Training**: Execute the `train.py` script to train the image recognition model using the collected data.

3. **Real-time Game Play**: Run the `play.py` script to play the Rock Paper Scissors game against the computer opponent.

## Acknowledgments
- This project is inspired by the popular Rock Paper Scissors game and utilizes concepts from computer vision and deep learning.
- The code for SqueezeNet is adapted from the `keras_squeezenet` library.
