from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton


class GauntletDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Guantlet")
        self.setFixedSize(180, 100)
        
        generalLayout = QVBoxLayout()
        formLayout = QFormLayout()

        # Tokens selection Combo Box
        self.tokensBox = QComboBox()
        self.tokensBox.addItems(["1", "2", "3", "4", "5"])

        # Numbers of times to run through
        self.runsSpinBox = QSpinBox()

        formLayout.addRow('Tokens', self.tokensBox)
        formLayout.addRow('Runs', self.runsSpinBox)
        generalLayout.addLayout(formLayout)

        self.okButton = QPushButton("Begin")
        generalLayout.addWidget(self.okButton)

        self.setLayout(generalLayout)