import os

import pygame

from config import AUDIO_DIR

pygame.mixer.init()

class AudioManager:
    @staticmethod
    def play_last_audio():
        audio_files = os.listdir(AUDIO_DIR)
        if audio_files:
            last_audio = os.path.join(AUDIO_DIR, audio_files[-1])
            pygame.mixer.music.load(last_audio)
            pygame.mixer.music.play()
        else:
            print("Nenhum áudio encontrado para reprodução.")

    @staticmethod
    def stop_audio():
        pygame.mixer.music.stop()
