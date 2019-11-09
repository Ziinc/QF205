"""
Entrypoint for the app.
"""

from app import App
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

qtCreatorFile = "app/LoanFactoringUI.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    app = App()
    app.show()
    sys.exit(app.exec_())
