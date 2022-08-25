from functools import partial

class PVPDialogController():
    def __init__(self, view, bot):
        self._view = view
        self._bot = bot
        self._connectSignals()
    
    def _connectSignals(self):
        # why do we need to use partial?

        self._view.beginButton.clicked.connect(self._view.close)
        # is there a way to always get the newest value of runs, use lazy evaluation
        self._view.beginButton.clicked.connect(partial(self.hackyworkaround))
    
    def hackyworkaround(self):
        self._bot.runPVP(self._view.runsSpinBox.value())
