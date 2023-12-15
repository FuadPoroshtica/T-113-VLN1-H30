@echo off

echo Installing requirements...
pip install -r Source/requirements.txt

echo Running the application...
python Source/main.py

pause
