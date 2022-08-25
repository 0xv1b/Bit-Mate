import sys

from PyQt5.QtWidgets import QApplication

from mainwindow import MainWindow
from rootcontroller import RootController
from config import Config
from bot import Bot


def main():
    app = QApplication(sys.argv)
    view = MainWindow()
    view.show()
    RootController(view=view, bot = Bot(config = Config()))

    style = """
    QWidget {background: #505a68; font-family: "Lucida Console", "Courier New", monospace;}
    QToolBar {border: 1px solid #262d37;}
    QLabel {color: #FFFFFF;}
    QPushButton {background: #262d37; color: #FFFFFF; border-radius: 5px; margin-top: 5px; margin-right: 5px;}
    QPushButton:hover {background: #16181a;  margin-top: 0px; margin-right: 0px;}
    QPushButton:disabled {background: #aeaeae;}
    QSpinBox {color: #000000;} 
    """
    app.setStyleSheet(style)

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()