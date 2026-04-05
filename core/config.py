import json

class Config:
    def __init__(self, file_path):
        self.path = file_path
        self.CONFIG = {}
        self.load()
    
    def load(self):
        with open(self.path, "r") as config_file:
            self.CONFIG = json.load(config_file)
    def get(self, key):
        return self.CONFIG[key]