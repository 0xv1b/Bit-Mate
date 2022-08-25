from inspect import classify_class_attrs
import pyautogui
import logging
from threading import Timer
from threading import Thread
from time import sleep


class Bot():
    def __init__(self, config):
        self._config = config

        logging.basicConfig(level=logging.DEBUG, filename='../log/app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')
        logging.debug("Setup Logging")
    
    def runPVP(self, times):
        logging.debug(f"Running PVP {times} times.")
        
        info = self._config._loadConfig()
        pvp = self.calculatePosition(info["position"]["pvp"])
        pvp_play = self.calculatePosition(info["position"]["pvp_play"])
        pvp_fight = self.calculatePosition(info["position"]["pvp_fight"])
        pvp_accept = self.calculatePosition(info["position"]["pvp_accept"])
        pvp_town = self.calculatePosition(info["position"]["pvp_town"])
        pvp_exit = self.calculatePosition(info["position"]["pvp_exit"])

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
                # So we don't interact with an item and hide the button from view
                pyautogui.moveTo(0, 0)
                sleep(pvp_duration)
                pyautogui.click(pvp_town)
                sleep(3)
                pyautogui.click(pvp_exit)   
                sleep(1)
        
        Thread(target=aux).start()


    def runWorldBoss(self, times):
        pass

    def runRaid(self, times, difficulty = "Heroic"):
        logging.debug(f"Running Raid {times} times at {difficulty} difficulty")

        info = self._config._loadConfig()

        raid = self.calculatePosition(info["position"]["raid"])
        raid_summon = self.calculatePosition(info["position"]["raid_summon"])
        raid_normal = self.calculatePosition(info["position"]["raid_normal"])
        raid_hard = self.calculatePosition(info["position"]["raid_hard"])
        raid_heroic = self.calculatePosition(info["position"]["raid_heroic"])
        raid_accept = self.calculatePosition(info["position"]["raid_accept"])
        raid_town = self.calculatePosition(info["position"]["raid_town"])
        raid_exit = self.calculatePosition(info["position"]["raid_exit"])

        raid_duration = info["duration"]["raid"]

        def aux():
            for x in range(times):
                pyautogui.click(raid)
                sleep(1)
                pyautogui.click(raid_summon)
                sleep(1)
                
                match difficulty:
                    case "Normal":
                        pyautogui.click(raid_normal)
                    case "Hard":
                        pyautogui.click(raid_hard)
                    case "Heroic":
                        pyautogui.click(raid_heroic)
                sleep(1)
                pyautogui.click(raid_accept)
                # so we dont interact with items and block the button from view
                pyautogui.moveTo(0, 0)
                sleep(raid_duration)
                pyautogui.click(raid_town)
                sleep(3)
                pyautogui.click(raid_exit)   
                sleep(1)
        
        Thread(target=aux).start()

        

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