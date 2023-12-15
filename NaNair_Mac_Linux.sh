#!/bin/bash

echo "Installing requirements..."
python -m pip install -r Source/requirements.txt

echo "Running the application..."
python Source/main.py
