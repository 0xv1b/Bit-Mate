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

from controllers.pvpdialogcontroller import PVPDialogController
from controllers.wbdialogcontroller import WBDialogController
from controllers.raiddialogcontroller import RaidDialogController
from controllers.gvgdialogcontroller import GVGDialogController
from controllers.invasiondialogcontroller import InvasionDialogController
from controllers.trialsdialogcontroller import TrialsDialogController
from controllers.gauntletdialogcontroller import GauntletDialogController

class RootController():
    def __init__(self, view, config = None):
        self._view = view
        self._config = config
        
        self.tutorialdialog = TutorialDialog(parent = self._view)
        self.calibrationdialog = CalibrationDialog(parent = self._view)
        self.presetdialog = PresetDialog(parent = self._view)

        self._connectSignals()


    def _connectSignals(self):
        self._view.Menu().addAction("Tutorial", self.tutorialdialog.show)


        self._view.Toolbar().addAction("Calibrate", self.calibrationdialog.show)
        self._view.Toolbar().addAction("Preset", self.presetdialog.show)

        self._connectPVPSignal()
        self._connectWBSignal()
        self._connectRaidSignal()
        self._connectGVGSignal()
        self._connectInvasionSignal()
        self._connectTrialsSignal()
        self._connectGauntletSignal()

    def _connectPVPSignal(self):
        self.pvpdialog = PVPDialog(parent = self._view)
        self._view.buttons['PVP'].clicked.connect(self.pvpdialog.show)
        PVPDialogController(self.pvpdialog)

    def _connectWBSignal(self):
        self.wbdialog = WBDialog(parent = self._view)
        self._view.buttons['World Boss'].clicked.connect(self.wbdialog.show)
        WBDialogController(self.wbdialog)
    
    def _connectRaidSignal(self):
        self.raiddialog = RaidDialog(parent = self._view)
        self._view.buttons['Raids'].clicked.connect(self.raiddialog.show)
        RaidDialogController(self.raiddialog)


    def _connectGVGSignal(self):
        self.gvgdialog = GVGDialog(parent = self._view)
        self._view.buttons['GVG'].clicked.connect(self.gvgdialog.show)
        GVGDialogController(self.gvgdialog)

    def _connectInvasionSignal(self):
        self.invasiondialog = InvasionDialog(parent = self._view)
        self._view.buttons['Invasion'].clicked.connect(self.invasiondialog.show)
        InvasionDialogController(self.invasiondialog)

    def _connectTrialsSignal(self):
        self.trialsdialog = TrialsDialog(parent = self._view)
        self._view.buttons['Trials'].clicked.connect(self.trialsdialog.show)
        TrialsDialogController(self.trialsdialog)


    def _connectGauntletSignal(self):
        self.gauntletdialog = GauntletDialog(parent = self._view)
        self._view.buttons['Gauntlet'].clicked.connect(self.gauntletdialog.show)
        GauntletDialogController(self.gauntletdialog)

    

