from views.dialogbase import DialogBase

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton


class WBDialog(DialogBase):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("World Boss")
        
        self.comboBox.addItems(["Heroic", "Hard", "Normal"])
        self.comboBox.setEnabled(False)

        self.formLayout.addRow('Difficulty', self.comboBox)
        self.formLayout.addRow('Runs', self.runsSpinBox)