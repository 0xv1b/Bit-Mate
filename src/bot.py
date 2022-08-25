import pyautogui
from functools import partial
from threading import Timer


class Bot():
    def __init__(self, config):
        self._config = config
    
    def runPVP(self):
        info = self._config._loadConfig()
        pvp = (info["positions"]["pvp"][0] + info["screen"]["origin"][0], info["positions"]["pvp"][1] + info["screen"]["origin"][1])
        print(pvp)
        pvp_play = (info["positions"]["pvp_play"][0] + info["screen"]["origin"][0], info["positions"]["pvp_play"][1] + info["screen"]["origin"][1])
        pvp_fight = (info["positions"]["pvp_fight"][0] + info["screen"]["origin"][0], info["positions"]["pvp_fight"][1] + info["screen"]["origin"][1],)
        pvp_accept = (info["positions"]["pvp_accept"][0] + info["screen"]["origin"][0], info["positions"]["pvp_accept"][1] + info["screen"]["origin"][1])
        pvp_town = (info["positions"]["pvp_town"][0] + info["screen"]["origin"][0], info["positions"]["pvp_town"][1] + info["screen"]["origin"][1])
        pvp_exit = (info["positions"]["pvp_exit"][0] + info["screen"]["origin"][0], info["positions"]["pvp_exit"][1] + info["screen"]["origin"][1])
        pvp_duration = info["duration"]["pvp"]


        Timer(1, lambda : pyautogui.click(pvp)).start()
        Timer(2, lambda : pyautogui.click(pvp_play)).start()
        Timer(3, lambda : pyautogui.click(pvp_fight)).start()
        Timer(4, lambda : pyautogui.click(pvp_accept)).start()
        Timer(pvp_duration + 5, lambda : pyautogui.click(pvp_town)).start()
        Timer(20, lambda : pyautogui.click(pvp_exit)).start()

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