from functools import partial

class RaidDialogController():
    def __init__(self, view, bot):
        self._view = view
        self._bot = bot
        self._connectSignals()
    
    def _connectSignals(self):

        self._view.beginButton.clicked.connect(self._view.close)
        self._view.beginButton.clicked.connect(partial(lambda : self._bot.runRaid(self._view.runsSpinBox.value(), self._view.comboBox.currentText())))