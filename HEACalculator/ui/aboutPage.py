# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutPage(object):
    def setupUi(self, AboutPage):
        AboutPage.setObjectName("AboutPage")
        AboutPage.resize(1000, 658)
        AboutPage.setMinimumSize(QtCore.QSize(1000, 300))
        AboutPage.setMaximumSize(QtCore.QSize(1000, 9999))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        AboutPage.setFont(font)
        AboutPage.setStyleSheet("QWidget{background-color: #0D1321;};")

        self.retranslateUi(AboutPage)
        QtCore.QMetaObject.connectSlotsByName(AboutPage)

    def retranslateUi(self, AboutPage):
        _translate = QtCore.QCoreApplication.translate
        AboutPage.setWindowTitle(_translate("AboutPage", "Form"))
import HEACalculator_rc