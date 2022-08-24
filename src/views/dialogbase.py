from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton


class DialogBase(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Dialog")
        self.setFixedSize(180, 100)
        
        self.generalLayout = QVBoxLayout()
        self.formLayout = QFormLayout()

        # Tokens selection Combo Box
        self.comboBox = QComboBox()

        # Numbers of times to run through
        self.runsSpinBox = QSpinBox()

        # formLayout.addRow('Tokens', self.tokensBox)
        # formLayout.addRow('Runs', self.runsSpinBox)
        self.generalLayout.addLayout(self.formLayout)

        self.beginButton = QPushButton("Begin")
        self.beginButton.setMinimumHeight(25)
        self.generalLayout.addWidget(self.beginButton)

        self.setLayout(self.generalLayout)