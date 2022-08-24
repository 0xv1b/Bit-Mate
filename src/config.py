import tomli 

# make class and pass object into controller instead of config file, class will let us get updated configuration values

class Config():
    def __init__(self):
        #self.config = self._loadConfig()
        pass
    
    def _loadConfig():
        with open('../config/config.toml', 'rb') as fp:
            config = tomli.load(fp)
        return config
