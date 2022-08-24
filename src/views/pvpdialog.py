from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton


class PVPDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("PVP")
        self.setFixedSize(180, 100)
        
        generalLayout = QVBoxLayout()
        formLayout = QFormLayout()

        # Tickets selection Combo Box
        self.ticketsBox = QComboBox()
        self.ticketsBox.addItems(["1", "2", "3", "4", "5"])

        # Numbers of times to run through
        self.runsSpinBox = QSpinBox()

        formLayout.addRow('Tickets', self.ticketsBox)
        formLayout.addRow('Runs', self.runsSpinBox)
        generalLayout.addLayout(formLayout)

        self.okButton = QPushButton("Begin")
        generalLayout.addWidget(self.okButton)

        self.setLayout(generalLayout)