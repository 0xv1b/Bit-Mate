import pyautogui
from threading import Timer
from threading import Thread
from time import sleep


class Bot():
    def __init__(self, config):
        self._config = config
    
    def runPVP(self, times):
        info = self._config._loadConfig()
        print(times)

        pvp = self.calculatePosition(info["positions"]["pvp"])
        pvp_play = self.calculatePosition(info["positions"]["pvp_play"])
        pvp_fight = self.calculatePosition(info["positions"]["pvp_fight"])
        pvp_accept = self.calculatePosition(info["positions"]["pvp_accept"])
        pvp_town = self.calculatePosition(info["positions"]["pvp_town"])
        pvp_exit = self.calculatePosition(info["positions"]["pvp_exit"])

        pvp_duration = info["duration"]["pvp"]

        def aux():
            for x in range(times):
                pyautogui.click(pvp)
                sleep(1)
                pyautogui.click(pvp_play)
                sleep(1)
                pyautogui.click(pvp_fight)
                sleep(1)
                pyautogui.click(pvp_accept)
                sleep(pvp_duration)
                pyautogui.click(pvp_town)
                sleep(2)
                pyautogui.click(pvp_exit)   
                sleep(1)
        
        Thread(target=aux).start()


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