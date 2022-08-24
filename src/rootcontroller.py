from functools import partial
import imp

import webbrowser

from PyQt5.QtWidgets import QDialogButtonBox

from views.tutorialdialog import TutorialDialog
from views.calibrationdialog import CalibrationDialog
from views.presetdialog import PresetDialog

from views.pvpdialog import PVPDialog
from views.wbdialog import WBDialog
from views.raiddialog import RaidDialog
from views.gvgdialog import GVGDialog
from views.invasiondialog import InvasionDialog
from views.trialsdialog import TrialsDialog
from views.gauntletdialog import GauntletDialog

class RootController():
    def __init__(self, view, config = None):
        self._view = view
        self._config = config
        self.tutorialdialog = TutorialDialog(parent = self._view)
        self.calibrationdialog = CalibrationDialog(parent = self._view)
        self.presetdialog = PresetDialog(parent = self._view)

        self.pvpdialog = PVPDialog(parent = self._view)
        self.wbdialog = WBDialog(parent = self._view)
        self.raiddialog = RaidDialog(parent = self._view)
        self.gvgdialog = GVGDialog(parent = self._view)
        self.invasiondialog = InvasionDialog(parent = self._view)
        self.trialsdialog = TrialsDialog(parent = self._view)
        self.guantletdialog = GauntletDialog(parent = self._view)
        

        self._connectSignals()


    def _connectSignals(self):
        self._view.Menu().addAction("Tutorial", self.tutorialdialog.show)
        self._view.Menu().addAction("GitHub", self.openGitHub)


        self._view.Toolbar().addAction("Calibrate", self.calibrationdialog.show)
        self._view.Toolbar().addAction("Preset", self.presetdialog.show)

        self._view.buttons['PVP'].clicked.connect(self.pvpdialog.show)
        self._view.buttons['World Boss'].clicked.connect(self.wbdialog.show)
        self._view.buttons['Raids'].clicked.connect(self.raiddialog.show)
        self._view.buttons['GVG'].clicked.connect(self.gvgdialog.show)
        self._view.buttons['Invasion'].clicked.connect(self.invasiondialog.show)
        self._view.buttons['Trials'].clicked.connect(self.trialsdialog.show)
        self._view.buttons['Gauntlet'].clicked.connect(self.guantletdialog.show)
    
    def _connectPVPSignal():
        pass

    def _connectWBSignal():
        pass
    
    def _connectRaidSignal():
        pass
    
    def openGitHub(self):
        url = "https://github.com/0xv1b/Worb-API"
        webbrowser.open(url, new=0, autoraise=True)
    

