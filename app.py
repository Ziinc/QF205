"""
Entrypoint for the app.
"""

from app import App
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

qtCreatorFile = "app/LoanFactoringUI.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class Main(QMainWindow, Ui_MainWindow):
    def init(self):
        super().__init__()
        self.setupUi(self)
        con = Controller()

    #     self.label_RepaymentPeriod.setText(
    #         "<span style='font-size:18pt;'>Repayment Period (In Years)</span>"
    #         "<span style='font-size:12pt;'>  (Between 1-25 years)</span>")

    #     self.pushButton_Calculate.clicked.connect(self.PB_C)

    # def PB_C(self,):
    #     PV = float(self.lineEdit_LoanAmount.text())
    #     t = float(self.lineEdit_RepaymentPeriod.text())
    #     r = float(self.lineEdit_InterestRateOfLoan.text())/100
    #     P = math.ceil((r*PV/12.0)/(1-(1+r/12.0)**(-12*t)))
    #     self.lineEdit_MonthlyInstallment.setText(str(P))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())


# if __name__ == "__main__":

#     app = QApplication(sys.argv)
#     app = App()
#     app.show()
#     sys.exit(app.exec_())
