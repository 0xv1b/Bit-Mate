import sys

from PyQt5.QtWidgets import QApplication

from views.mainwindow import MainWindow
from rootcontroller import RootController
from config import Config


def main():
    app = QApplication(sys.argv)
    view = MainWindow()
    view.show()
    RootController(view=view, config=Config())

    style = """
    QWidget {background: #505a68;}
    QToolBar {border: 1px solid #262d37;}
    QLabel {color: #FFFFFF;}
    QPushButton {background: #262d37; color: #FFFFFF; border-radius: 5px; margin-top: 5px; margin-right: 5px;}
    QPushButton:hover {background: #16181a;  margin-top: 0px; margin-right: 0px;}
    QSpinBox {color: #000000;} 
    """
    app.setStyleSheet(style)

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()