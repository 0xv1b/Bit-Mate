from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton


class GVGDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("GVG")
        self.setFixedSize(180, 100)
        
        generalLayout = QVBoxLayout()
        formLayout = QFormLayout()

        # Badges selection Combo Box
        self.badgesBox = QComboBox()
        self.badgesBox.addItems(["1", "2", "3", "4", "5"])

        # Numbers of times to run through
        self.runsSpinBox = QSpinBox()

        formLayout.addRow('Badges', self.badgesBox)
        formLayout.addRow('Runs', self.runsSpinBox)
        generalLayout.addLayout(formLayout)

        self.okButton = QPushButton("Begin")
        generalLayout.addWidget(self.okButton)

        self.setLayout(generalLayout)