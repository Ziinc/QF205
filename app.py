"""
Entrypoint for the app.
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QTableWidget, QTableView
from PyQt5 import uic, QtGui
from app.controller import Controller

qtCreatorFile = "app/LoanFactoringUI.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.con = Controller()

        # table setup
        self.OverviewTable.setEditTriggers(QTableWidget.NoEditTriggers)
        self.OverviewTable.setSelectionBehavior(QTableView.SelectRows)

        # table action buttons
        self.DeleteButton.clicked.connect(self.on_delete)
        self.EditButton.clicked.connect(self.on_edit)
        # connect form buttons
        self.SaveButton.clicked.connect(self.on_save)
        self.ResetButton.clicked.connect(self.on_reset)

    def on_save(self):
        attrs = {
            'company_name': self.CompanyNameLineEdit.text(),
            'credit_terms': int(self.CreditTermsLineEdit.text()),
            'factor_pct': int(self.FactorPercentageLineEdit.text())/100,
            'factor_start_date': self.FactorStartDayLineEdit.text(),
            'amt': float(self.InvoiceAmountLineEdit.text()),
            'date': self.InvoiceDateLineEdit.text()
        }
        self.con.create_invoice(attrs)
        self.update_list()
        self.on_reset()

    def on_reset(self):
        self.CompanyNameLineEdit.setText("")
        self.CreditTermsLineEdit.setText("")
        self.FactorPercentageLineEdit.setText("")
        self.InvoiceAmountLineEdit.setText("")
        self.FactorStartDayLineEdit.setText("")
        self.InvoiceDateLineEdit.setText("")

    def update_list(self):
        data = self.con.list_invoices()
        table = self.OverviewTable
        table.setRowCount(0)
        for invoice, calculated in data:
            rowPosition = self.OverviewTable.rowCount()

            table.insertRow(rowPosition)
            table.setItem(rowPosition, 0, QTableWidgetItem(str(invoice.id)))
            table.setItem(rowPosition, 1, QTableWidgetItem(
                str(invoice.company_name)))
            table.setItem(rowPosition, 2, QTableWidgetItem(str(invoice.amt)))
            table.setItem(rowPosition, 3, QTableWidgetItem(
                str(invoice.factor_pct * 100)))
            table.setItem(rowPosition, 4, QTableWidgetItem(
                invoice.date_iso_string))
            table.setItem(rowPosition, 5, QTableWidgetItem(
                str(invoice.credit_terms)))
            table.setItem(rowPosition, 6, QTableWidgetItem(
                invoice.factor_start_date.isoformat()))

    def on_delete(self):
        items = self.OverviewTable.selectedItems()
        ids = [int(item[0]) for item in items]
        for id in ids:
            self.con.delete_invoice(id)
        self.update_list()

    def on_edit(self):
        items = self.OverviewTable.selectedItems()
        if len(items) == 0:
            return None

        item = items[0]

        id = int(item[0])

        invoice, data = self.con.get_invoice(id)

        print(f"editing invoice {invoice.id}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
