# DeepProbLog Model for Reasoning Over CAVIAR Windows with Neural Network Predictions and Complex Event Definitions

This project aims to create a DeepProbLog model for reasoning over windows obtained by CAVIAR. The model will use a neural network to predict simple events such as walking, running, etc., and a logical component to define complex events based on the simple event predictions. The model will enable us to reason about the occurrence of complex events in the CAVIAR windows.

## Requirements

To run the model, you need to install DeepProbLog using the following command:

pip install deepproblog


## How to Run

To run the model, run the following command:

python run.py

## Files

The project consists of the following files:

- `run.py`: the main file that runs the DeepProbLog model.
- `network.py`: a Python file that defines the neural network used to predict simple events.
- `model.pl`: a Prolog file that defines the complex events based on the simple event predictions of the neural network.
