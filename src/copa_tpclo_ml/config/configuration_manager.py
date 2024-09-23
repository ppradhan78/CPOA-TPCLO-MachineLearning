import yaml

class ConfigurationManager:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config_data = self._load_config()

    def _load_config(self):
        try:
            with open(self.config_file, 'r') as file:
                config = yaml.safe_load(file)
                return config
        except FileNotFoundError:
            print(f"Configuration file {self.config_file} not found.")
            return {}
        except yaml.YAMLError:
            print(f"Error parsing YAML from {self.config_file}.")
            return {}

    def get(self, key, default=None):
        return self.config_data.get(key, default)