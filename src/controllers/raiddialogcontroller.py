from functools import partial

class RaidDialogController():
    def __init__(self, view, bot):
        self._view = view
        self._bot = bot