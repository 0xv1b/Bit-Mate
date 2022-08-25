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
    config = Config()
    config.updateScreenSize()
    RootController(view=view, bot = Bot(config))



    with open('./styles.css', mode='rt', encoding='utf-8') as file:
        app.setStyleSheet(file.read())

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()