class PVPDialogController():
    def __init__(self, view):
        self._view = view
        self._connectSignals()
    
    def _connectSignals(self):
        self._view.beginButton.clicked.connect(self._view.close)
