ELEGANT_THEME = """
QWidget {
    background-color: #121212;
    color: #E0E0E0;
    font-family: 'Segoe UI Variable Display', 'Segoe UI', sans-serif;
    font-size: 14px;
}

/* Headings */
QLabel#heading {
    font-size: 20px;
    font-weight: 600;
    color: #BB86FC;
    padding: 10px 0;
}

/* Timer Display */
QLabel#timerDisplay {
    font-family: 'Roboto Mono', 'Courier New', monospace;
    font-size: 96px;
    font-weight: 300;
    color: #03DAC6;
    background-color: #1E1E1E;
    border-radius: 12px;
    padding: 20px 40px;
    border: 1px solid #333333;
}
QLabel#timerDisplay[warning="true"] {
    color: #CF6679;
    background-color: #2C1818;
    border: 1px solid #CF6679;
}

/* Group Boxes (Settings) */
QGroupBox {
    border: 1px solid #333333;
    border-radius: 8px;
    margin-top: 24px;
    padding-top: 10px;
    font-weight: 600;
    color: #BB86FC;
    background-color: #1E1E1E;
}
QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 0 10px;
    background-color: #121212; 
    /* Slightly hides the line behind text */
}

/* Buttons */
QPushButton {
    background-color: #2D2D2D;
    border: 1px solid #444444;
    border-radius: 6px;
    color: #E0E0E0;
    padding: 8px 20px;
    font-weight: 600;
    min-width: 80px;
}
QPushButton:hover {
    background-color: #383838;
    border: 1px solid #BB86FC;
    color: #FFFFFF;
}
QPushButton:pressed {
    background-color: #BB86FC;
    color: #000000;
}

/* Primary Action Button */
QPushButton#actionButton {
    background-color: #3700B3;
    color: #FFFFFF;
    border: 1px solid #3700B3;
}
QPushButton#actionButton:hover {
    background-color: #6200EE;
    border: 1px solid #BB86FC;
}

/* Destructive Button */
QPushButton#stopButton {
    background-color: #2C1818;
    color: #CF6679;
    border: 1px solid #CF6679;
}
QPushButton#stopButton:hover {
    background-color: #CF6679;
    color: #000000;
}

/* Inputs */
QLineEdit, QSpinBox {
    background-color: #1E1E1E;
    border: 1px solid #333333;
    border-radius: 4px;
    padding: 6px;
    color: #E0E0E0;
    font-weight: 500;
}
QLineEdit:focus, QSpinBox:focus {
    border: 1px solid #BB86FC;
    background-color: #252525;
}

/* Scroll Area & Team List */
QScrollArea {
    border: none;
    background-color: transparent;
}
QScrollBar:vertical {
    border: none;
    background: #121212;
    width: 8px;
    margin: 0px 0px 0px 0px;
}
QScrollBar::handle:vertical {
    background: #333333;
    min-height: 20px;
    border-radius: 4px;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

/* Team Card */
QWidget#teamCard {
    background-color: #1E1E1E;
    border: 1px solid #333333;
    border-radius: 8px;
}
QWidget#teamCard:hover {
    border: 1px solid #555555;
}

/* Team Name Input */
QLineEdit#teamNameInputs {
    background-color: transparent;
    border: 1px solid transparent;
    font-weight: bold;
    font-size: 16px;
    color: #E0E0E0;
}
QLineEdit#teamNameInputs:hover {
    border: 1px solid #444444;
    background-color: #252525;
}
QLineEdit#teamNameInputs:focus {
    border: 1px solid #BB86FC;
    background-color: #252525;
}

QLabel#teamScore {
    font-size: 28px;
    font-weight: bold;
    color: #03DAC6;
    padding: 0 10px;
}

/* Splitter */
QSplitter::handle {
    background-color: #333333;
}
"""
