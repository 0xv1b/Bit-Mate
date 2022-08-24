import tomli 

# make class and pass object into controller instead of config file, class will let us get updated configuration values

class Config():
    def __init__(self):
        self.config = self._loadConfig()
    
    def _loadConfig(self):
        with open('../config/config.toml', 'rb') as fp:
            config = tomli.load(fp)
        return config
