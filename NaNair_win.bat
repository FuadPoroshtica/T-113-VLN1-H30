@echo off
echo Checking for Python installation...

python --version >nul 2>&1
if %errorlevel% neq 0 goto NoPython

echo Python is installed, proceeding...
echo Installing requirements...
pip install -r Source/requirements.txt

echo Running the application...
python Source/main.py

goto End

:NoPython
echo Python is not installed. Please install Python and retry.
goto End

:End
pause
