import wave
import math
import struct
import os

def generate_alarm_sound(file_path="assets/alarm.wav", duration=1.0, freq=880.0):
    """
    Generates a simple beep sound and saves it as a .wav file.
    """
    # Ensure directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    sample_rate = 44100
    n_samples = int(sample_rate * duration)
    amplitude = 16000
    
    with wave.open(file_path, 'w') as wav_file:
        wav_file.setnchannels(1) # Mono
        wav_file.setsampwidth(2) # 2 bytes per sample (16-bit)
        wav_file.setframerate(sample_rate)
        
        # Create a double beep pattern
        data = bytearray()
        for i in range(n_samples):
            # Modulate frequency for a "digital" alert sound
            # Beep for 0.1s, Silence for 0.1s...
            t = i / sample_rate
            
            # Pattern: Beep-Beep-Beep
            if (t % 0.2) < 0.1: 
                value = int(amplitude * math.sin(2 * math.pi * freq * t))
            else:
                value = 0
                
            data.extend(struct.pack('<h', value))
            
        wav_file.writeframes(data)
    
    print(f"Generated alarm sound at: {os.path.abspath(file_path)}")

if __name__ == "__main__":
    generate_alarm_sound()
