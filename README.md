# Chel Project - Countdown Timer Modern

A Python desktop application built with **PySide6**.

## How to Run via Terminal

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   python main.py
   ```

## How to Build Executable (Windows)

This application uses `PyInstaller` to create a standalone `.exe` file.

1. **Install PyInstaller** (if not already installed):
   ```bash
   pip install pyinstaller
   ```

2. **Build Command**:
   Run the following command in your terminal from the project root:
   ```bash
   pyinstaller --noconfirm --onefile --windowed --name "Chel Project - Countdown Timer Modern" --clean main.py
   ```

1.  **Install PyInstaller** (if not already installed):
    ```bash
    pip install pyinstaller
    ```

2.  **Build Command**:
    Run the following command in your terminal from the project root:
    ```bash
    pyinstaller --noconfirm --onefile --windowed --name "Chel Project - Countdown Timer Modern" --clean main.py
    ```

    **Explanation of flags**:
    -   `--noconfirm`: Don't ask for confirmation to overwrite.
    -   `--onefile`: Bundle everything into a single `.exe` file.
    -   `--windowed`: Hide the console window when running (GUI mode).
    -   `--name "Chel Project - Countdown Timer Modern"`: Name the output file `Chel Project - Countdown Timer Modern.exe`.
    -   `--clean`: Clean PyInstaller cache before building.
    -   `--add-data "assets;assets"`: Bundles the assets (optional, as the app auto-generates them if missing).

3.  **Locate the Executable**:
    The `Chel Project - Countdown Timer Modern.exe` file will be generated in the `dist/` folder.

## Distribution & Installation

Once built, the application is **portable**.

1.  **Move the File**: You can take `dist/Chel Project - Countdown Timer Modern.exe` and move it to your Desktop, Program Files, or a USB drive.
2.  **Running**: Double-click `.exe` to run.
3.  **Custom Sound**:
    -   When you run the app, it will automatically create an `assets` folder next to it containing `alarm.wav`.
    -   To change the sound, simply replace `assets/alarm.wav` with your own `.wav` file.

## Features

  - Custom duration input.
- **Team Management**:
  - Add unlimited teams.
  - Automatic naming (Team 1, Team 2...).
  - Adjustable default score increments.
- **Sound**:
  - Toggleable alert sound on timer finish.
