from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QPushButton, QSpinBox, QGroupBox, QGridLayout, QFrame
)
from PySide6.QtCore import Qt, QSize
from app.core.timer_logic import CountdownTimer
from app.utils.sound import SoundManager

class TimerWidget(QWidget):
    def __init__(self, timer_logic: CountdownTimer, sound_manager: SoundManager):
        super().__init__()
        self.timer = timer_logic
        self.sound = sound_manager
        self.init_ui()
        self.connect_signals()
        
    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(20)
        
        # Header
        header = QLabel("COUNTDOWN")
        header.setObjectName("heading")
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        # Display Area (Centered)
        self.time_label = QLabel("00:00:00:000")
        self.time_label.setObjectName("timerDisplay")
        self.time_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.time_label)
        
        # Spacing
        layout.addSpacing(20)
        
        # Controls (Start/Pause/Reset)
        controls_layout = QHBoxLayout()
        controls_layout.setSpacing(15)
        controls_layout.setAlignment(Qt.AlignCenter)
        
        self.start_btn = QPushButton("START")
        self.start_btn.setObjectName("actionButton")
        self.start_btn.setMinimumSize(QSize(120, 50))
        self.start_btn.setCursor(Qt.PointingHandCursor)
        self.start_btn.clicked.connect(self.timer.start)
        
        self.pause_btn = QPushButton("PAUSE")
        self.pause_btn.setMinimumSize(QSize(100, 50))
        self.pause_btn.setCursor(Qt.PointingHandCursor)
        self.pause_btn.clicked.connect(self.timer.pause)
        
        self.reset_btn = QPushButton("RESET")
        self.reset_btn.setObjectName("stopButton")
        self.reset_btn.setMinimumSize(QSize(100, 50))
        self.reset_btn.setCursor(Qt.PointingHandCursor)
        self.reset_btn.clicked.connect(self.timer.reset)
        
        controls_layout.addWidget(self.start_btn)
        controls_layout.addWidget(self.pause_btn)
        controls_layout.addWidget(self.reset_btn)
        layout.addLayout(controls_layout)
        
        # Settings Group
        settings_group = QGroupBox("CONFIGURATION")
        settings_layout = QGridLayout()
        settings_layout.setHorizontalSpacing(15)
        settings_layout.setVerticalSpacing(15)
        
        # Time Inputs
        self.h_input = self.create_time_input(99)
        self.m_input = self.create_time_input(59)
        self.s_input = self.create_time_input(59, 10) 
        self.ms_input = self.create_time_input(999, 0, 10)
        
        labels = ["HOURS", "MINUTES", "SECONDS", "MS"]
        inputs = [self.h_input, self.m_input, self.s_input, self.ms_input]
        
        for i, (lbl, inp) in enumerate(zip(labels, inputs)):
            l = QLabel(lbl)
            l.setAlignment(Qt.AlignCenter)
            l.setStyleSheet("font-size: 10px; color: #888;")
            settings_layout.addWidget(inp, 0, i)
            settings_layout.addWidget(l, 1, i)
        
        # Update Defaults Button
        self.set_time_btn = QPushButton("UPDATE DURATION")
        self.set_time_btn.setCursor(Qt.PointingHandCursor)
        self.set_time_btn.clicked.connect(self.update_duration)
        settings_layout.addWidget(self.set_time_btn, 2, 0, 1, 4)
        
        settings_group.setLayout(settings_layout)
        layout.addStretch()
        layout.addWidget(settings_group)
        
        # Sound Toggle (Small footer)
        footer_layout = QHBoxLayout()
        self.sound_toggle = QPushButton("🔊 Sound Effects: ON")
        self.sound_toggle.setCheckable(True)
        self.sound_toggle.setChecked(True)
        self.sound_toggle.setFlat(True)
        self.sound_toggle.setStyleSheet("text-align: left; color: #888;")
        self.sound_toggle.setCursor(Qt.PointingHandCursor)
        self.sound_toggle.clicked.connect(self.toggle_sound)
        footer_layout.addWidget(self.sound_toggle)
        
        layout.addLayout(footer_layout)
        
        self.setLayout(layout)

    def create_time_input(self, max_val, default=0, step=1):
        spin = QSpinBox()
        spin.setRange(0, max_val)
        spin.setValue(default)
        spin.setSingleStep(step)
        spin.setAlignment(Qt.AlignCenter)
        spin.setFixedHeight(40)
        return spin

    def connect_signals(self):
        self.timer.time_updated.connect(self.update_display)
        self.timer.warning_triggered.connect(self.start_warning)
        self.timer.timer_finished.connect(self.on_finished)

    def update_duration(self):
        h = self.h_input.value()
        m = self.m_input.value()
        s = self.s_input.value()
        ms = self.ms_input.value()
        self.timer.set_duration(h, m, s, ms)
        # Reset visual state
        self.time_label.setProperty("warning", "false")
        self.time_label.style().unpolish(self.time_label)
        self.time_label.style().polish(self.time_label)

    def update_display(self, time_str):
        self.time_label.setText(time_str)

    def start_warning(self):
        self.time_label.setProperty("warning", "true")
        self.time_label.style().unpolish(self.time_label)
        self.time_label.style().polish(self.time_label)

    def on_finished(self):
        self.sound.play_alert()

    def toggle_sound(self):
        is_on = self.sound_toggle.isChecked()
        self.sound.enabled = is_on
        self.sound_toggle.setText(f"🔊 Sound Effects: {'ON' if is_on else 'OFF'}")
