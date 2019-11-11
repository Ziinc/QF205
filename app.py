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
    editing_invoice_id = None

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
        try:
            attrs = {
                'company_name': self.CompanyNameLineEdit.text(),
                'credit_terms': int(self.CreditTermsLineEdit.text()),
                'factor_pct': float(self.FactorPercentageLineEdit.text())/100,
                'factor_start_date': self.FactorStartDayLineEdit.text(),
                'amt': self.InvoiceAmountLineEdit.text(),
                'date': self.InvoiceDateLineEdit.text()
            }
            if self.editing_invoice_id == None:
                self.con.create_invoice(attrs)
            else:
                self.con.update_invoice(self.editing_invoice_id, attrs)
            self.update_list()
            self.on_reset()
        except Exception as e:
            self.logger(str(e))

    def on_reset(self):
        self.CompanyNameLineEdit.setText("")
        self.CreditTermsLineEdit.setText("")
        self.FactorPercentageLineEdit.setText("")
        self.InvoiceAmountLineEdit.setText("")
        self.FactorStartDayLineEdit.setText("")
        self.InvoiceDateLineEdit.setText("")
        self.editing_invoice_id = None

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
            table.setItem(rowPosition, 2, QTableWidgetItem(
                f"${invoice.amt:.2f}"))
            table.setItem(rowPosition, 3, QTableWidgetItem(
                str(invoice.factor_pct * 100)))
            table.setItem(rowPosition, 4, QTableWidgetItem(
                invoice.date_iso_string))
            table.setItem(rowPosition, 5, QTableWidgetItem(
                str(invoice.credit_terms)))
            table.setItem(rowPosition, 6, QTableWidgetItem(
                invoice.factor_start_date.isoformat()))
            table.setItem(rowPosition, 7, QTableWidgetItem(
                f"${calculated['amt_to_collect']:.2f}"))
            table.setItem(rowPosition, 8, QTableWidgetItem(
                f"${calculated['factor_amt']:.2f}"))
            table.setItem(rowPosition, 9, QTableWidgetItem(
                str(calculated['is_stale'])))

    def on_delete(self):
        try:
            items = self.OverviewTable.selectedItems()
            if len(items) == 0 or items[0].text() == '':
                return None
            id_col = items[0]
            id = float(id_col.text())
            self.con.delete_invoice(id)
            self.update_list()
        except Exception as e:
            self.logger(str(e))

    def on_edit(self):
        try:
            items = self.OverviewTable.selectedItems()
            if len(items) == 0 or items[0].text() == '':
                return None

            id_col = items[0]

            id = float(id_col.text())

            invoice, data = self.con.get_invoice(id)
            self.CompanyNameLineEdit.setText(str(invoice.company_name))
            self.CreditTermsLineEdit.setText(str(invoice.credit_terms))
            self.FactorPercentageLineEdit.setText(str(invoice.factor_pct*100))
            self.InvoiceAmountLineEdit.setText(str(invoice.amt))
            self.FactorStartDayLineEdit.setText(
                invoice.factor_start_date.isoformat())
            self.InvoiceDateLineEdit.setText(invoice.date_iso_string)

            self.editing_invoice_id = id
            self.TabWidget.setCurrentIndex(1)
        except Exception as e:
            self.logger(str(e))

    def logger(self, msg):
        self.LogBox.setPlainText(msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
