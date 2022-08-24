import sys

from PyQt5.QtWidgets import QApplication

from views.mainwindow import MainWindow
from rootcontroller import RootController
from config import Config


def main():
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = MainWindow()
    view.show()
    RootController(view=view, config=Config())
    # Execute the calculator's main loop
    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()