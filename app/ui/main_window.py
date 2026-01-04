from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QSplitter
)
from PySide6.QtCore import Qt
from app.ui.timer_widget import TimerWidget
from app.ui.team_widget import TeamWidget
from app.core.timer_logic import CountdownTimer
from app.core.team_logic import TeamManager
from app.utils.sound import SoundManager
from app.styles.modern import ELEGANT_THEME

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chel Project - Countdown Timer Modern")
        self.resize(1100, 750)
        
        # Initialize Core Logic
        self.timer_logic = CountdownTimer()
        self.team_manager = TeamManager()
        self.sound_manager = SoundManager()
        
        # Apply Theme
        self.setStyleSheet(ELEGANT_THEME)
        
        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main Layout (Splitter for resizing)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        splitter = QSplitter(Qt.Horizontal)
        splitter.setHandleWidth(2)
        
        # Left Side: Timer
        self.timer_widget = TimerWidget(self.timer_logic, self.sound_manager)
        splitter.addWidget(self.timer_widget)
        
        # Right Side: Teams
        self.team_widget = TeamWidget(self.team_manager)
        splitter.addWidget(self.team_widget)
        
        # Set initial sizes (40% timer, 60% teams approx)
        splitter.setSizes([450, 650])
        
        main_layout.addWidget(splitter)
        
    def closeEvent(self, event):
        # Graceful shutdown if needed (stop threads etc)
        self.timer_logic.pause()
        super().closeEvent(event)
