import json

class JsonConfigurationManager:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config_data = self._load_config()

    def _load_config(self):
        try:
            with open(self.config_file, 'r') as file:
                config = json.load(file)
                return config
        except FileNotFoundError:
            print(f"Configuration file {self.config_file} not found.")
            return {}
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {self.config_file}.")
            return {}

    def get(self, key, default=None):
        return self.config_data.get(key, default)
