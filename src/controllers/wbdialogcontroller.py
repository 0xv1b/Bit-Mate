from functools import partial

class WBDialogController():
    def __init__(self, view, bot):
        self._view = view
        self._bot = bot