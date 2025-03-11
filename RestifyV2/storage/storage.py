import json
import os

from config import DATA_FILE, AUDIO_DIR


class Storage:
    def __init__(self):
        self.data = self.load_config()

    def load_config(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        return {}

    def save_config(self):
        with open(DATA_FILE, "w") as file:
            json.dump(self.data, file)

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value
        self.save_config()

# Criar pasta para armazenar áudios, se necessário
if not os.path.exists(AUDIO_DIR):
    os.makedirs(AUDIO_DIR)

storage = Storage()
