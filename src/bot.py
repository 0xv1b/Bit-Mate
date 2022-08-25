import pyautogui
from functools import partial
from threading import Timer


class Bot():
    def __init__(self, config):
        self._config = config
    
    def runPVP(self):
        info = self._config._loadConfig()
        pvp = self.calculatePosition(info["positions"]["pvp"])
        print(pvp)
        pvp_play = self.calculatePosition(info["positions"]["pvp_play"])
        pvp_fight = self.calculatePosition(info["positions"]["pvp_fight"])
        pvp_accept = self.calculatePosition(info["positions"]["pvp_accept"])
        pvp_town = self.calculatePosition(info["positions"]["pvp_town"])
        pvp_exit = self.calculatePosition(info["positions"]["pvp_exit"])
        pvp_duration = info["duration"]["pvp"]


        Timer(1, pyautogui.click, args = pvp).start()
        Timer(2, pyautogui.click, args = pvp_play).start()
        Timer(3, pyautogui.click, args = pvp_fight).start()
        Timer(4, pyautogui.click, args = pvp_accept).start()
        Timer(pvp_duration + 5, pyautogui.click, args = pvp_town).start()
        Timer(25, pyautogui.click, args = pvp_exit).start()

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

    # Adds the origin from the distance from the origin to get the exact screen coordinates
    def calculatePosition(self, position):
        info = self._config._loadConfig()
        return (position[0] + info["screen"]["origin"][0], position[1] + info["screen"]["origin"][1])