#!/usr/bin/env python3

# Copyright (C) 2022  Doguhan Sariturk
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# You should have received a copy of the GNU General Public License

import sys

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from HEACalculator.ui.HEACalculatorMain import Ui_HEACalculator
from HEACalculator.ui.parametersPage import Ui_ParametersPage
from HEACalculator.ui.batchCalculationsPage import Ui_BatchCalculationsPage
from HEACalculator.ui.aboutPage import Ui_AboutPage
from HEACalculator.ui.converterPage import Ui_ConverterPage

from HEACalculator.core.HEA import HEACalculator, __version__


class AlignDelegate(QtWidgets.QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter


class ItemDelegate(QtWidgets.QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        QtCore.QLocale.setDefault(QtCore.QLocale(QtCore.QLocale.C))
        lineEdt = QtWidgets.QLineEdit(parent)
        lineEdt.setValidator(QtGui.QDoubleValidator(0.0, 100.0, 3))
        return lineEdt


class ConverterPage(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.aboutPage = Ui_ConverterPage()
        self.aboutPage.setupUi(self)


class AboutPage(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.aboutPage = Ui_AboutPage()
        self.aboutPage.setupUi(self)


class BatchCalculationsPage(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.batchCalculationsPage = Ui_BatchCalculationsPage()
        self.batchCalculationsPage.setupUi(self)


class ParametersPage(QtWidgets.QWidget):

    elementEmitted = QtCore.pyqtSignal(str, bool)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.parametersPage = Ui_ParametersPage()
        self.parametersPage.setupUi(self)

        self.selectedElements = {}

        self.parametersPage.resultsTreeWidget.header().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        itemDelegate = ItemDelegate(self.parametersPage.tableWidget)
        self.parametersPage.tableWidget.setItemDelegate(itemDelegate)

        self.parametersPage.ClearAllPushButton.setEnabled(False)
        self.parametersPage.CalculatePushButton.setEnabled(False)

        for name in dir(self.parametersPage):
            if 'ebtn' in name:
                btn = getattr(self.parametersPage, name)
                btn.clicked[bool].connect(self.emitElement)

        self.elementEmitted.connect(self.handleElementClicked)
        self.parametersPage.tableWidget.cellChanged.connect(self.handleAmountChanged)
        self.parametersPage.ClearAllPushButton.pressed.connect(self.handleClearAllButton)
        self.parametersPage.CalculatePushButton.pressed.connect(self.handleCalculateButton)

    def calculate(self, formula):
        if not self.parametersPage.resultsTreeWidget.findItems(formula, QtCore.Qt.MatchExactly):
            res = HEACalculator(formula)
            res.calculate()
            resList = res.get_list()
            QtWidgets.QTreeWidgetItem(self.parametersPage.resultsTreeWidget, resList)

    def handleCalculateButton(self):
        formula = ''.join(['%s%d' % (k, v) for k, v in self.selectedElements.items()])
        self.calculate(formula)

    def handleClearAllButton(self):
        self.parametersPage.tableWidget.setRowCount(0)
        self.parametersPage.resultsTreeWidget.clear()
        self.selectedElements.clear()
        for name in dir(self.parametersPage):
            if 'ebtn' in name:
                btn = getattr(self.parametersPage, name)
                btn.setChecked(False)
        self.parametersPage.ClearAllPushButton.setEnabled(False)
        self.parametersPage.CalculatePushButton.setEnabled(False)

    def handleElementClicked(self, symbol, checked):
        currentRowCount = self.parametersPage.tableWidget.rowCount()

        if checked and (symbol not in self.selectedElements):
            self.parametersPage.ClearAllPushButton.setEnabled(True)
            self.parametersPage.CalculatePushButton.setEnabled(True)
            percentage = 100/(len(self.selectedElements) + 1) if len(self.selectedElements) + 1 != 1 else 100
            self.selectedElements = {k: percentage for k, v in self.selectedElements.items()}
            self.selectedElements.update({symbol: float(percentage)})
            self.parametersPage.tableWidget.insertRow(currentRowCount)
            elmItem = QtWidgets.QTableWidgetItem(symbol)
            elmItem.setFlags(QtCore.Qt.ItemIsEnabled)
            elmItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.parametersPage.tableWidget.setItem(currentRowCount, 0, elmItem)
            amount = "{:.2f}".format(percentage)
            amountItem = QtWidgets.QTableWidgetItem(amount)
            amountItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.parametersPage.tableWidget.setItem(currentRowCount, 1, amountItem)
            for row in range(self.parametersPage.tableWidget.rowCount()):
                self.parametersPage.tableWidget.item(row, 1).setText(amount)
        elif not checked and symbol in self.selectedElements:
            item = self.parametersPage.tableWidget.findItems(symbol, QtCore.Qt.MatchExactly)
            for it in item:
                self.parametersPage.tableWidget.removeRow(it.row())
            del self.selectedElements[symbol]
            percentage = 100 / (len(self.selectedElements)) if len(self.selectedElements) != 0 else 100
            self.selectedElements = {k: float(percentage) for k, v in self.selectedElements.items()}
            amount = "{:.2f}".format(percentage)
            for row in range(self.parametersPage.tableWidget.rowCount()):
                self.parametersPage.tableWidget.item(row, 1).setText(amount)
            if not self.selectedElements:
                self.parametersPage.ClearAllPushButton.setEnabled(False)
                self.parametersPage.CalculatePushButton.setEnabled(False)

    def handleAmountChanged(self, row, column):
        if column != 0:
            element = self.parametersPage.tableWidget.item(row, 0).text()
            amount = self.parametersPage.tableWidget.item(row, 1).text()
            if element in self.selectedElements.keys():
                self.selectedElements.update({element: float(amount)})

    def emitElement(self, checked):
        symbol = self.sender().text()
        self.elementEmitted.emit(symbol, checked)


class HEACalculatorMainWindow(QtWidgets.QMainWindow):

    BTN_BACKGROUND_COLOR_HIGHLIGHTED = """QPushButton{background-color: #3E5C76}
                                          QPushButton:hover{background-color: #3E5C76}
                                          QPushButton:pressed{background-color: #748CAB;}"""

    BTN_BACKGROUND_COLOR_DEFAULT = """QPushButton{background-color: #1D2D44}
                                      QPushButton:hover{background-color: #3E5C76}
                                      QPushButton:pressed{background-color: #748CAB;}"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.ui = Ui_HEACalculator()
        self.ui.setupUi(self)

        self.setWindowTitle("HEACalculator | MDL")

        self.oldPos = self.pos()

        self.parametersPage = ParametersPage()
        self.aboutPage = AboutPage()
        self.batchCalculationsPage = BatchCalculationsPage()
        self.converterPage = ConverterPage()

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.stackedWidget.addWidget(self.parametersPage)
        self.ui.stackedWidget.addWidget(self.converterPage)
        self.ui.stackedWidget.addWidget(self.batchCalculationsPage)
        self.ui.stackedWidget.addWidget(self.aboutPage)

        self.ui.btnParameters.setStyleSheet("QPushButton{background-color: #3E5C76}")

        self.ui.btnParameters.clicked.connect(self.btn_parameters_clicked)
        self.ui.btnConverter.clicked.connect(self.btn_converter_clicked)
        self.ui.btnBatchAmount.clicked.connect(self.btn_batch_amount_clicked)
        self.ui.btnMDL.clicked.connect(self.helpAbout)
        self.ui.btnClose.clicked.connect(self.close)

    def btn_parameters_clicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.parametersPage)
        self.ui.btnParameters.setStyleSheet(self.BTN_BACKGROUND_COLOR_HIGHLIGHTED)
        self.ui.btnConverter.setStyleSheet(self.BTN_BACKGROUND_COLOR_DEFAULT)
        self.ui.btnBatchAmount.setStyleSheet(self.BTN_BACKGROUND_COLOR_DEFAULT)
        self.ui.btnMDL.setStyleSheet(self.BTN_BACKGROUND_COLOR_DEFAULT)

    def btn_converter_clicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.converterPage)
        self.ui.btnParameters.setStyleSheet(self.BTN_BACKGROUND_COLOR_DEFAULT)
        self.ui.btnConverter.setStyleSheet(self.BTN_BACKGROUND_COLOR_HIGHLIGHTED)
        self.ui.btnBatchAmount.setStyleSheet(self.BTN_BACKGROUND_COLOR_DEFAULT)
        self.ui.btnMDL.setStyleSheet(self.BTN_BACKGROUND_COLOR_DEFAULT)

    def btn_batch_amount_clicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.batchCalculationsPage)
        self.ui.btnParameters.setStyleSheet(self.BTN_BACKGROUND_COLOR_DEFAULT)
        self.ui.btnConverter.setStyleSheet(self.BTN_BACKGROUND_COLOR_DEFAULT)
        self.ui.btnBatchAmount.setStyleSheet(self.BTN_BACKGROUND_COLOR_HIGHLIGHTED)
        self.ui.btnMDL.setStyleSheet(self.BTN_BACKGROUND_COLOR_DEFAULT)

    def btn_mdl_clicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.aboutPage)
        self.ui.btnParameters.setStyleSheet(self.BTN_BACKGROUND_COLOR_DEFAULT)
        self.ui.btnConverter.setStyleSheet(self.BTN_BACKGROUND_COLOR_DEFAULT)
        self.ui.btnBatchAmount.setStyleSheet(self.BTN_BACKGROUND_COLOR_DEFAULT)
        self.ui.btnMDL.setStyleSheet(self.BTN_BACKGROUND_COLOR_HIGHLIGHTED)

    @staticmethod
    def helpAbout():
        __ABOUT_TEXT = """<b>HEA Calculator v {}
    <p>Copyright &copy; 2020 MDL (METU).
    <p>This application can be used to perform calculations on
    thermodynamic parameters of high-entropy alloys."""

        __ABOUT_BOX = QMessageBox()
        __ABOUT_BOX.setIconPixmap(QtGui.QPixmap(":/img/images/ic1.png"))
        __ABOUT_BOX.setText(__ABOUT_TEXT.format(__version__))
        __ABOUT_BOX.setWindowTitle("About | HEA Calculator | MDL")
        __ABOUT_BOX.exec_()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


def run():
    application = QtWidgets.QApplication([])
    application.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(":/icons/images/icon.ico")))
    window = HEACalculatorMainWindow()
    desktop = QtWidgets.QDesktopWidget().availableGeometry()
    width = (desktop.width() - window.width()) / 2
    height = (desktop.height() - window.height()) / 2
    window.show()
    window.move(int(width), int(height))
    sys.exit(application.exec_())


if __name__ == "__main__":
    run()
