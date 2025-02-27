import serial
from gtts import gTTS
import os


warning_text = "Your Lunch box is in danger"

language = 'en'

ser = serial.Serial('COM4', 115200, timeout=1)

warning_speech_obj = gTTS(text=warning_text, lang=language, slow=False)

warning_speech_obj.save('warning.mp3')

def read_serial():
    while True:
        temp = ser.readline().decode().strip()
        if temp:
            print("Your Lunch box is in danger")
            os.system('start warning.mp3')
            
            
read_serial()