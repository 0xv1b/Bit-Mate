from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget

from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QStatusBar

from PyQt5.QtGui import QFont


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.setWindowIcon(QtGui.QIcon('./assets/Icon.png'))
        self.setMinimumSize(440, 280)
        self.setWindowTitle("Bit Mate")

        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        self._createMenu()
        self._createToolbar()
        # self._createStatusBar()
        self._createLabel()
        self._createButtons()
    
    def _createMenu(self):
        self.menu = self.menuBar().addMenu("Menu")
        self.menu.addAction('Exit', self.close)
    
    def Menu(self):
        return self.menu

    def _createToolbar(self):
        self.tools = QToolBar()
        self.addToolBar(self.tools)

    def Toolbar(self):
        return self.tools

    def _createStatusBar(self):
        self.status = QStatusBar()
        self.status.showMessage("Check us out on GitHub")
        self.setStatusBar(self.status)

    def StatusBar(self):
        self.status

    def _createLabel(self):
        self.header = QLabel()
        self.header.setText("Bit Mate")
        self.header.setAlignment(Qt.AlignCenter)
        self.header.setFont(QFont('Arial', 18))

        self.generalLayout.addWidget(self.header)
    
    def _createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        
        buttons = {'Preset': (0, 0),
                   'PVP': (0, 1),
                   'World Boss': (0, 2),
                   'Raids': (0, 3),
                   'Invasion': (1, 0),
                   'GVG': (1, 1),
                   'Trials': (1, 2),
                   'Gauntlet': (1, 3),
                  }
                  
        for text, pos in buttons.items():
            self.buttons[text] = QPushButton(text)
            self.buttons[text].setFixedSize(90, 40)
            buttonsLayout.addWidget(self.buttons[text], pos[0], pos[1])
        
        self.buttons["Preset"].setEnabled(False)
        self.buttons["World Boss"].setEnabled(False)
        self.buttons["Raids"].setEnabled(False)
        self.buttons["Invasion"].setEnabled(False)
        self.buttons["GVG"].setEnabled(False)
        self.buttons["Trials"].setEnabled(False)
        self.buttons["Gauntlet"].setEnabled(False)
            
        self.generalLayout.addLayout(buttonsLayout)