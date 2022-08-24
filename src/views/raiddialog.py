from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton


class RaidDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Raids")
        self.setFixedSize(180, 100)
        
        generalLayout = QVBoxLayout()
        formLayout = QFormLayout()

        # Difficulty selection Combo Box
        self.difficultyBox = QComboBox()
        self.difficultyBox.addItems(["Heroic", "Hard", "Normal"])

        # Numbers of times to run through
        self.runsSpinBox = QSpinBox()

        formLayout.addRow('Difficulty', self.difficultyBox)
        formLayout.addRow('Runs', self.runsSpinBox)
        generalLayout.addLayout(formLayout)

        self.okButton = QPushButton("Begin")
        generalLayout.addWidget(self.okButton)

        self.setLayout(generalLayout)