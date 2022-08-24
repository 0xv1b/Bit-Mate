import pyautogui


class Bot():
    def __init__(self, config):
        self._config = config

    def test(self):
        print("HELLLLLLLOOOOOOOOO")
    
    def runPVP(self):
        info = self._config._loadConfig()
        x = info["positions"]["pvp"][0] + info["screen"]["origin"][0]
        y = info["positions"]["pvp"][1] + info["screen"]["origin"][1]
        pyautogui.click(x,y)

    def runWorldBoss(self):
        pass

    def runRaid(self):
        pass

    def runGVG(self):
        pass

    def runInvasion(self):
        pass

    def runTrials(self):
        pass

    def runGauntlet(self):
        pass