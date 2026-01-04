from PySide6.QtCore import QObject, QTimer, Signal

class CountdownTimer(QObject):
    """
    Manages the countdown logic with millisecond precision display.
    """
    time_updated = Signal(str)      # Emits formatted time string "HH:MM:SS:mmm"
    timer_finished = Signal()       # Emits when timer reaches 0
    warning_triggered = Signal()    # Emits when time is <= 3 seconds (for red/blink)
    
    def __init__(self, default_seconds=10.0):
        super().__init__()
        self._total_ms = int(default_seconds * 1000)
        self._current_ms = self._total_ms
        self._is_running = False
        self._warned = False
        
        self._timer = QTimer(self)
        self._timer.setInterval(10)  # Update every 10ms for smooth UI
        self._timer.timeout.connect(self._tick)

    def set_duration(self, hours, minutes, seconds, milliseconds):
        self._total_ms = (hours * 3600000) + (minutes * 60000) + (seconds * 1000) + milliseconds
        self.reset()

    def start(self):
        if self._current_ms > 0:
            self._is_running = True
            self._timer.start()

    def pause(self):
        self._is_running = False
        self._timer.stop()

    def reset(self):
        self.pause()
        self._current_ms = self._total_ms
        self._warned = False
        self._emit_time()

    def _tick(self):
        if self._current_ms > 0:
            self._current_ms -= 10
            # Clamp to 0
            if self._current_ms < 0:
                self._current_ms = 0
            
            self._emit_time()

            # Check warning (<= 3 seconds)
            if not self._warned and self._current_ms <= 3000 and self._current_ms > 0:
                self._warned = True
                self.warning_triggered.emit()

            if self._current_ms == 0:
                self.pause()
                self.timer_finished.emit()
    
    def _emit_time(self):
        # Format HH:MM:SS:mmm
        ms = self._current_ms
        hdr = ms // 3600000
        ms %= 3600000
        mins = ms // 60000
        ms %= 60000
        secs = ms // 1000
        ms %= 1000
        
        time_str = f"{hdr:02}:{mins:02}:{secs:02}:{ms:03}"
        self.time_updated.emit(time_str)
