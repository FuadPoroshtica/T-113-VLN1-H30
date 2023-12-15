#!/bin/bash

# Check for Python
if command -v python3 &>/dev/null; then
    PYTHON_CMD=python3
elif command -v python &>/dev/null; then
    PYTHON_CMD=python
else
    echo "Python is not installed. Please install Python and retry."
    exit 1
fi

echo "Python is installed, proceeding..."
echo "Installing requirements..."
$PYTHON_CMD -m pip install -r Source/requirements.txt

echo "Running the application..."
$PYTHON_CMD Source/main.py
