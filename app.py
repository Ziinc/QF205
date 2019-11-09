"""
Entrypoint for the app.
"""

from app import App
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from app.controller import Controller

qtCreatorFile = "app/LoanFactoringUI.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
