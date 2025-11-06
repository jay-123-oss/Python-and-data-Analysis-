import pygame
import time
from datetime import datetime

alarm_time = input("Enter alarm time in HH:MM format (24-hour): ")

print(f"Alarm set for {alarm_time}. Waiting...")

while True:
    now = datetime.now().strftime("%H:%M")
    if now == alarm_time:
        print("Alarm ringing!")
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("sound.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        break
    time.sleep(1)