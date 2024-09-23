import configparser

class IniConfigurationManager:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self._load_config()

    def _load_config(self):
        try:
            with open(self.config_file, 'r') as file:
                self.config.read_file(file)
        except FileNotFoundError:
            print(f"Configuration file {self.config_file} not found.")
        except configparser.Error as e:
            print(f"Error parsing INI file {self.config_file}: {e}")

    def get(self, section, key, fallback=None):
        try:
            return self.config.get(section, key, fallback=fallback)
        except configparser.NoSectionError:
            print(f"Section [{section}] not found in the configuration file.")
            return fallback
        except configparser.NoOptionError:
            print(f"Key '{key}' not found in section [{section}].")
            return fallback