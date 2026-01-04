import winsound
import os
from PySide6.QtCore import QObject, Slot
from app.utils.sound_generator import generate_alarm_sound

class SoundManager(QObject):
    """
    Handles playing sounds.
    """
    def __init__(self):
        super().__init__()
        self._enabled = True
        self._sound_path = os.path.join("assets", "alarm.wav")
        self._ensure_sound_exists()

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        self._enabled = value

    def _ensure_sound_exists(self):
        if not os.path.exists(self._sound_path):
            generate_alarm_sound(self._sound_path)

    @Slot()
    def play_alert(self):
        if self._enabled:
            # Play the custom sound file
            # SND_FILENAME ensures it treats the input as a filename
            # SND_ASYNC ensures it doesn't block the UI
            try:
                winsound.PlaySound(self._sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
            except Exception as e:
                print(f"Error playing sound: {e}")
                # Fallback
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS | winsound.SND_ASYNC)
