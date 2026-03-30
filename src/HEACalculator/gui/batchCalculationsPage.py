"""Batch/range-search page UI definition for HEACalculator.

Auto-generated from Qt Designer. Defines the range-search page used to sweep
element compositions across a user-defined percentage range and collect HEA
thermodynamic results in bulk. Provides the same periodic-table element
selector as the parameters page alongside start/end/step inputs, a results
table, and CSV export controls.
"""

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_BatchCalculationsPage(object):
    """Qt Designer-generated UI class for the Batch Calculations (range search) page.

    Renders the element selector, range configuration inputs (start, end,
    step), and a results table for iterating over composition ranges.
    """

    def setupUi(self, BatchCalculationsPage):
        """Create and arrange all child widgets inside *BatchCalculationsPage*.

        Builds the periodic-table button grid, range parameter inputs,
        action buttons (Search, Clear, Export), and the results table.
        Applies the dark-theme stylesheet throughout.

        Args:
            BatchCalculationsPage: The ``QWidget`` instance that owns this
                UI.
        """
        BatchCalculationsPage.setObjectName("BatchCalculationsPage")
        BatchCalculationsPage.resize(1000, 658)
        BatchCalculationsPage.setMinimumSize(QtCore.QSize(1000, 300))
        BatchCalculationsPage.setMaximumSize(QtCore.QSize(1000, 9999))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(QtGui.QFont.Weight.Bold)
        BatchCalculationsPage.setFont(font)
        BatchCalculationsPage.setStyleSheet(
            "QWidget{\n"
            "                background-color: #0D1321;\n"
            "                alternate-background-color : rgb(24,30,43);\n"
            "                }\n"
            "\n"
            "                QToolTip { color: #F0EBD8; background-color: rgb(34,45,67); border: none; }\n"
            "            "
        )
        self.ebtnHe = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnHe.setGeometry(QtCore.QRect(740, 10, 29, 29))
        self.ebtnHe.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnHe.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnHe.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnHe.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnHe.setCheckable(True)
        self.ebtnHe.setAutoDefault(False)
        self.ebtnHe.setFlat(True)
        self.ebtnHe.setObjectName("ebtnHe")
        self.ebtnRa = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnRa.setGeometry(QtCore.QRect(260, 190, 29, 29))
        self.ebtnRa.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnRa.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnRa.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnRa.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnRa.setCheckable(True)
        self.ebtnRa.setAutoDefault(False)
        self.ebtnRa.setFlat(True)
        self.ebtnRa.setObjectName("ebtnRa")
        self.ebtnLu = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnLu.setGeometry(QtCore.QRect(740, 230, 29, 29))
        self.ebtnLu.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnLu.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnLu.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnLu.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnLu.setCheckable(True)
        self.ebtnLu.setAutoDefault(False)
        self.ebtnLu.setFlat(True)
        self.ebtnLu.setObjectName("ebtnLu")
        self.ebtnGa = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnGa.setGeometry(QtCore.QRect(590, 100, 29, 29))
        self.ebtnGa.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnGa.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnGa.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnGa.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnGa.setCheckable(True)
        self.ebtnGa.setAutoDefault(False)
        self.ebtnGa.setFlat(True)
        self.ebtnGa.setObjectName("ebtnGa")
        self.ebtnCa = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnCa.setGeometry(QtCore.QRect(260, 100, 29, 29))
        self.ebtnCa.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnCa.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnCa.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnCa.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnCa.setCheckable(True)
        self.ebtnCa.setAutoDefault(False)
        self.ebtnCa.setFlat(True)
        self.ebtnCa.setObjectName("ebtnCa")
        self.ebtnAu = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnAu.setGeometry(QtCore.QRect(530, 160, 29, 29))
        self.ebtnAu.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnAu.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnAu.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnAu.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnAu.setCheckable(True)
        self.ebtnAu.setAutoDefault(False)
        self.ebtnAu.setFlat(True)
        self.ebtnAu.setObjectName("ebtnAu")
        self.ebtnLa = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnLa.setGeometry(QtCore.QRect(320, 230, 29, 29))
        self.ebtnLa.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnLa.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnLa.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnLa.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnLa.setCheckable(True)
        self.ebtnLa.setAutoDefault(False)
        self.ebtnLa.setFlat(True)
        self.ebtnLa.setObjectName("ebtnLa")
        self.ebtnYb = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnYb.setGeometry(QtCore.QRect(710, 230, 29, 29))
        self.ebtnYb.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnYb.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnYb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnYb.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnYb.setCheckable(True)
        self.ebtnYb.setAutoDefault(False)
        self.ebtnYb.setFlat(True)
        self.ebtnYb.setObjectName("ebtnYb")
        self.ebtnW = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnW.setGeometry(QtCore.QRect(380, 160, 29, 29))
        self.ebtnW.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnW.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnW.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnW.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnW.setCheckable(True)
        self.ebtnW.setAutoDefault(False)
        self.ebtnW.setFlat(True)
        self.ebtnW.setObjectName("ebtnW")
        self.ebtnBk = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnBk.setGeometry(QtCore.QRect(560, 260, 29, 29))
        self.ebtnBk.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnBk.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnBk.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnBk.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnBk.setCheckable(True)
        self.ebtnBk.setAutoDefault(False)
        self.ebtnBk.setFlat(True)
        self.ebtnBk.setObjectName("ebtnBk")
        self.ebtnSc = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnSc.setGeometry(QtCore.QRect(290, 100, 29, 29))
        self.ebtnSc.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnSc.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnSc.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnSc.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnSc.setCheckable(True)
        self.ebtnSc.setAutoDefault(False)
        self.ebtnSc.setFlat(True)
        self.ebtnSc.setObjectName("ebtnSc")
        self.ebtnNi = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnNi.setGeometry(QtCore.QRect(500, 100, 29, 29))
        self.ebtnNi.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnNi.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnNi.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnNi.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnNi.setCheckable(True)
        self.ebtnNi.setAutoDefault(False)
        self.ebtnNi.setFlat(True)
        self.ebtnNi.setObjectName("ebtnNi")
        self.ebtnBa = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnBa.setGeometry(QtCore.QRect(260, 160, 29, 29))
        self.ebtnBa.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnBa.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnBa.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnBa.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnBa.setCheckable(True)
        self.ebtnBa.setAutoDefault(False)
        self.ebtnBa.setFlat(True)
        self.ebtnBa.setObjectName("ebtnBa")
        self.ebtnBh = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnBh.setGeometry(QtCore.QRect(410, 190, 29, 29))
        self.ebtnBh.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnBh.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnBh.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnBh.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnBh.setCheckable(True)
        self.ebtnBh.setAutoDefault(False)
        self.ebtnBh.setFlat(True)
        self.ebtnBh.setObjectName("ebtnBh")
        self.ebtnHs = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnHs.setGeometry(QtCore.QRect(440, 190, 29, 29))
        self.ebtnHs.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnHs.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnHs.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnHs.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnHs.setCheckable(True)
        self.ebtnHs.setAutoDefault(False)
        self.ebtnHs.setFlat(True)
        self.ebtnHs.setObjectName("ebtnHs")
        self.ebtnHf = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnHf.setGeometry(QtCore.QRect(320, 160, 29, 29))
        self.ebtnHf.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnHf.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnHf.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnHf.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnHf.setCheckable(True)
        self.ebtnHf.setAutoDefault(False)
        self.ebtnHf.setFlat(True)
        self.ebtnHf.setObjectName("ebtnHf")
        self.ebtnPr = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnPr.setGeometry(QtCore.QRect(380, 230, 29, 29))
        self.ebtnPr.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnPr.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnPr.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnPr.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnPr.setCheckable(True)
        self.ebtnPr.setAutoDefault(False)
        self.ebtnPr.setFlat(True)
        self.ebtnPr.setObjectName("ebtnPr")
        self.ebtnV = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnV.setGeometry(QtCore.QRect(350, 100, 29, 29))
        self.ebtnV.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnV.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnV.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnV.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnV.setCheckable(True)
        self.ebtnV.setAutoDefault(False)
        self.ebtnV.setFlat(True)
        self.ebtnV.setObjectName("ebtnV")
        self.ebtnN = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnN.setGeometry(QtCore.QRect(650, 40, 29, 29))
        self.ebtnN.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnN.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnN.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnN.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnN.setCheckable(True)
        self.ebtnN.setAutoDefault(False)
        self.ebtnN.setFlat(True)
        self.ebtnN.setObjectName("ebtnN")
        self.ebtnFr = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnFr.setGeometry(QtCore.QRect(230, 190, 29, 29))
        self.ebtnFr.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnFr.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnFr.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnFr.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnFr.setCheckable(True)
        self.ebtnFr.setAutoDefault(False)
        self.ebtnFr.setFlat(True)
        self.ebtnFr.setObjectName("ebtnFr")
        self.ebtnGd = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnGd.setGeometry(QtCore.QRect(530, 230, 29, 29))
        self.ebtnGd.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnGd.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnGd.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnGd.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnGd.setCheckable(True)
        self.ebtnGd.setAutoDefault(False)
        self.ebtnGd.setFlat(True)
        self.ebtnGd.setObjectName("ebtnGd")
        self.ebtnO = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnO.setGeometry(QtCore.QRect(680, 40, 29, 29))
        self.ebtnO.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnO.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnO.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnO.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnO.setCheckable(True)
        self.ebtnO.setAutoDefault(False)
        self.ebtnO.setFlat(True)
        self.ebtnO.setObjectName("ebtnO")
        self.ebtnPt = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnPt.setGeometry(QtCore.QRect(500, 160, 29, 29))
        self.ebtnPt.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnPt.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnPt.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnPt.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnPt.setCheckable(True)
        self.ebtnPt.setAutoDefault(False)
        self.ebtnPt.setFlat(True)
        self.ebtnPt.setObjectName("ebtnPt")
        self.ebtnLi = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnLi.setGeometry(QtCore.QRect(230, 40, 29, 29))
        self.ebtnLi.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnLi.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnLi.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnLi.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnLi.setCheckable(True)
        self.ebtnLi.setAutoDefault(False)
        self.ebtnLi.setFlat(True)
        self.ebtnLi.setObjectName("ebtnLi")
        self.ebtnP = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnP.setGeometry(QtCore.QRect(650, 70, 29, 29))
        self.ebtnP.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnP.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnP.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnP.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnP.setCheckable(True)
        self.ebtnP.setAutoDefault(False)
        self.ebtnP.setFlat(True)
        self.ebtnP.setObjectName("ebtnP")
        self.ebtnXe = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnXe.setGeometry(QtCore.QRect(740, 130, 29, 29))
        self.ebtnXe.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnXe.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnXe.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnXe.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnXe.setCheckable(True)
        self.ebtnXe.setAutoDefault(False)
        self.ebtnXe.setFlat(True)
        self.ebtnXe.setObjectName("ebtnXe")
        self.ebtnPd = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnPd.setGeometry(QtCore.QRect(500, 130, 29, 29))
        self.ebtnPd.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnPd.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnPd.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnPd.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnPd.setCheckable(True)
        self.ebtnPd.setAutoDefault(False)
        self.ebtnPd.setFlat(True)
        self.ebtnPd.setObjectName("ebtnPd")
        self.ebtnDb = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnDb.setGeometry(QtCore.QRect(350, 190, 29, 29))
        self.ebtnDb.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnDb.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnDb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnDb.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnDb.setCheckable(True)
        self.ebtnDb.setAutoDefault(False)
        self.ebtnDb.setFlat(True)
        self.ebtnDb.setObjectName("ebtnDb")
        self.ebtnRb = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnRb.setGeometry(QtCore.QRect(230, 130, 29, 29))
        self.ebtnRb.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnRb.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnRb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnRb.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnRb.setCheckable(True)
        self.ebtnRb.setAutoDefault(False)
        self.ebtnRb.setFlat(True)
        self.ebtnRb.setObjectName("ebtnRb")
        self.ebtnBi = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnBi.setGeometry(QtCore.QRect(650, 160, 29, 29))
        self.ebtnBi.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnBi.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnBi.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnBi.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnBi.setCheckable(True)
        self.ebtnBi.setAutoDefault(False)
        self.ebtnBi.setFlat(True)
        self.ebtnBi.setObjectName("ebtnBi")
        self.ebtnIn = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnIn.setGeometry(QtCore.QRect(590, 130, 29, 29))
        self.ebtnIn.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnIn.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnIn.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnIn.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnIn.setCheckable(True)
        self.ebtnIn.setAutoDefault(False)
        self.ebtnIn.setFlat(True)
        self.ebtnIn.setObjectName("ebtnIn")
        self.ebtnS = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnS.setGeometry(QtCore.QRect(680, 70, 29, 29))
        self.ebtnS.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnS.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnS.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnS.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnS.setCheckable(True)
        self.ebtnS.setAutoDefault(False)
        self.ebtnS.setFlat(True)
        self.ebtnS.setObjectName("ebtnS")
        self.ebtnAnd = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnAnd.setGeometry(QtCore.QRect(410, 230, 29, 29))
        self.ebtnAnd.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnAnd.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnAnd.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnAnd.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnAnd.setCheckable(True)
        self.ebtnAnd.setAutoDefault(False)
        self.ebtnAnd.setFlat(True)
        self.ebtnAnd.setObjectName("ebtnAnd")
        self.ebtnNa = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnNa.setGeometry(QtCore.QRect(230, 70, 29, 29))
        self.ebtnNa.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnNa.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnNa.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnNa.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnNa.setCheckable(True)
        self.ebtnNa.setAutoDefault(False)
        self.ebtnNa.setFlat(True)
        self.ebtnNa.setObjectName("ebtnNa")
        self.ebtnIr = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnIr.setGeometry(QtCore.QRect(470, 160, 29, 29))
        self.ebtnIr.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnIr.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnIr.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnIr.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnIr.setCheckable(True)
        self.ebtnIr.setAutoDefault(False)
        self.ebtnIr.setFlat(True)
        self.ebtnIr.setObjectName("ebtnIr")
        self.ebtnOs = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnOs.setGeometry(QtCore.QRect(440, 160, 29, 29))
        self.ebtnOs.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnOs.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnOs.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnOs.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnOs.setCheckable(True)
        self.ebtnOs.setAutoDefault(False)
        self.ebtnOs.setFlat(True)
        self.ebtnOs.setObjectName("ebtnOs")
        self.ebtnPu = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnPu.setGeometry(QtCore.QRect(470, 260, 29, 29))
        self.ebtnPu.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnPu.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnPu.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnPu.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnPu.setCheckable(True)
        self.ebtnPu.setAutoDefault(False)
        self.ebtnPu.setFlat(True)
        self.ebtnPu.setObjectName("ebtnPu")
        self.ebtnTe = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnTe.setGeometry(QtCore.QRect(680, 130, 29, 29))
        self.ebtnTe.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnTe.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnTe.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnTe.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnTe.setCheckable(True)
        self.ebtnTe.setAutoDefault(False)
        self.ebtnTe.setFlat(True)
        self.ebtnTe.setObjectName("ebtnTe")
        self.ebtnEs = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnEs.setGeometry(QtCore.QRect(620, 260, 29, 29))
        self.ebtnEs.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnEs.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnEs.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnEs.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnEs.setCheckable(True)
        self.ebtnEs.setAutoDefault(False)
        self.ebtnEs.setFlat(True)
        self.ebtnEs.setObjectName("ebtnEs")
        self.ebtnCe = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnCe.setGeometry(QtCore.QRect(350, 230, 29, 29))
        self.ebtnCe.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnCe.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnCe.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnCe.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnCe.setCheckable(True)
        self.ebtnCe.setAutoDefault(False)
        self.ebtnCe.setFlat(True)
        self.ebtnCe.setObjectName("ebtnCe")
        self.ebtnB = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnB.setGeometry(QtCore.QRect(590, 40, 29, 29))
        self.ebtnB.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnB.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnB.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnB.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnB.setCheckable(True)
        self.ebtnB.setAutoDefault(False)
        self.ebtnB.setFlat(True)
        self.ebtnB.setObjectName("ebtnB")
        self.ebtnRe = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnRe.setGeometry(QtCore.QRect(410, 160, 29, 29))
        self.ebtnRe.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnRe.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnRe.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnRe.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnRe.setCheckable(True)
        self.ebtnRe.setAutoDefault(False)
        self.ebtnRe.setFlat(True)
        self.ebtnRe.setObjectName("ebtnRe")
        self.ebtnCs = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnCs.setGeometry(QtCore.QRect(230, 160, 29, 29))
        self.ebtnCs.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnCs.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnCs.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnCs.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnCs.setCheckable(True)
        self.ebtnCs.setAutoDefault(False)
        self.ebtnCs.setFlat(True)
        self.ebtnCs.setObjectName("ebtnCs")
        self.ebtnCd = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnCd.setGeometry(QtCore.QRect(560, 130, 29, 29))
        self.ebtnCd.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnCd.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnCd.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnCd.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnCd.setCheckable(True)
        self.ebtnCd.setAutoDefault(False)
        self.ebtnCd.setFlat(True)
        self.ebtnCd.setObjectName("ebtnCd")
        self.ebtnPb = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnPb.setGeometry(QtCore.QRect(620, 160, 29, 29))
        self.ebtnPb.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnPb.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnPb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnPb.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnPb.setCheckable(True)
        self.ebtnPb.setAutoDefault(False)
        self.ebtnPb.setFlat(True)
        self.ebtnPb.setObjectName("ebtnPb")
        self.ebtnRn = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnRn.setGeometry(QtCore.QRect(740, 160, 29, 29))
        self.ebtnRn.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnRn.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnRn.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnRn.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnRn.setCheckable(True)
        self.ebtnRn.setAutoDefault(False)
        self.ebtnRn.setFlat(True)
        self.ebtnRn.setObjectName("ebtnRn")
        self.ebtnY = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnY.setGeometry(QtCore.QRect(290, 130, 29, 29))
        self.ebtnY.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnY.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnY.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnY.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnY.setCheckable(True)
        self.ebtnY.setAutoDefault(False)
        self.ebtnY.setFlat(True)
        self.ebtnY.setObjectName("ebtnY")
        self.ebtnU = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnU.setGeometry(QtCore.QRect(410, 260, 29, 29))
        self.ebtnU.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnU.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnU.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnU.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnU.setCheckable(True)
        self.ebtnU.setAutoDefault(False)
        self.ebtnU.setFlat(True)
        self.ebtnU.setObjectName("ebtnU")
        self.ebtnBr = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnBr.setGeometry(QtCore.QRect(710, 100, 29, 29))
        self.ebtnBr.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnBr.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnBr.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnBr.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnBr.setCheckable(True)
        self.ebtnBr.setAutoDefault(False)
        self.ebtnBr.setFlat(True)
        self.ebtnBr.setObjectName("ebtnBr")
        self.ebtnC = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnC.setGeometry(QtCore.QRect(620, 40, 29, 29))
        self.ebtnC.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnC.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnC.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnC.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnC.setCheckable(True)
        self.ebtnC.setAutoDefault(False)
        self.ebtnC.setFlat(True)
        self.ebtnC.setObjectName("ebtnC")
        self.ebtnHo = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnHo.setGeometry(QtCore.QRect(620, 230, 29, 29))
        self.ebtnHo.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnHo.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnHo.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnHo.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnHo.setCheckable(True)
        self.ebtnHo.setAutoDefault(False)
        self.ebtnHo.setFlat(True)
        self.ebtnHo.setObjectName("ebtnHo")
        self.ebtnNp = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnNp.setGeometry(QtCore.QRect(440, 260, 29, 29))
        self.ebtnNp.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnNp.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnNp.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnNp.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnNp.setCheckable(True)
        self.ebtnNp.setAutoDefault(False)
        self.ebtnNp.setFlat(True)
        self.ebtnNp.setObjectName("ebtnNp")
        self.ebtnEu = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnEu.setGeometry(QtCore.QRect(500, 230, 29, 29))
        self.ebtnEu.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnEu.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnEu.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnEu.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnEu.setCheckable(True)
        self.ebtnEu.setAutoDefault(False)
        self.ebtnEu.setFlat(True)
        self.ebtnEu.setObjectName("ebtnEu")
        self.ebtnMn = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnMn.setGeometry(QtCore.QRect(410, 100, 29, 29))
        self.ebtnMn.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnMn.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnMn.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnMn.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnMn.setCheckable(True)
        self.ebtnMn.setAutoDefault(False)
        self.ebtnMn.setFlat(True)
        self.ebtnMn.setObjectName("ebtnMn")
        self.ebtnGe = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnGe.setGeometry(QtCore.QRect(620, 100, 29, 29))
        self.ebtnGe.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnGe.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnGe.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnGe.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnGe.setCheckable(True)
        self.ebtnGe.setAutoDefault(False)
        self.ebtnGe.setFlat(True)
        self.ebtnGe.setObjectName("ebtnGe")
        self.ebtnAc = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnAc.setEnabled(True)
        self.ebtnAc.setGeometry(QtCore.QRect(320, 260, 29, 29))
        self.ebtnAc.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnAc.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnAc.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnAc.setAcceptDrops(False)
        self.ebtnAc.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnAc.setCheckable(True)
        self.ebtnAc.setChecked(False)
        self.ebtnAc.setAutoDefault(False)
        self.ebtnAc.setFlat(True)
        self.ebtnAc.setObjectName("ebtnAc")
        self.ebtnAl = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnAl.setGeometry(QtCore.QRect(590, 70, 29, 29))
        self.ebtnAl.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnAl.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnAl.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnAl.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnAl.setCheckable(True)
        self.ebtnAl.setAutoDefault(False)
        self.ebtnAl.setFlat(True)
        self.ebtnAl.setObjectName("ebtnAl")
        self.ebtnSr = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnSr.setGeometry(QtCore.QRect(260, 130, 29, 29))
        self.ebtnSr.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnSr.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnSr.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnSr.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnSr.setCheckable(True)
        self.ebtnSr.setAutoDefault(False)
        self.ebtnSr.setFlat(True)
        self.ebtnSr.setObjectName("ebtnSr")
        self.ebtnPo = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnPo.setGeometry(QtCore.QRect(680, 160, 29, 29))
        self.ebtnPo.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnPo.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnPo.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnPo.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnPo.setCheckable(True)
        self.ebtnPo.setAutoDefault(False)
        self.ebtnPo.setFlat(True)
        self.ebtnPo.setObjectName("ebtnPo")
        self.ebtnH = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnH.setGeometry(QtCore.QRect(230, 10, 29, 29))
        self.ebtnH.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnH.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnH.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnH.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnH.setCheckable(True)
        self.ebtnH.setAutoDefault(False)
        self.ebtnH.setFlat(True)
        self.ebtnH.setObjectName("ebtnH")
        self.ebtnMg = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnMg.setGeometry(QtCore.QRect(260, 70, 29, 29))
        self.ebtnMg.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnMg.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnMg.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnMg.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnMg.setCheckable(True)
        self.ebtnMg.setAutoDefault(False)
        self.ebtnMg.setFlat(True)
        self.ebtnMg.setObjectName("ebtnMg")
        self.ebtnNb = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnNb.setGeometry(QtCore.QRect(350, 130, 29, 29))
        self.ebtnNb.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnNb.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnNb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnNb.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnNb.setCheckable(True)
        self.ebtnNb.setAutoDefault(False)
        self.ebtnNb.setFlat(True)
        self.ebtnNb.setObjectName("ebtnNb")
        self.ebtnSe = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnSe.setGeometry(QtCore.QRect(680, 100, 29, 29))
        self.ebtnSe.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnSe.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnSe.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnSe.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnSe.setCheckable(True)
        self.ebtnSe.setAutoDefault(False)
        self.ebtnSe.setFlat(True)
        self.ebtnSe.setObjectName("ebtnSe")
        self.ebtnFm = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnFm.setGeometry(QtCore.QRect(650, 260, 29, 29))
        self.ebtnFm.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnFm.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnFm.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnFm.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnFm.setCheckable(True)
        self.ebtnFm.setAutoDefault(False)
        self.ebtnFm.setFlat(True)
        self.ebtnFm.setObjectName("ebtnFm")
        self.ebtnRu = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnRu.setGeometry(QtCore.QRect(440, 130, 29, 29))
        self.ebtnRu.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnRu.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnRu.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnRu.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnRu.setCheckable(True)
        self.ebtnRu.setAutoDefault(False)
        self.ebtnRu.setFlat(True)
        self.ebtnRu.setObjectName("ebtnRu")
        self.ebtnZr = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnZr.setGeometry(QtCore.QRect(320, 130, 29, 29))
        self.ebtnZr.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnZr.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnZr.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnZr.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnZr.setCheckable(True)
        self.ebtnZr.setAutoDefault(False)
        self.ebtnZr.setFlat(True)
        self.ebtnZr.setObjectName("ebtnZr")
        self.ebtnCm = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnCm.setGeometry(QtCore.QRect(530, 260, 29, 29))
        self.ebtnCm.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnCm.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnCm.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnCm.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnCm.setCheckable(True)
        self.ebtnCm.setAutoDefault(False)
        self.ebtnCm.setFlat(True)
        self.ebtnCm.setObjectName("ebtnCm")
        self.ebtnAm = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnAm.setGeometry(QtCore.QRect(500, 260, 29, 29))
        self.ebtnAm.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnAm.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnAm.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnAm.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnAm.setCheckable(True)
        self.ebtnAm.setAutoDefault(False)
        self.ebtnAm.setFlat(True)
        self.ebtnAm.setObjectName("ebtnAm")
        self.ebtnNo = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnNo.setGeometry(QtCore.QRect(710, 260, 29, 29))
        self.ebtnNo.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnNo.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnNo.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnNo.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnNo.setCheckable(True)
        self.ebtnNo.setAutoDefault(False)
        self.ebtnNo.setFlat(True)
        self.ebtnNo.setObjectName("ebtnNo")
        self.ebtnMt = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnMt.setGeometry(QtCore.QRect(470, 190, 29, 29))
        self.ebtnMt.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnMt.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnMt.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnMt.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnMt.setCheckable(True)
        self.ebtnMt.setAutoDefault(False)
        self.ebtnMt.setFlat(True)
        self.ebtnMt.setObjectName("ebtnMt")
        self.ebtnTh = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnTh.setGeometry(QtCore.QRect(350, 260, 29, 29))
        self.ebtnTh.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnTh.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnTh.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnTh.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnTh.setCheckable(True)
        self.ebtnTh.setAutoDefault(False)
        self.ebtnTh.setFlat(True)
        self.ebtnTh.setObjectName("ebtnTh")
        self.ebtnK = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnK.setGeometry(QtCore.QRect(230, 100, 29, 29))
        self.ebtnK.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnK.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnK.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnK.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnK.setCheckable(True)
        self.ebtnK.setAutoDefault(False)
        self.ebtnK.setFlat(True)
        self.ebtnK.setObjectName("ebtnK")
        self.ebtnMo = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnMo.setGeometry(QtCore.QRect(380, 130, 29, 29))
        self.ebtnMo.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnMo.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnMo.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnMo.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnMo.setCheckable(True)
        self.ebtnMo.setAutoDefault(False)
        self.ebtnMo.setFlat(True)
        self.ebtnMo.setObjectName("ebtnMo")
        self.ebtnF = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnF.setGeometry(QtCore.QRect(710, 40, 29, 29))
        self.ebtnF.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnF.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnF.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnF.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnF.setCheckable(True)
        self.ebtnF.setAutoDefault(False)
        self.ebtnF.setFlat(True)
        self.ebtnF.setObjectName("ebtnF")
        self.ebtnTc = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnTc.setGeometry(QtCore.QRect(410, 130, 29, 29))
        self.ebtnTc.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnTc.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnTc.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnTc.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnTc.setCheckable(True)
        self.ebtnTc.setAutoDefault(False)
        self.ebtnTc.setFlat(True)
        self.ebtnTc.setObjectName("ebtnTc")
        self.ebtnNe = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnNe.setGeometry(QtCore.QRect(740, 40, 29, 29))
        self.ebtnNe.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnNe.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnNe.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnNe.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnNe.setCheckable(True)
        self.ebtnNe.setAutoDefault(False)
        self.ebtnNe.setFlat(True)
        self.ebtnNe.setObjectName("ebtnNe")
        self.ebtnCo = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnCo.setGeometry(QtCore.QRect(470, 100, 29, 29))
        self.ebtnCo.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnCo.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnCo.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnCo.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnCo.setCheckable(True)
        self.ebtnCo.setAutoDefault(False)
        self.ebtnCo.setFlat(True)
        self.ebtnCo.setObjectName("ebtnCo")
        self.ebtnMd = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnMd.setGeometry(QtCore.QRect(680, 260, 29, 29))
        self.ebtnMd.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnMd.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnMd.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnMd.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnMd.setCheckable(True)
        self.ebtnMd.setAutoDefault(False)
        self.ebtnMd.setFlat(True)
        self.ebtnMd.setObjectName("ebtnMd")
        self.ebtnSb = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnSb.setGeometry(QtCore.QRect(650, 130, 29, 29))
        self.ebtnSb.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnSb.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnSb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnSb.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnSb.setCheckable(True)
        self.ebtnSb.setAutoDefault(False)
        self.ebtnSb.setFlat(True)
        self.ebtnSb.setObjectName("ebtnSb")
        self.ebtnTb = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnTb.setGeometry(QtCore.QRect(560, 230, 29, 29))
        self.ebtnTb.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnTb.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnTb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnTb.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnTb.setCheckable(True)
        self.ebtnTb.setAutoDefault(False)
        self.ebtnTb.setFlat(True)
        self.ebtnTb.setObjectName("ebtnTb")
        self.ebtnTm = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnTm.setGeometry(QtCore.QRect(680, 230, 29, 29))
        self.ebtnTm.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnTm.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnTm.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnTm.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnTm.setCheckable(True)
        self.ebtnTm.setAutoDefault(False)
        self.ebtnTm.setFlat(True)
        self.ebtnTm.setObjectName("ebtnTm")
        self.ebtnEr = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnEr.setGeometry(QtCore.QRect(650, 230, 29, 29))
        self.ebtnEr.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnEr.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnEr.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnEr.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnEr.setCheckable(True)
        self.ebtnEr.setAutoDefault(False)
        self.ebtnEr.setFlat(True)
        self.ebtnEr.setObjectName("ebtnEr")
        self.ebtnCl = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnCl.setGeometry(QtCore.QRect(710, 70, 29, 29))
        self.ebtnCl.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnCl.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnCl.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnCl.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnCl.setCheckable(True)
        self.ebtnCl.setAutoDefault(False)
        self.ebtnCl.setFlat(True)
        self.ebtnCl.setObjectName("ebtnCl")
        self.ebtnAt = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnAt.setGeometry(QtCore.QRect(710, 160, 29, 29))
        self.ebtnAt.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnAt.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnAt.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnAt.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnAt.setCheckable(True)
        self.ebtnAt.setAutoDefault(False)
        self.ebtnAt.setFlat(True)
        self.ebtnAt.setObjectName("ebtnAt")
        self.ebtnCr = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnCr.setGeometry(QtCore.QRect(380, 100, 29, 29))
        self.ebtnCr.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnCr.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnCr.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnCr.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnCr.setCheckable(True)
        self.ebtnCr.setAutoDefault(False)
        self.ebtnCr.setFlat(True)
        self.ebtnCr.setObjectName("ebtnCr")
        self.ebtnTa = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnTa.setGeometry(QtCore.QRect(350, 160, 29, 29))
        self.ebtnTa.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnTa.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnTa.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnTa.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnTa.setCheckable(True)
        self.ebtnTa.setAutoDefault(False)
        self.ebtnTa.setFlat(True)
        self.ebtnTa.setObjectName("ebtnTa")
        self.ebtnRh = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnRh.setGeometry(QtCore.QRect(470, 130, 29, 29))
        self.ebtnRh.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnRh.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnRh.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnRh.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnRh.setCheckable(True)
        self.ebtnRh.setAutoDefault(False)
        self.ebtnRh.setFlat(True)
        self.ebtnRh.setObjectName("ebtnRh")
        self.ebtnI = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnI.setGeometry(QtCore.QRect(710, 130, 29, 29))
        self.ebtnI.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnI.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnI.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnI.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnI.setCheckable(True)
        self.ebtnI.setAutoDefault(False)
        self.ebtnI.setFlat(True)
        self.ebtnI.setObjectName("ebtnI")
        self.ebtnTl = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnTl.setGeometry(QtCore.QRect(590, 160, 29, 29))
        self.ebtnTl.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnTl.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnTl.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnTl.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnTl.setCheckable(True)
        self.ebtnTl.setAutoDefault(False)
        self.ebtnTl.setFlat(True)
        self.ebtnTl.setObjectName("ebtnTl")
        self.ebtnSn = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnSn.setGeometry(QtCore.QRect(620, 130, 29, 29))
        self.ebtnSn.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnSn.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnSn.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnSn.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnSn.setCheckable(True)
        self.ebtnSn.setAutoDefault(False)
        self.ebtnSn.setFlat(True)
        self.ebtnSn.setObjectName("ebtnSn")
        self.ebtnPa = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnPa.setGeometry(QtCore.QRect(380, 260, 29, 29))
        self.ebtnPa.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnPa.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnPa.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnPa.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnPa.setCheckable(True)
        self.ebtnPa.setAutoDefault(False)
        self.ebtnPa.setFlat(True)
        self.ebtnPa.setObjectName("ebtnPa")
        self.ebtnAr = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnAr.setGeometry(QtCore.QRect(740, 70, 29, 29))
        self.ebtnAr.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnAr.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnAr.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnAr.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnAr.setCheckable(True)
        self.ebtnAr.setAutoDefault(False)
        self.ebtnAr.setFlat(True)
        self.ebtnAr.setObjectName("ebtnAr")
        self.ebtnSi = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnSi.setGeometry(QtCore.QRect(620, 70, 29, 29))
        self.ebtnSi.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnSi.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnSi.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnSi.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnSi.setCheckable(True)
        self.ebtnSi.setAutoDefault(False)
        self.ebtnSi.setFlat(True)
        self.ebtnSi.setObjectName("ebtnSi")
        self.ebtnSm = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnSm.setGeometry(QtCore.QRect(470, 230, 29, 29))
        self.ebtnSm.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnSm.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnSm.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnSm.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnSm.setCheckable(True)
        self.ebtnSm.setAutoDefault(False)
        self.ebtnSm.setFlat(True)
        self.ebtnSm.setObjectName("ebtnSm")
        self.ebtnFe = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnFe.setGeometry(QtCore.QRect(440, 100, 29, 29))
        self.ebtnFe.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnFe.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnFe.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnFe.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnFe.setCheckable(True)
        self.ebtnFe.setAutoDefault(False)
        self.ebtnFe.setFlat(True)
        self.ebtnFe.setObjectName("ebtnFe")
        self.ebtnKr = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnKr.setGeometry(QtCore.QRect(740, 100, 29, 29))
        self.ebtnKr.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnKr.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnKr.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnKr.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnKr.setCheckable(True)
        self.ebtnKr.setAutoDefault(False)
        self.ebtnKr.setFlat(True)
        self.ebtnKr.setObjectName("ebtnKr")
        self.ebtnBe = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnBe.setGeometry(QtCore.QRect(260, 40, 29, 29))
        self.ebtnBe.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnBe.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnBe.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnBe.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnBe.setCheckable(True)
        self.ebtnBe.setAutoDefault(False)
        self.ebtnBe.setFlat(True)
        self.ebtnBe.setObjectName("ebtnBe")
        self.ebtnRf = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnRf.setGeometry(QtCore.QRect(320, 190, 29, 29))
        self.ebtnRf.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnRf.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnRf.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnRf.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnRf.setCheckable(True)
        self.ebtnRf.setAutoDefault(False)
        self.ebtnRf.setFlat(True)
        self.ebtnRf.setObjectName("ebtnRf")
        self.ebtnLr = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnLr.setGeometry(QtCore.QRect(740, 260, 29, 29))
        self.ebtnLr.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnLr.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnLr.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnLr.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnLr.setCheckable(True)
        self.ebtnLr.setAutoDefault(False)
        self.ebtnLr.setFlat(True)
        self.ebtnLr.setObjectName("ebtnLr")
        self.ebtnSg = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnSg.setGeometry(QtCore.QRect(380, 190, 29, 29))
        self.ebtnSg.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnSg.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnSg.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnSg.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnSg.setCheckable(True)
        self.ebtnSg.setAutoDefault(False)
        self.ebtnSg.setFlat(True)
        self.ebtnSg.setObjectName("ebtnSg")
        self.ebtnHg = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnHg.setGeometry(QtCore.QRect(560, 160, 29, 29))
        self.ebtnHg.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnHg.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnHg.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnHg.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnHg.setCheckable(True)
        self.ebtnHg.setAutoDefault(False)
        self.ebtnHg.setFlat(True)
        self.ebtnHg.setObjectName("ebtnHg")
        self.ebtnAs = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnAs.setGeometry(QtCore.QRect(650, 100, 29, 29))
        self.ebtnAs.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnAs.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnAs.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnAs.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnAs.setCheckable(True)
        self.ebtnAs.setAutoDefault(False)
        self.ebtnAs.setFlat(True)
        self.ebtnAs.setObjectName("ebtnAs")
        self.ebtnCu = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnCu.setGeometry(QtCore.QRect(530, 100, 29, 29))
        self.ebtnCu.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnCu.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnCu.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnCu.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnCu.setCheckable(True)
        self.ebtnCu.setAutoDefault(False)
        self.ebtnCu.setFlat(True)
        self.ebtnCu.setObjectName("ebtnCu")
        self.ebtnCf = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnCf.setGeometry(QtCore.QRect(590, 260, 29, 29))
        self.ebtnCf.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnCf.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnCf.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnCf.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnCf.setCheckable(True)
        self.ebtnCf.setAutoDefault(False)
        self.ebtnCf.setFlat(True)
        self.ebtnCf.setObjectName("ebtnCf")
        self.ebtnTi = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnTi.setGeometry(QtCore.QRect(320, 100, 29, 29))
        self.ebtnTi.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnTi.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnTi.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnTi.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnTi.setCheckable(True)
        self.ebtnTi.setAutoDefault(False)
        self.ebtnTi.setFlat(True)
        self.ebtnTi.setObjectName("ebtnTi")
        self.ebtnDy = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnDy.setGeometry(QtCore.QRect(590, 230, 29, 29))
        self.ebtnDy.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnDy.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnDy.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnDy.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnDy.setCheckable(True)
        self.ebtnDy.setAutoDefault(False)
        self.ebtnDy.setFlat(True)
        self.ebtnDy.setObjectName("ebtnDy")
        self.ebtnPm = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnPm.setGeometry(QtCore.QRect(440, 230, 29, 29))
        self.ebtnPm.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnPm.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnPm.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnPm.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnPm.setCheckable(True)
        self.ebtnPm.setAutoDefault(False)
        self.ebtnPm.setFlat(True)
        self.ebtnPm.setObjectName("ebtnPm")
        self.ebtnAg = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnAg.setGeometry(QtCore.QRect(530, 130, 29, 29))
        self.ebtnAg.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnAg.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnAg.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnAg.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnAg.setCheckable(True)
        self.ebtnAg.setAutoDefault(False)
        self.ebtnAg.setFlat(True)
        self.ebtnAg.setObjectName("ebtnAg")
        self.ebtnZn = QtWidgets.QPushButton(BatchCalculationsPage)
        self.ebtnZn.setGeometry(QtCore.QRect(560, 100, 29, 29))
        self.ebtnZn.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnZn.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnZn.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnZn.setStyleSheet(
            "QPushButton {\n"
            "                    border: none;\n"
            "                    background-color: #1D2D44;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:hover{\n"
            "                    border: none;\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QPushButton:checked {\n"
            "                    border:none;\n"
            "                    background-color: #748CAB;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "                "
        )
        self.ebtnZn.setCheckable(True)
        self.ebtnZn.setAutoDefault(False)
        self.ebtnZn.setFlat(True)
        self.ebtnZn.setObjectName("ebtnZn")
        self.resultsTreeWidget = QtWidgets.QTreeWidget(BatchCalculationsPage)
        self.resultsTreeWidget.setGeometry(QtCore.QRect(10, 355, 971, 190))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resultsTreeWidget.sizePolicy().hasHeightForWidth())
        self.resultsTreeWidget.setSizePolicy(sizePolicy)
        self.resultsTreeWidget.setMinimumSize(QtCore.QSize(100, 0))
        self.resultsTreeWidget.setMaximumSize(QtCore.QSize(1000, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(QtGui.QFont.Weight.Normal)
        self.resultsTreeWidget.setFont(font)
        self.resultsTreeWidget.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.resultsTreeWidget.setStyleSheet(
            "QTreeWidget {\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QTreeWidget::item:selected{\n"
            "                    background-color: #3E5C76;\n"
            "                    color: #F0EBD8;\n"
            "                    }\n"
            "\n"
            "                    QHeaderView::section{\n"
            "                    color: #F0EBD8;\n"
            "                    background-color: #1D2D44;\n"
            "                    max-width: 30px;\n"
            "                    border: 0px solid;\n"
            "                    border-style: none;\n"
            "                    border-bottom: 0px solid;\n"
            "                    border-right: 1px solid rgb(53, 66, 87);\n"
            "                    }\n"
            "\n"
            "                    QHeaderView::section:horizontal\n"
            "                    {\n"
            "                    background-color: #1D2D44;\n"
            "                    border-bottom: 0px solid;\n"
            "                    }\n"
            "                    QHeaderView::section:vertical\n"
            "                    {\n"
            "                    border: 0px solid rgb(44, 49, 60);\n"
            "                    }\n"
            "\n"
            "                    QHeaderView::down-arrow {\n"
            "                    image: url(down_arrow_gray.png);\n"
            "                    }\n"
            "\n"
            "                    QHeaderView::up-arrow {\n"
            "                    }\n"
            "                "
        )
        self.resultsTreeWidget.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.resultsTreeWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.resultsTreeWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.resultsTreeWidget.setTabKeyNavigation(True)
        self.resultsTreeWidget.setProperty("showDropIndicator", False)
        self.resultsTreeWidget.setAlternatingRowColors(True)
        self.resultsTreeWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.resultsTreeWidget.setRootIsDecorated(False)
        self.resultsTreeWidget.setUniformRowHeights(True)
        self.resultsTreeWidget.setItemsExpandable(True)
        self.resultsTreeWidget.setAnimated(True)
        self.resultsTreeWidget.setAllColumnsShowFocus(False)
        self.resultsTreeWidget.setWordWrap(True)
        self.resultsTreeWidget.setHeaderHidden(False)
        self.resultsTreeWidget.setExpandsOnDoubleClick(True)
        self.resultsTreeWidget.setObjectName("resultsTreeWidget")
        for _col in range(23):
            self.resultsTreeWidget.headerItem().setTextAlignment(_col, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsTreeWidget.header().setVisible(True)
        self.resultsTreeWidget.header().setCascadingSectionResizes(False)
        self.resultsTreeWidget.header().setDefaultSectionSize(96)
        self.resultsTreeWidget.header().setHighlightSections(True)
        self.resultsTreeWidget.header().setMinimumSectionSize(15)
        self.resultsTreeWidget.header().setSortIndicatorShown(True)
        self.resultsTreeWidget.header().setStretchLastSection(True)
        _btn_style = (
            "QPushButton{background-color: #1D2D44;color: #F0EBD8;}"
            "QPushButton:hover{background-color: #3E5C76;color: #F0EBD8;}"
            "QPushButton:pressed{background-color: #748CAB;color: #F0EBD8;}"
        )
        _spinbox_style = ""
        _label_style = "QLabel{color: #F0EBD8; font-weight: bold;}"

        # Row 1: Start / End / Step labels + spinboxes
        self.lblStart = QtWidgets.QLabel(BatchCalculationsPage)
        self.lblStart.setGeometry(QtCore.QRect(10, 315, 40, 22))
        self.lblStart.setStyleSheet(_label_style)
        self.lblStart.setObjectName("lblStart")

        self.startSpinBox = QtWidgets.QDoubleSpinBox(BatchCalculationsPage)
        self.startSpinBox.setGeometry(QtCore.QRect(54, 312, 80, 28))
        self.startSpinBox.setRange(0.0, 100.0)
        self.startSpinBox.setSingleStep(5.0)
        self.startSpinBox.setValue(0.0)
        self.startSpinBox.setDecimals(1)
        self.startSpinBox.setSuffix(" %")
        self.startSpinBox.setStyleSheet(_spinbox_style)
        self.startSpinBox.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.startSpinBox.setObjectName("startSpinBox")

        self.lblEnd = QtWidgets.QLabel(BatchCalculationsPage)
        self.lblEnd.setGeometry(QtCore.QRect(145, 315, 32, 22))
        self.lblEnd.setStyleSheet(_label_style)
        self.lblEnd.setObjectName("lblEnd")

        self.endSpinBox = QtWidgets.QDoubleSpinBox(BatchCalculationsPage)
        self.endSpinBox.setGeometry(QtCore.QRect(181, 312, 80, 28))
        self.endSpinBox.setRange(0.0, 100.0)
        self.endSpinBox.setSingleStep(5.0)
        self.endSpinBox.setValue(100.0)
        self.endSpinBox.setDecimals(1)
        self.endSpinBox.setSuffix(" %")
        self.endSpinBox.setStyleSheet(_spinbox_style)
        self.endSpinBox.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.endSpinBox.setObjectName("endSpinBox")

        self.lblStep = QtWidgets.QLabel(BatchCalculationsPage)
        self.lblStep.setGeometry(QtCore.QRect(272, 315, 36, 22))
        self.lblStep.setStyleSheet(_label_style)
        self.lblStep.setObjectName("lblStep")

        self.stepSpinBox = QtWidgets.QDoubleSpinBox(BatchCalculationsPage)
        self.stepSpinBox.setGeometry(QtCore.QRect(312, 312, 80, 28))
        self.stepSpinBox.setRange(0.01, 100.0)
        self.stepSpinBox.setSingleStep(1.0)
        self.stepSpinBox.setValue(5.0)
        self.stepSpinBox.setDecimals(1)
        self.stepSpinBox.setSuffix(" %")
        self.stepSpinBox.setStyleSheet(_spinbox_style)
        self.stepSpinBox.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.stepSpinBox.setObjectName("stepSpinBox")

        # Row 2: Search / Clear / Save buttons
        self.btnSearch = QtWidgets.QPushButton(BatchCalculationsPage)
        self.btnSearch.setGeometry(QtCore.QRect(600, 312, 120, 28))
        self.btnSearch.setMinimumSize(QtCore.QSize(0, 28))
        self.btnSearch.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.btnSearch.setStyleSheet(_btn_style)
        self.btnSearch.setObjectName("btnSearch")

        self.btnClear = QtWidgets.QPushButton(BatchCalculationsPage)
        self.btnClear.setGeometry(QtCore.QRect(728, 312, 110, 28))
        self.btnClear.setMinimumSize(QtCore.QSize(0, 28))
        self.btnClear.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.btnClear.setStyleSheet(_btn_style)
        self.btnClear.setObjectName("btnClear")

        self.btnSave = QtWidgets.QPushButton(BatchCalculationsPage)
        self.btnSave.setGeometry(QtCore.QRect(846, 312, 138, 28))
        self.btnSave.setMinimumSize(QtCore.QSize(0, 28))
        self.btnSave.setEnabled(False)
        self.btnSave.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.btnSave.setStyleSheet(_btn_style)
        self.btnSave.setObjectName("btnSave")

        self.retranslateUi(BatchCalculationsPage)
        QtCore.QMetaObject.connectSlotsByName(BatchCalculationsPage)

    def retranslateUi(self, BatchCalculationsPage):
        """Set all translatable string properties on the child widgets.

        Called by ``setupUi`` after the widget hierarchy is fully built.
        Populates element button labels, input field placeholders, column
        headers, and action button captions through Qt's translation
        mechanism.

        Args:
            BatchCalculationsPage: The ``QWidget`` instance whose child text
                properties are being populated.
        """
        _translate = QtCore.QCoreApplication.translate
        BatchCalculationsPage.setWindowTitle(_translate("BatchCalculationsPage", "Form"))
        self.ebtnHe.setText(_translate("BatchCalculationsPage", "He"))
        self.ebtnRa.setText(_translate("BatchCalculationsPage", "Ra"))
        self.ebtnLu.setText(_translate("BatchCalculationsPage", "Lu"))
        self.ebtnGa.setText(_translate("BatchCalculationsPage", "Ga"))
        self.ebtnCa.setText(_translate("BatchCalculationsPage", "Ca"))
        self.ebtnAu.setText(_translate("BatchCalculationsPage", "Au"))
        self.ebtnLa.setText(_translate("BatchCalculationsPage", "La"))
        self.ebtnYb.setText(_translate("BatchCalculationsPage", "Yb"))
        self.ebtnW.setText(_translate("BatchCalculationsPage", "W"))
        self.ebtnBk.setText(_translate("BatchCalculationsPage", "Bk"))
        self.ebtnSc.setText(_translate("BatchCalculationsPage", "Sc"))
        self.ebtnNi.setText(_translate("BatchCalculationsPage", "Ni"))
        self.ebtnBa.setText(_translate("BatchCalculationsPage", "Ba"))
        self.ebtnBh.setText(_translate("BatchCalculationsPage", "Bh"))
        self.ebtnHs.setText(_translate("BatchCalculationsPage", "Hs"))
        self.ebtnHf.setText(_translate("BatchCalculationsPage", "Hf"))
        self.ebtnPr.setText(_translate("BatchCalculationsPage", "Pr"))
        self.ebtnV.setText(_translate("BatchCalculationsPage", "V"))
        self.ebtnN.setText(_translate("BatchCalculationsPage", "N"))
        self.ebtnFr.setText(_translate("BatchCalculationsPage", "Fr"))
        self.ebtnGd.setText(_translate("BatchCalculationsPage", "Gd"))
        self.ebtnO.setText(_translate("BatchCalculationsPage", "O"))
        self.ebtnPt.setText(_translate("BatchCalculationsPage", "Pt"))
        self.ebtnLi.setText(_translate("BatchCalculationsPage", "Li"))
        self.ebtnP.setText(_translate("BatchCalculationsPage", "P"))
        self.ebtnXe.setText(_translate("BatchCalculationsPage", "Xe"))
        self.ebtnPd.setText(_translate("BatchCalculationsPage", "Pd"))
        self.ebtnDb.setText(_translate("BatchCalculationsPage", "Db"))
        self.ebtnRb.setText(_translate("BatchCalculationsPage", "Rb"))
        self.ebtnBi.setText(_translate("BatchCalculationsPage", "Bi"))
        self.ebtnIn.setText(_translate("BatchCalculationsPage", "In"))
        self.ebtnS.setText(_translate("BatchCalculationsPage", "S"))
        self.ebtnAnd.setText(_translate("BatchCalculationsPage", "Nd"))
        self.ebtnNa.setText(_translate("BatchCalculationsPage", "Na"))
        self.ebtnIr.setText(_translate("BatchCalculationsPage", "Ir"))
        self.ebtnOs.setText(_translate("BatchCalculationsPage", "Os"))
        self.ebtnPu.setText(_translate("BatchCalculationsPage", "Pu"))
        self.ebtnTe.setText(_translate("BatchCalculationsPage", "Te"))
        self.ebtnEs.setText(_translate("BatchCalculationsPage", "Es"))
        self.ebtnCe.setText(_translate("BatchCalculationsPage", "Ce"))
        self.ebtnB.setText(_translate("BatchCalculationsPage", "B"))
        self.ebtnRe.setText(_translate("BatchCalculationsPage", "Re"))
        self.ebtnCs.setText(_translate("BatchCalculationsPage", "Cs"))
        self.ebtnCd.setText(_translate("BatchCalculationsPage", "Cd"))
        self.ebtnPb.setText(_translate("BatchCalculationsPage", "Pb"))
        self.ebtnRn.setText(_translate("BatchCalculationsPage", "Rn"))
        self.ebtnY.setText(_translate("BatchCalculationsPage", "Y"))
        self.ebtnU.setText(_translate("BatchCalculationsPage", "U"))
        self.ebtnBr.setText(_translate("BatchCalculationsPage", "Br"))
        self.ebtnC.setText(_translate("BatchCalculationsPage", "C"))
        self.ebtnHo.setText(_translate("BatchCalculationsPage", "Ho"))
        self.ebtnNp.setText(_translate("BatchCalculationsPage", "Np"))
        self.ebtnEu.setText(_translate("BatchCalculationsPage", "Eu"))
        self.ebtnMn.setText(_translate("BatchCalculationsPage", "Mn"))
        self.ebtnGe.setText(_translate("BatchCalculationsPage", "Ge"))
        self.ebtnAc.setText(_translate("BatchCalculationsPage", "Ac"))
        self.ebtnAl.setText(_translate("BatchCalculationsPage", "Al"))
        self.ebtnSr.setText(_translate("BatchCalculationsPage", "Sr"))
        self.ebtnPo.setText(_translate("BatchCalculationsPage", "Po"))
        self.ebtnH.setText(_translate("BatchCalculationsPage", "H"))
        self.ebtnMg.setText(_translate("BatchCalculationsPage", "Mg"))
        self.ebtnNb.setText(_translate("BatchCalculationsPage", "Nb"))
        self.ebtnSe.setText(_translate("BatchCalculationsPage", "Se"))
        self.ebtnFm.setText(_translate("BatchCalculationsPage", "Fm"))
        self.ebtnRu.setText(_translate("BatchCalculationsPage", "Ru"))
        self.ebtnZr.setText(_translate("BatchCalculationsPage", "Zr"))
        self.ebtnCm.setText(_translate("BatchCalculationsPage", "Cm"))
        self.ebtnAm.setText(_translate("BatchCalculationsPage", "Am"))
        self.ebtnNo.setText(_translate("BatchCalculationsPage", "No"))
        self.ebtnMt.setText(_translate("BatchCalculationsPage", "Mt"))
        self.ebtnTh.setText(_translate("BatchCalculationsPage", "Th"))
        self.ebtnK.setText(_translate("BatchCalculationsPage", "K"))
        self.ebtnMo.setText(_translate("BatchCalculationsPage", "Mo"))
        self.ebtnF.setText(_translate("BatchCalculationsPage", "F"))
        self.ebtnTc.setText(_translate("BatchCalculationsPage", "Tc"))
        self.ebtnNe.setText(_translate("BatchCalculationsPage", "Ne"))
        self.ebtnCo.setText(_translate("BatchCalculationsPage", "Co"))
        self.ebtnMd.setText(_translate("BatchCalculationsPage", "Md"))
        self.ebtnSb.setText(_translate("BatchCalculationsPage", "Sb"))
        self.ebtnTb.setText(_translate("BatchCalculationsPage", "Tb"))
        self.ebtnTm.setText(_translate("BatchCalculationsPage", "Tm"))
        self.ebtnEr.setText(_translate("BatchCalculationsPage", "Er"))
        self.ebtnCl.setText(_translate("BatchCalculationsPage", "Cl"))
        self.ebtnAt.setText(_translate("BatchCalculationsPage", "At"))
        self.ebtnCr.setText(_translate("BatchCalculationsPage", "Cr"))
        self.ebtnTa.setText(_translate("BatchCalculationsPage", "Ta"))
        self.ebtnRh.setText(_translate("BatchCalculationsPage", "Rh"))
        self.ebtnI.setText(_translate("BatchCalculationsPage", "I"))
        self.ebtnTl.setText(_translate("BatchCalculationsPage", "Tl"))
        self.ebtnSn.setText(_translate("BatchCalculationsPage", "Sn"))
        self.ebtnPa.setText(_translate("BatchCalculationsPage", "Pa"))
        self.ebtnAr.setText(_translate("BatchCalculationsPage", "Ar"))
        self.ebtnSi.setText(_translate("BatchCalculationsPage", "Si"))
        self.ebtnSm.setText(_translate("BatchCalculationsPage", "Sm"))
        self.ebtnFe.setText(_translate("BatchCalculationsPage", "Fe"))
        self.ebtnKr.setText(_translate("BatchCalculationsPage", "Kr"))
        self.ebtnBe.setText(_translate("BatchCalculationsPage", "Be"))
        self.ebtnRf.setText(_translate("BatchCalculationsPage", "Rf"))
        self.ebtnLr.setText(_translate("BatchCalculationsPage", "Lr"))
        self.ebtnSg.setText(_translate("BatchCalculationsPage", "Sg"))
        self.ebtnHg.setText(_translate("BatchCalculationsPage", "Hg"))
        self.ebtnAs.setText(_translate("BatchCalculationsPage", "As"))
        self.ebtnCu.setText(_translate("BatchCalculationsPage", "Cu"))
        self.ebtnCf.setText(_translate("BatchCalculationsPage", "Cf"))
        self.ebtnTi.setText(_translate("BatchCalculationsPage", "Ti"))
        self.ebtnDy.setText(_translate("BatchCalculationsPage", "Dy"))
        self.ebtnPm.setText(_translate("BatchCalculationsPage", "Pm"))
        self.ebtnAg.setText(_translate("BatchCalculationsPage", "Ag"))
        self.ebtnZn.setText(_translate("BatchCalculationsPage", "Zn"))
        self.resultsTreeWidget.setSortingEnabled(True)
        hi = self.resultsTreeWidget.headerItem()
        hi.setText(0, _translate("BatchCalculationsPage", "Formula"))
        hi.setText(1, _translate("BatchCalculationsPage", "Density"))
        hi.setToolTip(
            1,
            _translate(
                "BatchCalculationsPage",
                '<html><head/><body><p>g/cm<span style=" vertical-align:super;">3</span></p></body></html>',
            ),
        )
        hi.setText(2, _translate("BatchCalculationsPage", "\u03b4"))
        hi.setText(3, _translate("BatchCalculationsPage", "\u03b4 (CN12)"))
        hi.setText(4, _translate("BatchCalculationsPage", "\u0394\u03c7 (Allen)"))
        hi.setText(5, _translate("BatchCalculationsPage", "Omega"))
        hi.setText(6, _translate("BatchCalculationsPage", "Gamma"))
        hi.setToolTip(6, _translate("BatchCalculationsPage", "<html><head/><body><p>\u03b3</p></body></html>"))
        hi.setText(7, _translate("BatchCalculationsPage", "Lambda"))
        hi.setToolTip(7, _translate("BatchCalculationsPage", "<html><head/><body><p>\u03bb</p></body></html>"))
        hi.setText(8, _translate("BatchCalculationsPage", "VEC"))
        hi.setText(9, _translate("BatchCalculationsPage", "Mixing Enthalpy"))
        hi.setToolTip(9, _translate("BatchCalculationsPage", "<html><head/><body><p>kJ/mol</p></body></html>"))
        hi.setText(10, _translate("BatchCalculationsPage", "Mixing Entropy"))
        hi.setToolTip(10, _translate("BatchCalculationsPage", "<html><head/><body><p>J/K.mol</p></body></html>"))
        hi.setText(11, _translate("BatchCalculationsPage", "Formation Enthalpy"))
        hi.setToolTip(11, _translate("BatchCalculationsPage", "<html><head/><body><p>meV/atom</p></body></html>"))
        hi.setText(12, _translate("BatchCalculationsPage", "Min. Formation Enthalpy"))
        hi.setToolTip(12, _translate("BatchCalculationsPage", "<html><head/><body><p>meV/atom</p></body></html>"))
        hi.setText(13, _translate("BatchCalculationsPage", "Melting Temperature"))
        hi.setToolTip(13, _translate("BatchCalculationsPage", "<html><head/><body><p>K</p></body></html>"))
        hi.setText(14, _translate("BatchCalculationsPage", "Crystal Structure"))
        hi.setText(15, _translate("BatchCalculationsPage", "Model 1"))
        hi.setText(16, _translate("BatchCalculationsPage", "Model 2"))
        hi.setText(17, _translate("BatchCalculationsPage", "Model 3"))
        hi.setText(18, _translate("BatchCalculationsPage", "Model 4"))
        hi.setText(19, _translate("BatchCalculationsPage", "Model 5"))
        hi.setText(20, _translate("BatchCalculationsPage", "Model 6"))
        hi.setText(21, _translate("BatchCalculationsPage", "Model 7"))
        hi.setText(22, _translate("BatchCalculationsPage", "Model 8"))
        self.lblStart.setText(_translate("BatchCalculationsPage", "Start:"))
        self.lblEnd.setText(_translate("BatchCalculationsPage", "End:"))
        self.lblStep.setText(_translate("BatchCalculationsPage", "Step:"))
        self.btnSearch.setText(_translate("BatchCalculationsPage", "Search"))
        self.btnClear.setText(_translate("BatchCalculationsPage", "Clear"))
        self.btnSave.setText(_translate("BatchCalculationsPage", "Save CSV"))
