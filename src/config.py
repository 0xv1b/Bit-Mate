import tomlkit
from tomlkit import dump
from tomlkit import parse
import pyautogui

# make class and pass object into controller instead of config file, class will let us get updated configuration values

class Config():
    def __init__(self):
        self.config = self._loadConfig()
    
    def _loadConfig(self):
        with open('../config/config.toml', mode='rt', encoding='utf-8') as fp:
            self.config = tomlkit.load(fp)
        return self.config

    def updateScreenSize(self):
        screen = pyautogui.size()
        with open('../config/config.toml', mode='wt', encoding='utf-8') as fp:
            self.config["screen"]["width"] = screen.width
            self.config["screen"]["height"] = screen.height
            # change to use bit heroes app size once we have that in the configuration
            self.config["screen"]["origin"] = [int((screen.width / 2) - (800 / 2)), int((screen.height / 2)  - (480 / 2))]
            dump(self.config, fp)