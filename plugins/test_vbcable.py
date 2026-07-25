import os

os.environ["SDL_AUDIODRIVER"] = "wasapi"
os.environ["SDL_AUDIO_DEVICE_NAME"] = "CABLE Input (VB-Audio Virtual Cable)"

import pygame

pygame.mixer.init()

print(pygame.mixer.get_init())

input("Si no dio error, presiona Enter...")