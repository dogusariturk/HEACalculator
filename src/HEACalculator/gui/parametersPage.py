"""Parameters page UI definition for HEACalculator.

Auto-generated from Qt Designer. Defines the single-alloy thermodynamic
parameters page: a periodic-table-style element selector grid, input fields
for custom compositions, a results table displaying computed HEA parameters
(mixing enthalpy/entropy, VEC, atomic size difference, omega, etc.), and
solid-solution prediction model outputs.
"""

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ParametersPage(object):
    """Qt Designer-generated UI class for the HEA Parameters page.

    Renders the interactive periodic table selector, composition inputs,
    and results table used for single-alloy thermodynamic calculations.
    """

    def setupUi(self, ParametersPage):
        """Create and arrange all child widgets inside *ParametersPage*.

        Builds the full periodic-table button grid (118 elements), the
        composition input area, the calculate/clear action buttons, and
        the results table. Applies the dark-theme stylesheet throughout.

        Args:
            ParametersPage: The ``QWidget`` instance that owns this UI.
        """
        ParametersPage.setObjectName("ParametersPage")
        ParametersPage.resize(1000, 658)
        ParametersPage.setMinimumSize(QtCore.QSize(1000, 300))
        ParametersPage.setMaximumSize(QtCore.QSize(1000, 9999))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(QtGui.QFont.Weight.Bold)
        ParametersPage.setFont(font)
        ParametersPage.setStyleSheet(
            "QWidget{\n"
            "    background-color: #0D1321;\n"
            "    alternate-background-color : rgb(24,30,43);\n"
            "}\n"
            "\n"
            "QToolTip { color: #F0EBD8; background-color: rgb(34,45,67); border: none; }"
        )
        self.ebtnHe = QtWidgets.QPushButton(ParametersPage)
        self.ebtnHe.setGeometry(QtCore.QRect(520, 10, 29, 29))
        self.ebtnHe.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnHe.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnHe.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnHe.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnHe.setCheckable(True)
        self.ebtnHe.setAutoDefault(False)
        self.ebtnHe.setFlat(True)
        self.ebtnHe.setObjectName("ebtnHe")
        self.ebtnRa = QtWidgets.QPushButton(ParametersPage)
        self.ebtnRa.setGeometry(QtCore.QRect(40, 190, 29, 29))
        self.ebtnRa.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnRa.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnRa.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnRa.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnRa.setCheckable(True)
        self.ebtnRa.setAutoDefault(False)
        self.ebtnRa.setFlat(True)
        self.ebtnRa.setObjectName("ebtnRa")
        self.ebtnLu = QtWidgets.QPushButton(ParametersPage)
        self.ebtnLu.setGeometry(QtCore.QRect(520, 230, 29, 29))
        self.ebtnLu.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnLu.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnLu.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnLu.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnLu.setCheckable(True)
        self.ebtnLu.setAutoDefault(False)
        self.ebtnLu.setFlat(True)
        self.ebtnLu.setObjectName("ebtnLu")
        self.ebtnGa = QtWidgets.QPushButton(ParametersPage)
        self.ebtnGa.setGeometry(QtCore.QRect(370, 100, 29, 29))
        self.ebtnGa.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnGa.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnGa.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnGa.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnGa.setCheckable(True)
        self.ebtnGa.setAutoDefault(False)
        self.ebtnGa.setFlat(True)
        self.ebtnGa.setObjectName("ebtnGa")
        self.ebtnCa = QtWidgets.QPushButton(ParametersPage)
        self.ebtnCa.setGeometry(QtCore.QRect(40, 100, 29, 29))
        self.ebtnCa.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnCa.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnCa.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnCa.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnCa.setCheckable(True)
        self.ebtnCa.setAutoDefault(False)
        self.ebtnCa.setFlat(True)
        self.ebtnCa.setObjectName("ebtnCa")
        self.ebtnAu = QtWidgets.QPushButton(ParametersPage)
        self.ebtnAu.setGeometry(QtCore.QRect(310, 160, 29, 29))
        self.ebtnAu.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnAu.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnAu.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnAu.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnAu.setCheckable(True)
        self.ebtnAu.setAutoDefault(False)
        self.ebtnAu.setFlat(True)
        self.ebtnAu.setObjectName("ebtnAu")
        self.ebtnLa = QtWidgets.QPushButton(ParametersPage)
        self.ebtnLa.setGeometry(QtCore.QRect(100, 230, 29, 29))
        self.ebtnLa.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnLa.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnLa.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnLa.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnLa.setCheckable(True)
        self.ebtnLa.setAutoDefault(False)
        self.ebtnLa.setFlat(True)
        self.ebtnLa.setObjectName("ebtnLa")
        self.ebtnYb = QtWidgets.QPushButton(ParametersPage)
        self.ebtnYb.setGeometry(QtCore.QRect(490, 230, 29, 29))
        self.ebtnYb.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnYb.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnYb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnYb.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnYb.setCheckable(True)
        self.ebtnYb.setAutoDefault(False)
        self.ebtnYb.setFlat(True)
        self.ebtnYb.setObjectName("ebtnYb")
        self.ebtnW = QtWidgets.QPushButton(ParametersPage)
        self.ebtnW.setGeometry(QtCore.QRect(160, 160, 29, 29))
        self.ebtnW.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnW.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnW.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnW.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnW.setCheckable(True)
        self.ebtnW.setAutoDefault(False)
        self.ebtnW.setFlat(True)
        self.ebtnW.setObjectName("ebtnW")
        self.ebtnBk = QtWidgets.QPushButton(ParametersPage)
        self.ebtnBk.setGeometry(QtCore.QRect(340, 260, 29, 29))
        self.ebtnBk.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnBk.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnBk.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnBk.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnBk.setCheckable(True)
        self.ebtnBk.setAutoDefault(False)
        self.ebtnBk.setFlat(True)
        self.ebtnBk.setObjectName("ebtnBk")
        self.ebtnSc = QtWidgets.QPushButton(ParametersPage)
        self.ebtnSc.setGeometry(QtCore.QRect(70, 100, 29, 29))
        self.ebtnSc.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnSc.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnSc.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnSc.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnSc.setCheckable(True)
        self.ebtnSc.setAutoDefault(False)
        self.ebtnSc.setFlat(True)
        self.ebtnSc.setObjectName("ebtnSc")
        self.ebtnNi = QtWidgets.QPushButton(ParametersPage)
        self.ebtnNi.setGeometry(QtCore.QRect(280, 100, 29, 29))
        self.ebtnNi.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnNi.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnNi.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnNi.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnNi.setCheckable(True)
        self.ebtnNi.setAutoDefault(False)
        self.ebtnNi.setFlat(True)
        self.ebtnNi.setObjectName("ebtnNi")
        self.ebtnBa = QtWidgets.QPushButton(ParametersPage)
        self.ebtnBa.setGeometry(QtCore.QRect(40, 160, 29, 29))
        self.ebtnBa.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnBa.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnBa.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnBa.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnBa.setCheckable(True)
        self.ebtnBa.setAutoDefault(False)
        self.ebtnBa.setFlat(True)
        self.ebtnBa.setObjectName("ebtnBa")
        self.ebtnBh = QtWidgets.QPushButton(ParametersPage)
        self.ebtnBh.setGeometry(QtCore.QRect(190, 190, 29, 29))
        self.ebtnBh.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnBh.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnBh.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnBh.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnBh.setCheckable(True)
        self.ebtnBh.setAutoDefault(False)
        self.ebtnBh.setFlat(True)
        self.ebtnBh.setObjectName("ebtnBh")
        self.ebtnHs = QtWidgets.QPushButton(ParametersPage)
        self.ebtnHs.setGeometry(QtCore.QRect(220, 190, 29, 29))
        self.ebtnHs.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnHs.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnHs.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnHs.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnHs.setCheckable(True)
        self.ebtnHs.setAutoDefault(False)
        self.ebtnHs.setFlat(True)
        self.ebtnHs.setObjectName("ebtnHs")
        self.ebtnHf = QtWidgets.QPushButton(ParametersPage)
        self.ebtnHf.setGeometry(QtCore.QRect(100, 160, 29, 29))
        self.ebtnHf.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnHf.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnHf.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnHf.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnHf.setCheckable(True)
        self.ebtnHf.setAutoDefault(False)
        self.ebtnHf.setFlat(True)
        self.ebtnHf.setObjectName("ebtnHf")
        self.ebtnPr = QtWidgets.QPushButton(ParametersPage)
        self.ebtnPr.setGeometry(QtCore.QRect(160, 230, 29, 29))
        self.ebtnPr.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnPr.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnPr.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnPr.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnPr.setCheckable(True)
        self.ebtnPr.setAutoDefault(False)
        self.ebtnPr.setFlat(True)
        self.ebtnPr.setObjectName("ebtnPr")
        self.ebtnV = QtWidgets.QPushButton(ParametersPage)
        self.ebtnV.setGeometry(QtCore.QRect(130, 100, 29, 29))
        self.ebtnV.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnV.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnV.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnV.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnV.setCheckable(True)
        self.ebtnV.setAutoDefault(False)
        self.ebtnV.setFlat(True)
        self.ebtnV.setObjectName("ebtnV")
        self.ebtnN = QtWidgets.QPushButton(ParametersPage)
        self.ebtnN.setGeometry(QtCore.QRect(430, 40, 29, 29))
        self.ebtnN.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnN.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnN.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnN.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnN.setCheckable(True)
        self.ebtnN.setAutoDefault(False)
        self.ebtnN.setFlat(True)
        self.ebtnN.setObjectName("ebtnN")
        self.ebtnFr = QtWidgets.QPushButton(ParametersPage)
        self.ebtnFr.setGeometry(QtCore.QRect(10, 190, 29, 29))
        self.ebtnFr.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnFr.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnFr.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnFr.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnFr.setCheckable(True)
        self.ebtnFr.setAutoDefault(False)
        self.ebtnFr.setFlat(True)
        self.ebtnFr.setObjectName("ebtnFr")
        self.ebtnGd = QtWidgets.QPushButton(ParametersPage)
        self.ebtnGd.setGeometry(QtCore.QRect(310, 230, 29, 29))
        self.ebtnGd.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnGd.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnGd.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnGd.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnGd.setCheckable(True)
        self.ebtnGd.setAutoDefault(False)
        self.ebtnGd.setFlat(True)
        self.ebtnGd.setObjectName("ebtnGd")
        self.ebtnO = QtWidgets.QPushButton(ParametersPage)
        self.ebtnO.setGeometry(QtCore.QRect(460, 40, 29, 29))
        self.ebtnO.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnO.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnO.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnO.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnO.setCheckable(True)
        self.ebtnO.setAutoDefault(False)
        self.ebtnO.setFlat(True)
        self.ebtnO.setObjectName("ebtnO")
        self.ebtnPt = QtWidgets.QPushButton(ParametersPage)
        self.ebtnPt.setGeometry(QtCore.QRect(280, 160, 29, 29))
        self.ebtnPt.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnPt.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnPt.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnPt.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnPt.setCheckable(True)
        self.ebtnPt.setAutoDefault(False)
        self.ebtnPt.setFlat(True)
        self.ebtnPt.setObjectName("ebtnPt")
        self.ebtnLi = QtWidgets.QPushButton(ParametersPage)
        self.ebtnLi.setGeometry(QtCore.QRect(10, 40, 29, 29))
        self.ebtnLi.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnLi.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnLi.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnLi.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnLi.setCheckable(True)
        self.ebtnLi.setAutoDefault(False)
        self.ebtnLi.setFlat(True)
        self.ebtnLi.setObjectName("ebtnLi")
        self.ebtnP = QtWidgets.QPushButton(ParametersPage)
        self.ebtnP.setGeometry(QtCore.QRect(430, 70, 29, 29))
        self.ebtnP.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnP.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnP.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnP.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnP.setCheckable(True)
        self.ebtnP.setAutoDefault(False)
        self.ebtnP.setFlat(True)
        self.ebtnP.setObjectName("ebtnP")
        self.ebtnXe = QtWidgets.QPushButton(ParametersPage)
        self.ebtnXe.setGeometry(QtCore.QRect(520, 130, 29, 29))
        self.ebtnXe.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnXe.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnXe.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnXe.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnXe.setCheckable(True)
        self.ebtnXe.setAutoDefault(False)
        self.ebtnXe.setFlat(True)
        self.ebtnXe.setObjectName("ebtnXe")
        self.ebtnPd = QtWidgets.QPushButton(ParametersPage)
        self.ebtnPd.setGeometry(QtCore.QRect(280, 130, 29, 29))
        self.ebtnPd.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnPd.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnPd.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnPd.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnPd.setCheckable(True)
        self.ebtnPd.setAutoDefault(False)
        self.ebtnPd.setFlat(True)
        self.ebtnPd.setObjectName("ebtnPd")
        self.ebtnDb = QtWidgets.QPushButton(ParametersPage)
        self.ebtnDb.setGeometry(QtCore.QRect(130, 190, 29, 29))
        self.ebtnDb.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnDb.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnDb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnDb.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnDb.setCheckable(True)
        self.ebtnDb.setAutoDefault(False)
        self.ebtnDb.setFlat(True)
        self.ebtnDb.setObjectName("ebtnDb")
        self.ebtnRb = QtWidgets.QPushButton(ParametersPage)
        self.ebtnRb.setGeometry(QtCore.QRect(10, 130, 29, 29))
        self.ebtnRb.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnRb.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnRb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnRb.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnRb.setCheckable(True)
        self.ebtnRb.setAutoDefault(False)
        self.ebtnRb.setFlat(True)
        self.ebtnRb.setObjectName("ebtnRb")
        self.ebtnBi = QtWidgets.QPushButton(ParametersPage)
        self.ebtnBi.setGeometry(QtCore.QRect(430, 160, 29, 29))
        self.ebtnBi.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnBi.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnBi.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnBi.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnBi.setCheckable(True)
        self.ebtnBi.setAutoDefault(False)
        self.ebtnBi.setFlat(True)
        self.ebtnBi.setObjectName("ebtnBi")
        self.ebtnIn = QtWidgets.QPushButton(ParametersPage)
        self.ebtnIn.setGeometry(QtCore.QRect(370, 130, 29, 29))
        self.ebtnIn.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnIn.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnIn.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnIn.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnIn.setCheckable(True)
        self.ebtnIn.setAutoDefault(False)
        self.ebtnIn.setFlat(True)
        self.ebtnIn.setObjectName("ebtnIn")
        self.ebtnS = QtWidgets.QPushButton(ParametersPage)
        self.ebtnS.setGeometry(QtCore.QRect(460, 70, 29, 29))
        self.ebtnS.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnS.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnS.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnS.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnS.setCheckable(True)
        self.ebtnS.setAutoDefault(False)
        self.ebtnS.setFlat(True)
        self.ebtnS.setObjectName("ebtnS")
        self.ebtnAnd = QtWidgets.QPushButton(ParametersPage)
        self.ebtnAnd.setGeometry(QtCore.QRect(190, 230, 29, 29))
        self.ebtnAnd.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnAnd.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnAnd.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnAnd.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnAnd.setCheckable(True)
        self.ebtnAnd.setAutoDefault(False)
        self.ebtnAnd.setFlat(True)
        self.ebtnAnd.setObjectName("ebtnAnd")
        self.ebtnNa = QtWidgets.QPushButton(ParametersPage)
        self.ebtnNa.setGeometry(QtCore.QRect(10, 70, 29, 29))
        self.ebtnNa.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnNa.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnNa.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnNa.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnNa.setCheckable(True)
        self.ebtnNa.setAutoDefault(False)
        self.ebtnNa.setFlat(True)
        self.ebtnNa.setObjectName("ebtnNa")
        self.ebtnIr = QtWidgets.QPushButton(ParametersPage)
        self.ebtnIr.setGeometry(QtCore.QRect(250, 160, 29, 29))
        self.ebtnIr.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnIr.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnIr.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnIr.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnIr.setCheckable(True)
        self.ebtnIr.setAutoDefault(False)
        self.ebtnIr.setFlat(True)
        self.ebtnIr.setObjectName("ebtnIr")
        self.ebtnOs = QtWidgets.QPushButton(ParametersPage)
        self.ebtnOs.setGeometry(QtCore.QRect(220, 160, 29, 29))
        self.ebtnOs.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnOs.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnOs.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnOs.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnOs.setCheckable(True)
        self.ebtnOs.setAutoDefault(False)
        self.ebtnOs.setFlat(True)
        self.ebtnOs.setObjectName("ebtnOs")
        self.ebtnPu = QtWidgets.QPushButton(ParametersPage)
        self.ebtnPu.setGeometry(QtCore.QRect(250, 260, 29, 29))
        self.ebtnPu.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnPu.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnPu.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnPu.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnPu.setCheckable(True)
        self.ebtnPu.setAutoDefault(False)
        self.ebtnPu.setFlat(True)
        self.ebtnPu.setObjectName("ebtnPu")
        self.ebtnTe = QtWidgets.QPushButton(ParametersPage)
        self.ebtnTe.setGeometry(QtCore.QRect(460, 130, 29, 29))
        self.ebtnTe.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnTe.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnTe.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnTe.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnTe.setCheckable(True)
        self.ebtnTe.setAutoDefault(False)
        self.ebtnTe.setFlat(True)
        self.ebtnTe.setObjectName("ebtnTe")
        self.ebtnEs = QtWidgets.QPushButton(ParametersPage)
        self.ebtnEs.setGeometry(QtCore.QRect(400, 260, 29, 29))
        self.ebtnEs.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnEs.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnEs.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnEs.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnEs.setCheckable(True)
        self.ebtnEs.setAutoDefault(False)
        self.ebtnEs.setFlat(True)
        self.ebtnEs.setObjectName("ebtnEs")
        self.ebtnCe = QtWidgets.QPushButton(ParametersPage)
        self.ebtnCe.setGeometry(QtCore.QRect(130, 230, 29, 29))
        self.ebtnCe.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnCe.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnCe.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnCe.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnCe.setCheckable(True)
        self.ebtnCe.setAutoDefault(False)
        self.ebtnCe.setFlat(True)
        self.ebtnCe.setObjectName("ebtnCe")
        self.ebtnB = QtWidgets.QPushButton(ParametersPage)
        self.ebtnB.setGeometry(QtCore.QRect(370, 40, 29, 29))
        self.ebtnB.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnB.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnB.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnB.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnB.setCheckable(True)
        self.ebtnB.setAutoDefault(False)
        self.ebtnB.setFlat(True)
        self.ebtnB.setObjectName("ebtnB")
        self.ebtnRe = QtWidgets.QPushButton(ParametersPage)
        self.ebtnRe.setGeometry(QtCore.QRect(190, 160, 29, 29))
        self.ebtnRe.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnRe.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnRe.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnRe.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnRe.setCheckable(True)
        self.ebtnRe.setAutoDefault(False)
        self.ebtnRe.setFlat(True)
        self.ebtnRe.setObjectName("ebtnRe")
        self.ebtnCs = QtWidgets.QPushButton(ParametersPage)
        self.ebtnCs.setGeometry(QtCore.QRect(10, 160, 29, 29))
        self.ebtnCs.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnCs.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnCs.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnCs.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnCs.setCheckable(True)
        self.ebtnCs.setAutoDefault(False)
        self.ebtnCs.setFlat(True)
        self.ebtnCs.setObjectName("ebtnCs")
        self.ebtnCd = QtWidgets.QPushButton(ParametersPage)
        self.ebtnCd.setGeometry(QtCore.QRect(340, 130, 29, 29))
        self.ebtnCd.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnCd.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnCd.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnCd.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnCd.setCheckable(True)
        self.ebtnCd.setAutoDefault(False)
        self.ebtnCd.setFlat(True)
        self.ebtnCd.setObjectName("ebtnCd")
        self.ebtnPb = QtWidgets.QPushButton(ParametersPage)
        self.ebtnPb.setGeometry(QtCore.QRect(400, 160, 29, 29))
        self.ebtnPb.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnPb.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnPb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnPb.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnPb.setCheckable(True)
        self.ebtnPb.setAutoDefault(False)
        self.ebtnPb.setFlat(True)
        self.ebtnPb.setObjectName("ebtnPb")
        self.ebtnRn = QtWidgets.QPushButton(ParametersPage)
        self.ebtnRn.setGeometry(QtCore.QRect(520, 160, 29, 29))
        self.ebtnRn.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnRn.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnRn.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnRn.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnRn.setCheckable(True)
        self.ebtnRn.setAutoDefault(False)
        self.ebtnRn.setFlat(True)
        self.ebtnRn.setObjectName("ebtnRn")
        self.ebtnY = QtWidgets.QPushButton(ParametersPage)
        self.ebtnY.setGeometry(QtCore.QRect(70, 130, 29, 29))
        self.ebtnY.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnY.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnY.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnY.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnY.setCheckable(True)
        self.ebtnY.setAutoDefault(False)
        self.ebtnY.setFlat(True)
        self.ebtnY.setObjectName("ebtnY")
        self.ebtnU = QtWidgets.QPushButton(ParametersPage)
        self.ebtnU.setGeometry(QtCore.QRect(190, 260, 29, 29))
        self.ebtnU.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnU.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnU.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnU.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnU.setCheckable(True)
        self.ebtnU.setAutoDefault(False)
        self.ebtnU.setFlat(True)
        self.ebtnU.setObjectName("ebtnU")
        self.ebtnBr = QtWidgets.QPushButton(ParametersPage)
        self.ebtnBr.setGeometry(QtCore.QRect(490, 100, 29, 29))
        self.ebtnBr.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnBr.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnBr.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnBr.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnBr.setCheckable(True)
        self.ebtnBr.setAutoDefault(False)
        self.ebtnBr.setFlat(True)
        self.ebtnBr.setObjectName("ebtnBr")
        self.ebtnC = QtWidgets.QPushButton(ParametersPage)
        self.ebtnC.setGeometry(QtCore.QRect(400, 40, 29, 29))
        self.ebtnC.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnC.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnC.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnC.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnC.setCheckable(True)
        self.ebtnC.setAutoDefault(False)
        self.ebtnC.setFlat(True)
        self.ebtnC.setObjectName("ebtnC")
        self.ebtnHo = QtWidgets.QPushButton(ParametersPage)
        self.ebtnHo.setGeometry(QtCore.QRect(400, 230, 29, 29))
        self.ebtnHo.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnHo.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnHo.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnHo.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnHo.setCheckable(True)
        self.ebtnHo.setAutoDefault(False)
        self.ebtnHo.setFlat(True)
        self.ebtnHo.setObjectName("ebtnHo")
        self.ebtnNp = QtWidgets.QPushButton(ParametersPage)
        self.ebtnNp.setGeometry(QtCore.QRect(220, 260, 29, 29))
        self.ebtnNp.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnNp.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnNp.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnNp.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnNp.setCheckable(True)
        self.ebtnNp.setAutoDefault(False)
        self.ebtnNp.setFlat(True)
        self.ebtnNp.setObjectName("ebtnNp")
        self.ebtnEu = QtWidgets.QPushButton(ParametersPage)
        self.ebtnEu.setGeometry(QtCore.QRect(280, 230, 29, 29))
        self.ebtnEu.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnEu.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnEu.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnEu.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnEu.setCheckable(True)
        self.ebtnEu.setAutoDefault(False)
        self.ebtnEu.setFlat(True)
        self.ebtnEu.setObjectName("ebtnEu")
        self.ebtnMn = QtWidgets.QPushButton(ParametersPage)
        self.ebtnMn.setGeometry(QtCore.QRect(190, 100, 29, 29))
        self.ebtnMn.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnMn.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnMn.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnMn.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnMn.setCheckable(True)
        self.ebtnMn.setAutoDefault(False)
        self.ebtnMn.setFlat(True)
        self.ebtnMn.setObjectName("ebtnMn")
        self.ebtnGe = QtWidgets.QPushButton(ParametersPage)
        self.ebtnGe.setGeometry(QtCore.QRect(400, 100, 29, 29))
        self.ebtnGe.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnGe.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnGe.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnGe.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnGe.setCheckable(True)
        self.ebtnGe.setAutoDefault(False)
        self.ebtnGe.setFlat(True)
        self.ebtnGe.setObjectName("ebtnGe")
        self.ebtnAc = QtWidgets.QPushButton(ParametersPage)
        self.ebtnAc.setEnabled(True)
        self.ebtnAc.setGeometry(QtCore.QRect(100, 260, 29, 29))
        self.ebtnAc.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnAc.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnAc.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnAc.setAcceptDrops(False)
        self.ebtnAc.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnAc.setCheckable(True)
        self.ebtnAc.setChecked(False)
        self.ebtnAc.setAutoDefault(False)
        self.ebtnAc.setFlat(True)
        self.ebtnAc.setObjectName("ebtnAc")
        self.ebtnAl = QtWidgets.QPushButton(ParametersPage)
        self.ebtnAl.setGeometry(QtCore.QRect(370, 70, 29, 29))
        self.ebtnAl.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnAl.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnAl.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnAl.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnAl.setCheckable(True)
        self.ebtnAl.setAutoDefault(False)
        self.ebtnAl.setFlat(True)
        self.ebtnAl.setObjectName("ebtnAl")
        self.ebtnSr = QtWidgets.QPushButton(ParametersPage)
        self.ebtnSr.setGeometry(QtCore.QRect(40, 130, 29, 29))
        self.ebtnSr.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnSr.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnSr.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnSr.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnSr.setCheckable(True)
        self.ebtnSr.setAutoDefault(False)
        self.ebtnSr.setFlat(True)
        self.ebtnSr.setObjectName("ebtnSr")
        self.ebtnPo = QtWidgets.QPushButton(ParametersPage)
        self.ebtnPo.setGeometry(QtCore.QRect(460, 160, 29, 29))
        self.ebtnPo.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnPo.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnPo.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnPo.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnPo.setCheckable(True)
        self.ebtnPo.setAutoDefault(False)
        self.ebtnPo.setFlat(True)
        self.ebtnPo.setObjectName("ebtnPo")
        self.ebtnH = QtWidgets.QPushButton(ParametersPage)
        self.ebtnH.setGeometry(QtCore.QRect(10, 10, 29, 29))
        self.ebtnH.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnH.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnH.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnH.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnH.setCheckable(True)
        self.ebtnH.setAutoDefault(False)
        self.ebtnH.setFlat(True)
        self.ebtnH.setObjectName("ebtnH")
        self.ebtnMg = QtWidgets.QPushButton(ParametersPage)
        self.ebtnMg.setGeometry(QtCore.QRect(40, 70, 29, 29))
        self.ebtnMg.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnMg.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnMg.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnMg.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnMg.setCheckable(True)
        self.ebtnMg.setAutoDefault(False)
        self.ebtnMg.setFlat(True)
        self.ebtnMg.setObjectName("ebtnMg")
        self.ebtnNb = QtWidgets.QPushButton(ParametersPage)
        self.ebtnNb.setGeometry(QtCore.QRect(130, 130, 29, 29))
        self.ebtnNb.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnNb.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnNb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnNb.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnNb.setCheckable(True)
        self.ebtnNb.setAutoDefault(False)
        self.ebtnNb.setFlat(True)
        self.ebtnNb.setObjectName("ebtnNb")
        self.ebtnSe = QtWidgets.QPushButton(ParametersPage)
        self.ebtnSe.setGeometry(QtCore.QRect(460, 100, 29, 29))
        self.ebtnSe.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnSe.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnSe.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnSe.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnSe.setCheckable(True)
        self.ebtnSe.setAutoDefault(False)
        self.ebtnSe.setFlat(True)
        self.ebtnSe.setObjectName("ebtnSe")
        self.ebtnFm = QtWidgets.QPushButton(ParametersPage)
        self.ebtnFm.setGeometry(QtCore.QRect(430, 260, 29, 29))
        self.ebtnFm.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnFm.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnFm.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnFm.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnFm.setCheckable(True)
        self.ebtnFm.setAutoDefault(False)
        self.ebtnFm.setFlat(True)
        self.ebtnFm.setObjectName("ebtnFm")
        self.ebtnRu = QtWidgets.QPushButton(ParametersPage)
        self.ebtnRu.setGeometry(QtCore.QRect(220, 130, 29, 29))
        self.ebtnRu.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnRu.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnRu.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnRu.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnRu.setCheckable(True)
        self.ebtnRu.setAutoDefault(False)
        self.ebtnRu.setFlat(True)
        self.ebtnRu.setObjectName("ebtnRu")
        self.ebtnZr = QtWidgets.QPushButton(ParametersPage)
        self.ebtnZr.setGeometry(QtCore.QRect(100, 130, 29, 29))
        self.ebtnZr.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnZr.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnZr.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnZr.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnZr.setCheckable(True)
        self.ebtnZr.setAutoDefault(False)
        self.ebtnZr.setFlat(True)
        self.ebtnZr.setObjectName("ebtnZr")
        self.ebtnCm = QtWidgets.QPushButton(ParametersPage)
        self.ebtnCm.setGeometry(QtCore.QRect(310, 260, 29, 29))
        self.ebtnCm.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnCm.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnCm.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnCm.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnCm.setCheckable(True)
        self.ebtnCm.setAutoDefault(False)
        self.ebtnCm.setFlat(True)
        self.ebtnCm.setObjectName("ebtnCm")
        self.ebtnAm = QtWidgets.QPushButton(ParametersPage)
        self.ebtnAm.setGeometry(QtCore.QRect(280, 260, 29, 29))
        self.ebtnAm.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnAm.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnAm.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnAm.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnAm.setCheckable(True)
        self.ebtnAm.setAutoDefault(False)
        self.ebtnAm.setFlat(True)
        self.ebtnAm.setObjectName("ebtnAm")
        self.ebtnNo = QtWidgets.QPushButton(ParametersPage)
        self.ebtnNo.setGeometry(QtCore.QRect(490, 260, 29, 29))
        self.ebtnNo.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnNo.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnNo.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnNo.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnNo.setCheckable(True)
        self.ebtnNo.setAutoDefault(False)
        self.ebtnNo.setFlat(True)
        self.ebtnNo.setObjectName("ebtnNo")
        self.ebtnMt = QtWidgets.QPushButton(ParametersPage)
        self.ebtnMt.setGeometry(QtCore.QRect(250, 190, 29, 29))
        self.ebtnMt.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnMt.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnMt.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnMt.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnMt.setCheckable(True)
        self.ebtnMt.setAutoDefault(False)
        self.ebtnMt.setFlat(True)
        self.ebtnMt.setObjectName("ebtnMt")
        self.ebtnTh = QtWidgets.QPushButton(ParametersPage)
        self.ebtnTh.setGeometry(QtCore.QRect(130, 260, 29, 29))
        self.ebtnTh.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnTh.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnTh.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnTh.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnTh.setCheckable(True)
        self.ebtnTh.setAutoDefault(False)
        self.ebtnTh.setFlat(True)
        self.ebtnTh.setObjectName("ebtnTh")
        self.ebtnK = QtWidgets.QPushButton(ParametersPage)
        self.ebtnK.setGeometry(QtCore.QRect(10, 100, 29, 29))
        self.ebtnK.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnK.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnK.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnK.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnK.setCheckable(True)
        self.ebtnK.setAutoDefault(False)
        self.ebtnK.setFlat(True)
        self.ebtnK.setObjectName("ebtnK")
        self.ebtnMo = QtWidgets.QPushButton(ParametersPage)
        self.ebtnMo.setGeometry(QtCore.QRect(160, 130, 29, 29))
        self.ebtnMo.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnMo.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnMo.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnMo.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnMo.setCheckable(True)
        self.ebtnMo.setAutoDefault(False)
        self.ebtnMo.setFlat(True)
        self.ebtnMo.setObjectName("ebtnMo")
        self.ebtnF = QtWidgets.QPushButton(ParametersPage)
        self.ebtnF.setGeometry(QtCore.QRect(490, 40, 29, 29))
        self.ebtnF.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnF.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnF.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnF.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnF.setCheckable(True)
        self.ebtnF.setAutoDefault(False)
        self.ebtnF.setFlat(True)
        self.ebtnF.setObjectName("ebtnF")
        self.ebtnTc = QtWidgets.QPushButton(ParametersPage)
        self.ebtnTc.setGeometry(QtCore.QRect(190, 130, 29, 29))
        self.ebtnTc.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnTc.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnTc.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnTc.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnTc.setCheckable(True)
        self.ebtnTc.setAutoDefault(False)
        self.ebtnTc.setFlat(True)
        self.ebtnTc.setObjectName("ebtnTc")
        self.ebtnNe = QtWidgets.QPushButton(ParametersPage)
        self.ebtnNe.setGeometry(QtCore.QRect(520, 40, 29, 29))
        self.ebtnNe.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnNe.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnNe.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnNe.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnNe.setCheckable(True)
        self.ebtnNe.setAutoDefault(False)
        self.ebtnNe.setFlat(True)
        self.ebtnNe.setObjectName("ebtnNe")
        self.ebtnCo = QtWidgets.QPushButton(ParametersPage)
        self.ebtnCo.setGeometry(QtCore.QRect(250, 100, 29, 29))
        self.ebtnCo.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnCo.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnCo.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnCo.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnCo.setCheckable(True)
        self.ebtnCo.setAutoDefault(False)
        self.ebtnCo.setFlat(True)
        self.ebtnCo.setObjectName("ebtnCo")
        self.ebtnMd = QtWidgets.QPushButton(ParametersPage)
        self.ebtnMd.setGeometry(QtCore.QRect(460, 260, 29, 29))
        self.ebtnMd.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnMd.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnMd.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnMd.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnMd.setCheckable(True)
        self.ebtnMd.setAutoDefault(False)
        self.ebtnMd.setFlat(True)
        self.ebtnMd.setObjectName("ebtnMd")
        self.ebtnSb = QtWidgets.QPushButton(ParametersPage)
        self.ebtnSb.setGeometry(QtCore.QRect(430, 130, 29, 29))
        self.ebtnSb.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnSb.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnSb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnSb.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnSb.setCheckable(True)
        self.ebtnSb.setAutoDefault(False)
        self.ebtnSb.setFlat(True)
        self.ebtnSb.setObjectName("ebtnSb")
        self.ebtnTb = QtWidgets.QPushButton(ParametersPage)
        self.ebtnTb.setGeometry(QtCore.QRect(340, 230, 29, 29))
        self.ebtnTb.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnTb.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnTb.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnTb.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnTb.setCheckable(True)
        self.ebtnTb.setAutoDefault(False)
        self.ebtnTb.setFlat(True)
        self.ebtnTb.setObjectName("ebtnTb")
        self.ebtnTm = QtWidgets.QPushButton(ParametersPage)
        self.ebtnTm.setGeometry(QtCore.QRect(460, 230, 29, 29))
        self.ebtnTm.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnTm.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnTm.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnTm.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnTm.setCheckable(True)
        self.ebtnTm.setAutoDefault(False)
        self.ebtnTm.setFlat(True)
        self.ebtnTm.setObjectName("ebtnTm")
        self.ebtnEr = QtWidgets.QPushButton(ParametersPage)
        self.ebtnEr.setGeometry(QtCore.QRect(430, 230, 29, 29))
        self.ebtnEr.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnEr.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnEr.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnEr.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnEr.setCheckable(True)
        self.ebtnEr.setAutoDefault(False)
        self.ebtnEr.setFlat(True)
        self.ebtnEr.setObjectName("ebtnEr")
        self.ebtnCl = QtWidgets.QPushButton(ParametersPage)
        self.ebtnCl.setGeometry(QtCore.QRect(490, 70, 29, 29))
        self.ebtnCl.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnCl.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnCl.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnCl.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnCl.setCheckable(True)
        self.ebtnCl.setAutoDefault(False)
        self.ebtnCl.setFlat(True)
        self.ebtnCl.setObjectName("ebtnCl")
        self.ebtnAt = QtWidgets.QPushButton(ParametersPage)
        self.ebtnAt.setGeometry(QtCore.QRect(490, 160, 29, 29))
        self.ebtnAt.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnAt.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnAt.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnAt.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnAt.setCheckable(True)
        self.ebtnAt.setAutoDefault(False)
        self.ebtnAt.setFlat(True)
        self.ebtnAt.setObjectName("ebtnAt")
        self.ebtnCr = QtWidgets.QPushButton(ParametersPage)
        self.ebtnCr.setGeometry(QtCore.QRect(160, 100, 29, 29))
        self.ebtnCr.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnCr.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnCr.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnCr.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnCr.setCheckable(True)
        self.ebtnCr.setAutoDefault(False)
        self.ebtnCr.setFlat(True)
        self.ebtnCr.setObjectName("ebtnCr")
        self.ebtnTa = QtWidgets.QPushButton(ParametersPage)
        self.ebtnTa.setGeometry(QtCore.QRect(130, 160, 29, 29))
        self.ebtnTa.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnTa.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnTa.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnTa.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnTa.setCheckable(True)
        self.ebtnTa.setAutoDefault(False)
        self.ebtnTa.setFlat(True)
        self.ebtnTa.setObjectName("ebtnTa")
        self.ebtnRh = QtWidgets.QPushButton(ParametersPage)
        self.ebtnRh.setGeometry(QtCore.QRect(250, 130, 29, 29))
        self.ebtnRh.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnRh.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnRh.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnRh.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnRh.setCheckable(True)
        self.ebtnRh.setAutoDefault(False)
        self.ebtnRh.setFlat(True)
        self.ebtnRh.setObjectName("ebtnRh")
        self.ebtnI = QtWidgets.QPushButton(ParametersPage)
        self.ebtnI.setGeometry(QtCore.QRect(490, 130, 29, 29))
        self.ebtnI.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnI.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnI.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnI.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnI.setCheckable(True)
        self.ebtnI.setAutoDefault(False)
        self.ebtnI.setFlat(True)
        self.ebtnI.setObjectName("ebtnI")
        self.ebtnTl = QtWidgets.QPushButton(ParametersPage)
        self.ebtnTl.setGeometry(QtCore.QRect(370, 160, 29, 29))
        self.ebtnTl.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnTl.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnTl.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnTl.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnTl.setCheckable(True)
        self.ebtnTl.setAutoDefault(False)
        self.ebtnTl.setFlat(True)
        self.ebtnTl.setObjectName("ebtnTl")
        self.ebtnSn = QtWidgets.QPushButton(ParametersPage)
        self.ebtnSn.setGeometry(QtCore.QRect(400, 130, 29, 29))
        self.ebtnSn.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnSn.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnSn.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnSn.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnSn.setCheckable(True)
        self.ebtnSn.setAutoDefault(False)
        self.ebtnSn.setFlat(True)
        self.ebtnSn.setObjectName("ebtnSn")
        self.ebtnPa = QtWidgets.QPushButton(ParametersPage)
        self.ebtnPa.setGeometry(QtCore.QRect(160, 260, 29, 29))
        self.ebtnPa.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnPa.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnPa.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnPa.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnPa.setCheckable(True)
        self.ebtnPa.setAutoDefault(False)
        self.ebtnPa.setFlat(True)
        self.ebtnPa.setObjectName("ebtnPa")
        self.ebtnAr = QtWidgets.QPushButton(ParametersPage)
        self.ebtnAr.setGeometry(QtCore.QRect(520, 70, 29, 29))
        self.ebtnAr.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnAr.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnAr.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnAr.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnAr.setCheckable(True)
        self.ebtnAr.setAutoDefault(False)
        self.ebtnAr.setFlat(True)
        self.ebtnAr.setObjectName("ebtnAr")
        self.ebtnSi = QtWidgets.QPushButton(ParametersPage)
        self.ebtnSi.setGeometry(QtCore.QRect(400, 70, 29, 29))
        self.ebtnSi.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnSi.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnSi.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnSi.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnSi.setCheckable(True)
        self.ebtnSi.setAutoDefault(False)
        self.ebtnSi.setFlat(True)
        self.ebtnSi.setObjectName("ebtnSi")
        self.ebtnSm = QtWidgets.QPushButton(ParametersPage)
        self.ebtnSm.setGeometry(QtCore.QRect(250, 230, 29, 29))
        self.ebtnSm.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnSm.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnSm.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnSm.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnSm.setCheckable(True)
        self.ebtnSm.setAutoDefault(False)
        self.ebtnSm.setFlat(True)
        self.ebtnSm.setObjectName("ebtnSm")
        self.ebtnFe = QtWidgets.QPushButton(ParametersPage)
        self.ebtnFe.setGeometry(QtCore.QRect(220, 100, 29, 29))
        self.ebtnFe.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnFe.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnFe.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnFe.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnFe.setCheckable(True)
        self.ebtnFe.setAutoDefault(False)
        self.ebtnFe.setFlat(True)
        self.ebtnFe.setObjectName("ebtnFe")
        self.ebtnKr = QtWidgets.QPushButton(ParametersPage)
        self.ebtnKr.setGeometry(QtCore.QRect(520, 100, 29, 29))
        self.ebtnKr.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnKr.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnKr.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnKr.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnKr.setCheckable(True)
        self.ebtnKr.setAutoDefault(False)
        self.ebtnKr.setFlat(True)
        self.ebtnKr.setObjectName("ebtnKr")
        self.ebtnBe = QtWidgets.QPushButton(ParametersPage)
        self.ebtnBe.setGeometry(QtCore.QRect(40, 40, 29, 29))
        self.ebtnBe.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnBe.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnBe.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnBe.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnBe.setCheckable(True)
        self.ebtnBe.setAutoDefault(False)
        self.ebtnBe.setFlat(True)
        self.ebtnBe.setObjectName("ebtnBe")
        self.ebtnRf = QtWidgets.QPushButton(ParametersPage)
        self.ebtnRf.setGeometry(QtCore.QRect(100, 190, 29, 29))
        self.ebtnRf.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnRf.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnRf.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnRf.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnRf.setCheckable(True)
        self.ebtnRf.setAutoDefault(False)
        self.ebtnRf.setFlat(True)
        self.ebtnRf.setObjectName("ebtnRf")
        self.ebtnLr = QtWidgets.QPushButton(ParametersPage)
        self.ebtnLr.setGeometry(QtCore.QRect(520, 260, 29, 29))
        self.ebtnLr.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnLr.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnLr.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnLr.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnLr.setCheckable(True)
        self.ebtnLr.setAutoDefault(False)
        self.ebtnLr.setFlat(True)
        self.ebtnLr.setObjectName("ebtnLr")
        self.ebtnSg = QtWidgets.QPushButton(ParametersPage)
        self.ebtnSg.setGeometry(QtCore.QRect(160, 190, 29, 29))
        self.ebtnSg.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnSg.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnSg.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnSg.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnSg.setCheckable(True)
        self.ebtnSg.setAutoDefault(False)
        self.ebtnSg.setFlat(True)
        self.ebtnSg.setObjectName("ebtnSg")
        self.ebtnHg = QtWidgets.QPushButton(ParametersPage)
        self.ebtnHg.setGeometry(QtCore.QRect(340, 160, 29, 29))
        self.ebtnHg.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnHg.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnHg.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnHg.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnHg.setCheckable(True)
        self.ebtnHg.setAutoDefault(False)
        self.ebtnHg.setFlat(True)
        self.ebtnHg.setObjectName("ebtnHg")
        self.ebtnAs = QtWidgets.QPushButton(ParametersPage)
        self.ebtnAs.setGeometry(QtCore.QRect(430, 100, 29, 29))
        self.ebtnAs.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnAs.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnAs.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnAs.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnAs.setCheckable(True)
        self.ebtnAs.setAutoDefault(False)
        self.ebtnAs.setFlat(True)
        self.ebtnAs.setObjectName("ebtnAs")
        self.ebtnCu = QtWidgets.QPushButton(ParametersPage)
        self.ebtnCu.setGeometry(QtCore.QRect(310, 100, 29, 29))
        self.ebtnCu.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnCu.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnCu.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnCu.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnCu.setCheckable(True)
        self.ebtnCu.setAutoDefault(False)
        self.ebtnCu.setFlat(True)
        self.ebtnCu.setObjectName("ebtnCu")
        self.ebtnCf = QtWidgets.QPushButton(ParametersPage)
        self.ebtnCf.setGeometry(QtCore.QRect(370, 260, 29, 29))
        self.ebtnCf.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnCf.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnCf.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnCf.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnCf.setCheckable(True)
        self.ebtnCf.setAutoDefault(False)
        self.ebtnCf.setFlat(True)
        self.ebtnCf.setObjectName("ebtnCf")
        self.ebtnTi = QtWidgets.QPushButton(ParametersPage)
        self.ebtnTi.setGeometry(QtCore.QRect(100, 100, 29, 29))
        self.ebtnTi.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnTi.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnTi.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnTi.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnTi.setCheckable(True)
        self.ebtnTi.setAutoDefault(False)
        self.ebtnTi.setFlat(True)
        self.ebtnTi.setObjectName("ebtnTi")
        self.ebtnDy = QtWidgets.QPushButton(ParametersPage)
        self.ebtnDy.setGeometry(QtCore.QRect(370, 230, 29, 29))
        self.ebtnDy.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnDy.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnDy.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnDy.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnDy.setCheckable(True)
        self.ebtnDy.setAutoDefault(False)
        self.ebtnDy.setFlat(True)
        self.ebtnDy.setObjectName("ebtnDy")
        self.ebtnPm = QtWidgets.QPushButton(ParametersPage)
        self.ebtnPm.setGeometry(QtCore.QRect(220, 230, 29, 29))
        self.ebtnPm.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnPm.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnPm.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnPm.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnPm.setCheckable(True)
        self.ebtnPm.setAutoDefault(False)
        self.ebtnPm.setFlat(True)
        self.ebtnPm.setObjectName("ebtnPm")
        self.ebtnAg = QtWidgets.QPushButton(ParametersPage)
        self.ebtnAg.setGeometry(QtCore.QRect(310, 130, 29, 29))
        self.ebtnAg.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnAg.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnAg.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnAg.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnAg.setCheckable(True)
        self.ebtnAg.setAutoDefault(False)
        self.ebtnAg.setFlat(True)
        self.ebtnAg.setObjectName("ebtnAg")
        self.ebtnZn = QtWidgets.QPushButton(ParametersPage)
        self.ebtnZn.setGeometry(QtCore.QRect(340, 100, 29, 29))
        self.ebtnZn.setMinimumSize(QtCore.QSize(29, 29))
        self.ebtnZn.setMaximumSize(QtCore.QSize(29, 29))
        self.ebtnZn.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ebtnZn.setStyleSheet(
            "QPushButton {\n"
            "    border: none;\n"
            "    background-color: #1D2D44;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    border: none;\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    border:none;\n"
            "    background-color: #748CAB;\n"
            "    color: #F0EBD8;            \n"
            "}"
        )
        self.ebtnZn.setCheckable(True)
        self.ebtnZn.setAutoDefault(False)
        self.ebtnZn.setFlat(True)
        self.ebtnZn.setObjectName("ebtnZn")
        self.tableWidget = QtWidgets.QTableWidget(ParametersPage)
        self.tableWidget.setGeometry(QtCore.QRect(570, 10, 410, 171))
        self.tableWidget.setMinimumSize(QtCore.QSize(410, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(410, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 216))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 19, 33))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 216))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 216))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 19, 33))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 19, 33))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 30, 43))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 216, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 216))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 19, 33))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 216))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 216))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 19, 33))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 19, 33))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 30, 43))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 216, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 216))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 19, 33))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 216))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 216))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 19, 33))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 19, 33))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(24, 30, 43))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 235, 216, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.tableWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(QtGui.QFont.Weight.Normal)
        self.tableWidget.setFont(font)
        self.tableWidget.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.tableWidget.setStyleSheet(
            "QTableWidget {    \n"
            "    color: #F0EBD8;\n"
            "    gridline-color: rgb(53, 66, 87);\n"
            "    border-radius: 0px;\n"
            "    border-bottom: 0px solid;\n"
            "}\n"
            "QTableWidget::item{\n"
            "    border-color: #748CAB;\n"
            "    gridline-color: rgb(53, 66, 87);\n"
            "}\n"
            "QTableWidget::item:selected{\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QScrollBar:horizontal {\n"
            "    border: 1px solid;\n"
            "    background-color: #1D2D44;\n"
            "    border-radius: 10px;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: 0px solid;\n"
            "    background-color: #1D2D44;\n"
            "    gridline-color: rgb(53, 66, 87);\n"
            "    border-top: 1px solid;\n"
            "    border-color: rgb(53, 66, 87);\n"
            " }\n"
            "\n"
            "QHeaderView::section{\n"
            "    color: #F0EBD8;\n"
            "    background-color: #1D2D44;\n"
            "    max-width: 10px;\n"
            "    border: 0px solid;\n"
            "    border-style: none;\n"
            "}\n"
            "QTableWidget::horizontalHeader {    \n"
            "    background-color: #1D2D44;\n"
            "}\n"
            "\n"
            "QHeaderView::section:horizontal\n"
            "{\n"
            "    background-color: #1D2D44;\n"
            "    border-bottom: 1px solid rgb(53, 66, 87);\n"
            "}\n"
            "QHeaderView::section:vertical\n"
            "{\n"
            "    border: 0px solid rgb(44, 49, 60);\n"
            "}\n"
            ""
        )
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.DoubleClicked)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(190)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(18)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.resultsTreeWidget = QtWidgets.QTreeWidget(ParametersPage)
        self.resultsTreeWidget.setGeometry(QtCore.QRect(10, 310, 971, 333))
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
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QTreeWidget::item:selected{\n"
            "    background-color: #3E5C76;\n"
            "    color: #F0EBD8;\n"
            "}\n"
            "\n"
            "QHeaderView::section{\n"
            "    color: #F0EBD8;\n"
            "    background-color: #1D2D44;\n"
            "    max-width: 30px;\n"
            "    border: 0px solid;\n"
            "    border-style: none;\n"
            "    border-bottom: 0px solid;\n"
            "    border-right: 1px solid rgb(53, 66, 87);\n"
            "}\n"
            "\n"
            "QHeaderView::section:horizontal\n"
            "{\n"
            "    background-color: #1D2D44;\n"
            "    border-bottom: 0px solid;\n"
            "}\n"
            "QHeaderView::section:vertical\n"
            "{\n"
            "    border: 0px solid rgb(44, 49, 60);\n"
            "}\n"
            "\n"
            "QHeaderView::down-arrow {\n"
            "     image: url(down_arrow_gray.png);\n"
            "}\n"
            "\n"
            "QHeaderView::up-arrow {\n"
            "}"
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
        self.resultsTreeWidget.headerItem().setTextAlignment(0, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsTreeWidget.headerItem().setTextAlignment(1, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsTreeWidget.headerItem().setTextAlignment(2, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsTreeWidget.headerItem().setTextAlignment(3, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsTreeWidget.headerItem().setTextAlignment(4, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsTreeWidget.headerItem().setTextAlignment(5, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsTreeWidget.headerItem().setTextAlignment(6, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsTreeWidget.headerItem().setTextAlignment(7, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsTreeWidget.headerItem().setTextAlignment(8, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsTreeWidget.headerItem().setTextAlignment(9, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsTreeWidget.headerItem().setTextAlignment(10, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsTreeWidget.headerItem().setTextAlignment(11, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsTreeWidget.headerItem().setTextAlignment(12, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsTreeWidget.headerItem().setTextAlignment(13, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsTreeWidget.headerItem().setTextAlignment(14, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsTreeWidget.headerItem().setTextAlignment(15, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsTreeWidget.headerItem().setTextAlignment(16, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsTreeWidget.headerItem().setTextAlignment(17, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsTreeWidget.headerItem().setTextAlignment(18, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsTreeWidget.headerItem().setTextAlignment(19, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsTreeWidget.headerItem().setTextAlignment(20, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsTreeWidget.headerItem().setTextAlignment(21, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsTreeWidget.headerItem().setTextAlignment(22, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsTreeWidget.headerItem().setTextAlignment(23, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsTreeWidget.headerItem().setTextAlignment(24, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultsTreeWidget.header().setVisible(True)
        self.resultsTreeWidget.header().setCascadingSectionResizes(False)
        self.resultsTreeWidget.header().setDefaultSectionSize(96)
        self.resultsTreeWidget.header().setHighlightSections(True)
        self.resultsTreeWidget.header().setMinimumSectionSize(15)
        self.resultsTreeWidget.header().setSortIndicatorShown(True)
        self.resultsTreeWidget.header().setStretchLastSection(True)
        self.ClearAllPushButton = QtWidgets.QPushButton(ParametersPage)
        self.ClearAllPushButton.setGeometry(QtCore.QRect(570, 264, 410, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ClearAllPushButton.sizePolicy().hasHeightForWidth())
        self.ClearAllPushButton.setSizePolicy(sizePolicy)
        self.ClearAllPushButton.setMinimumSize(QtCore.QSize(198, 25))
        self.ClearAllPushButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.ClearAllPushButton.setStyleSheet(
            "QPushButton{background-color: #1D2D44;color: #F0EBD8;}\n"
            "QPushButton:hover{background-color: #3E5C76;color: #F0EBD8;}\n"
            "QPushButton:pressed{background-color: #748CAB;color: #F0EBD8;};"
        )
        self.ClearAllPushButton.setObjectName("ClearAllPushButton")
        self.SavePushButton = QtWidgets.QPushButton(ParametersPage)
        self.SavePushButton.setGeometry(QtCore.QRect(570, 230, 410, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SavePushButton.sizePolicy().hasHeightForWidth())
        self.SavePushButton.setSizePolicy(sizePolicy)
        self.SavePushButton.setMinimumSize(QtCore.QSize(198, 25))
        self.SavePushButton.setStyleSheet(
            "QPushButton{background-color: #1D2D44;color: #F0EBD8;}\n"
            "QPushButton:hover{background-color: #3E5C76;color: #F0EBD8;}\n"
            "QPushButton:pressed{background-color: #748CAB;color: #F0EBD8;};"
        )
        self.SavePushButton.setObjectName("SavePushButton")
        self.CalculatePushButton = QtWidgets.QPushButton(ParametersPage)
        self.CalculatePushButton.setGeometry(QtCore.QRect(570, 196, 410, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CalculatePushButton.sizePolicy().hasHeightForWidth())
        self.CalculatePushButton.setSizePolicy(sizePolicy)
        self.CalculatePushButton.setMinimumSize(QtCore.QSize(198, 25))
        self.CalculatePushButton.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.CalculatePushButton.setStyleSheet(
            "QPushButton{background-color: #1D2D44;color: #F0EBD8;}\n"
            "QPushButton:hover{background-color: #3E5C76;color: #F0EBD8;}\n"
            "QPushButton:pressed{background-color: #748CAB;color: #F0EBD8;};"
        )
        self.CalculatePushButton.setObjectName("CalculatePushButton")

        self.retranslateUi(ParametersPage)
        QtCore.QMetaObject.connectSlotsByName(ParametersPage)

    def retranslateUi(self, ParametersPage):
        """Set all translatable string properties on the child widgets.

        Called by ``setupUi`` after the widget hierarchy is fully built.
        Populates element button labels, column/row headers, tooltip text,
        and action button captions through Qt's translation mechanism.

        Args:
            ParametersPage: The ``QWidget`` instance whose child text
                properties are being populated.
        """
        _translate = QtCore.QCoreApplication.translate
        ParametersPage.setWindowTitle(_translate("ParametersPage", "Form"))
        self.ebtnHe.setText(_translate("ParametersPage", "He"))
        self.ebtnRa.setText(_translate("ParametersPage", "Ra"))
        self.ebtnLu.setText(_translate("ParametersPage", "Lu"))
        self.ebtnGa.setText(_translate("ParametersPage", "Ga"))
        self.ebtnCa.setText(_translate("ParametersPage", "Ca"))
        self.ebtnAu.setText(_translate("ParametersPage", "Au"))
        self.ebtnLa.setText(_translate("ParametersPage", "La"))
        self.ebtnYb.setText(_translate("ParametersPage", "Yb"))
        self.ebtnW.setText(_translate("ParametersPage", "W"))
        self.ebtnBk.setText(_translate("ParametersPage", "Bk"))
        self.ebtnSc.setText(_translate("ParametersPage", "Sc"))
        self.ebtnNi.setText(_translate("ParametersPage", "Ni"))
        self.ebtnBa.setText(_translate("ParametersPage", "Ba"))
        self.ebtnBh.setText(_translate("ParametersPage", "Bh"))
        self.ebtnHs.setText(_translate("ParametersPage", "Hs"))
        self.ebtnHf.setText(_translate("ParametersPage", "Hf"))
        self.ebtnPr.setText(_translate("ParametersPage", "Pr"))
        self.ebtnV.setText(_translate("ParametersPage", "V"))
        self.ebtnN.setText(_translate("ParametersPage", "N"))
        self.ebtnFr.setText(_translate("ParametersPage", "Fr"))
        self.ebtnGd.setText(_translate("ParametersPage", "Gd"))
        self.ebtnO.setText(_translate("ParametersPage", "O"))
        self.ebtnPt.setText(_translate("ParametersPage", "Pt"))
        self.ebtnLi.setText(_translate("ParametersPage", "Li"))
        self.ebtnP.setText(_translate("ParametersPage", "P"))
        self.ebtnXe.setText(_translate("ParametersPage", "Xe"))
        self.ebtnPd.setText(_translate("ParametersPage", "Pd"))
        self.ebtnDb.setText(_translate("ParametersPage", "Db"))
        self.ebtnRb.setText(_translate("ParametersPage", "Rb"))
        self.ebtnBi.setText(_translate("ParametersPage", "Bi"))
        self.ebtnIn.setText(_translate("ParametersPage", "In"))
        self.ebtnS.setText(_translate("ParametersPage", "S"))
        self.ebtnAnd.setText(_translate("ParametersPage", "Nd"))
        self.ebtnNa.setText(_translate("ParametersPage", "Na"))
        self.ebtnIr.setText(_translate("ParametersPage", "Ir"))
        self.ebtnOs.setText(_translate("ParametersPage", "Os"))
        self.ebtnPu.setText(_translate("ParametersPage", "Pu"))
        self.ebtnTe.setText(_translate("ParametersPage", "Te"))
        self.ebtnEs.setText(_translate("ParametersPage", "Es"))
        self.ebtnCe.setText(_translate("ParametersPage", "Ce"))
        self.ebtnB.setText(_translate("ParametersPage", "B"))
        self.ebtnRe.setText(_translate("ParametersPage", "Re"))
        self.ebtnCs.setText(_translate("ParametersPage", "Cs"))
        self.ebtnCd.setText(_translate("ParametersPage", "Cd"))
        self.ebtnPb.setText(_translate("ParametersPage", "Pb"))
        self.ebtnRn.setText(_translate("ParametersPage", "Rn"))
        self.ebtnY.setText(_translate("ParametersPage", "Y"))
        self.ebtnU.setText(_translate("ParametersPage", "U"))
        self.ebtnBr.setText(_translate("ParametersPage", "Br"))
        self.ebtnC.setText(_translate("ParametersPage", "C"))
        self.ebtnHo.setText(_translate("ParametersPage", "Ho"))
        self.ebtnNp.setText(_translate("ParametersPage", "Np"))
        self.ebtnEu.setText(_translate("ParametersPage", "Eu"))
        self.ebtnMn.setText(_translate("ParametersPage", "Mn"))
        self.ebtnGe.setText(_translate("ParametersPage", "Ge"))
        self.ebtnAc.setText(_translate("ParametersPage", "Ac"))
        self.ebtnAl.setText(_translate("ParametersPage", "Al"))
        self.ebtnSr.setText(_translate("ParametersPage", "Sr"))
        self.ebtnPo.setText(_translate("ParametersPage", "Po"))
        self.ebtnH.setText(_translate("ParametersPage", "H"))
        self.ebtnMg.setText(_translate("ParametersPage", "Mg"))
        self.ebtnNb.setText(_translate("ParametersPage", "Nb"))
        self.ebtnSe.setText(_translate("ParametersPage", "Se"))
        self.ebtnFm.setText(_translate("ParametersPage", "Fm"))
        self.ebtnRu.setText(_translate("ParametersPage", "Ru"))
        self.ebtnZr.setText(_translate("ParametersPage", "Zr"))
        self.ebtnCm.setText(_translate("ParametersPage", "Cm"))
        self.ebtnAm.setText(_translate("ParametersPage", "Am"))
        self.ebtnNo.setText(_translate("ParametersPage", "No"))
        self.ebtnMt.setText(_translate("ParametersPage", "Mt"))
        self.ebtnTh.setText(_translate("ParametersPage", "Th"))
        self.ebtnK.setText(_translate("ParametersPage", "K"))
        self.ebtnMo.setText(_translate("ParametersPage", "Mo"))
        self.ebtnF.setText(_translate("ParametersPage", "F"))
        self.ebtnTc.setText(_translate("ParametersPage", "Tc"))
        self.ebtnNe.setText(_translate("ParametersPage", "Ne"))
        self.ebtnCo.setText(_translate("ParametersPage", "Co"))
        self.ebtnMd.setText(_translate("ParametersPage", "Md"))
        self.ebtnSb.setText(_translate("ParametersPage", "Sb"))
        self.ebtnTb.setText(_translate("ParametersPage", "Tb"))
        self.ebtnTm.setText(_translate("ParametersPage", "Tm"))
        self.ebtnEr.setText(_translate("ParametersPage", "Er"))
        self.ebtnCl.setText(_translate("ParametersPage", "Cl"))
        self.ebtnAt.setText(_translate("ParametersPage", "At"))
        self.ebtnCr.setText(_translate("ParametersPage", "Cr"))
        self.ebtnTa.setText(_translate("ParametersPage", "Ta"))
        self.ebtnRh.setText(_translate("ParametersPage", "Rh"))
        self.ebtnI.setText(_translate("ParametersPage", "I"))
        self.ebtnTl.setText(_translate("ParametersPage", "Tl"))
        self.ebtnSn.setText(_translate("ParametersPage", "Sn"))
        self.ebtnPa.setText(_translate("ParametersPage", "Pa"))
        self.ebtnAr.setText(_translate("ParametersPage", "Ar"))
        self.ebtnSi.setText(_translate("ParametersPage", "Si"))
        self.ebtnSm.setText(_translate("ParametersPage", "Sm"))
        self.ebtnFe.setText(_translate("ParametersPage", "Fe"))
        self.ebtnKr.setText(_translate("ParametersPage", "Kr"))
        self.ebtnBe.setText(_translate("ParametersPage", "Be"))
        self.ebtnRf.setText(_translate("ParametersPage", "Rf"))
        self.ebtnLr.setText(_translate("ParametersPage", "Lr"))
        self.ebtnSg.setText(_translate("ParametersPage", "Sg"))
        self.ebtnHg.setText(_translate("ParametersPage", "Hg"))
        self.ebtnAs.setText(_translate("ParametersPage", "As"))
        self.ebtnCu.setText(_translate("ParametersPage", "Cu"))
        self.ebtnCf.setText(_translate("ParametersPage", "Cf"))
        self.ebtnTi.setText(_translate("ParametersPage", "Ti"))
        self.ebtnDy.setText(_translate("ParametersPage", "Dy"))
        self.ebtnPm.setText(_translate("ParametersPage", "Pm"))
        self.ebtnAg.setText(_translate("ParametersPage", "Ag"))
        self.ebtnZn.setText(_translate("ParametersPage", "Zn"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ParametersPage", "Element"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ParametersPage", "at%"))
        self.resultsTreeWidget.setSortingEnabled(True)
        header = self.resultsTreeWidget.header()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setStretchLastSection(False)
        header.setSectionResizeMode(8, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.resultsTreeWidget.headerItem().setText(0, _translate("ParametersPage", "Formula"))

        self.resultsTreeWidget.headerItem().setText(1, _translate("ParametersPage", "Density"))
        self.resultsTreeWidget.headerItem().setToolTip(
            1,
            _translate(
                "ParametersPage",
                '<html><head/><body><p>g/cm<span style=" vertical-align:super;">3</span></p></body></html>',
            ),
        )
        self.resultsTreeWidget.headerItem().setText(2, _translate("ParametersPage", "δ"))
        self.resultsTreeWidget.headerItem().setText(3, _translate("ParametersPage", "δ (CN12)"))
        self.resultsTreeWidget.headerItem().setText(4, _translate("ParametersPage", "Δχ (Allen)"))
        self.resultsTreeWidget.headerItem().setText(5, _translate("ParametersPage", "Δχ (Pauling)"))
        self.resultsTreeWidget.headerItem().setText(6, _translate("ParametersPage", "Omega"))
        self.resultsTreeWidget.headerItem().setText(7, _translate("ParametersPage", "Gamma"))
        self.resultsTreeWidget.headerItem().setToolTip(
            7,
            _translate("ParametersPage", "<html><head/><body><p>γ</p></body></html>"),
        )
        self.resultsTreeWidget.headerItem().setText(8, _translate("ParametersPage", "Lambda"))
        self.resultsTreeWidget.headerItem().setToolTip(
            8,
            _translate("ParametersPage", "<html><head/><body><p>λ</p></body></html>"),
        )
        self.resultsTreeWidget.headerItem().setText(9, _translate("ParametersPage", "VEC"))
        self.resultsTreeWidget.headerItem().setText(10, _translate("ParametersPage", "e/a"))

        self.resultsTreeWidget.headerItem().setText(11, _translate("ParametersPage", "Mixing Enthalpy"))
        self.resultsTreeWidget.headerItem().setToolTip(
            11,
            _translate("ParametersPage", "<html><head/><body><p>kJ/mol</p></body></html>"),
        )
        self.resultsTreeWidget.headerItem().setText(12, _translate("ParametersPage", "Mixing Entropy"))
        self.resultsTreeWidget.headerItem().setToolTip(
            12,
            _translate("ParametersPage", "<html><head/><body><p>J/K.mol</p></body></html>"),
        )

        self.resultsTreeWidget.headerItem().setText(13, _translate("ParametersPage", "Formation Enthalpy"))
        self.resultsTreeWidget.headerItem().setToolTip(
            13,
            _translate("ParametersPage", "<html><head/><body><p>meV/atom</p></body></html>"),
        )

        self.resultsTreeWidget.headerItem().setText(14, _translate("ParametersPage", "Min. Formation Enthalpy"))
        self.resultsTreeWidget.headerItem().setToolTip(
            14,
            _translate("ParametersPage", "<html><head/><body><p>meV/atom</p></body></html>"),
        )

        self.resultsTreeWidget.headerItem().setText(15, _translate("ParametersPage", "Melting Temperature"))
        self.resultsTreeWidget.headerItem().setToolTip(
            15, _translate("ParametersPage", "<html><head/><body><p>K</p></body></html>")
        )

        self.resultsTreeWidget.headerItem().setText(16, _translate("ParametersPage", "Crystal Structure"))
        self.resultsTreeWidget.headerItem().setText(17, _translate("ParametersPage", "Model 1"))
        self.resultsTreeWidget.headerItem().setText(18, _translate("ParametersPage", "Model 2"))
        self.resultsTreeWidget.headerItem().setText(19, _translate("ParametersPage", "Model 3"))
        self.resultsTreeWidget.headerItem().setText(20, _translate("ParametersPage", "Model 4"))
        self.resultsTreeWidget.headerItem().setText(21, _translate("ParametersPage", "Model 5"))
        self.resultsTreeWidget.headerItem().setText(22, _translate("ParametersPage", "Model 6"))
        self.resultsTreeWidget.headerItem().setText(23, _translate("ParametersPage", "Model 7"))
        self.resultsTreeWidget.headerItem().setText(24, _translate("ParametersPage", "Model 8"))
        self.ClearAllPushButton.setText(_translate("ParametersPage", "Clear All"))
        self.SavePushButton.setText(_translate("ParametersPage", "Save"))
        self.CalculatePushButton.setText(_translate("ParametersPage", "Calculate"))
