"""Main window UI definition for HEACalculator.

Auto-generated from Qt Designer and adapted for the src-layout package
structure. Defines the top-level ``QMainWindow`` layout: a custom top bar
(title label + close button), a collapsible side-menu (Parameters, Range
Search, MDL buttons), and a ``QStackedWidget`` content area that hosts the
per-page widgets.
"""

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_HEACalculator(object):
    """Qt Designer-generated UI class for the HEACalculator main window.

    Builds the complete widget hierarchy and wires up tab-order when
    ``setupUi`` is called on a ``QMainWindow`` instance.
    """

    def setupUi(self, HEACalculator):
        """Create and arrange all child widgets inside *HEACalculator*.

        Sets fixed window dimensions (1125x600), applies the dark-theme
        stylesheet, constructs the top bar and side-menu frames, and
        embeds a ``QStackedWidget`` for page switching.

        Args:
            HEACalculator: The ``QMainWindow`` instance that owns this UI.
        """
        HEACalculator.setObjectName("HEACalculator")
        HEACalculator.resize(1125, 600)
        HEACalculator.setMinimumSize(QtCore.QSize(1125, 600))
        HEACalculator.setMaximumSize(QtCore.QSize(1125, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/icons/images/icon.ico"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        HEACalculator.setWindowIcon(icon)
        HEACalculator.setStyleSheet("background-color: rgb(13, 19, 33);")
        self.centralwidget = QtWidgets.QWidget(HEACalculator)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TopBar = QtWidgets.QFrame(self.centralwidget)
        self.TopBar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.TopBar.setStyleSheet("background-color: rgb(29, 45, 68);")
        self.TopBar.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.TopBar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.TopBar.setObjectName("TopBar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.TopBar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toggle_f = QtWidgets.QFrame(self.TopBar)
        self.toggle_f.setMaximumSize(QtCore.QSize(125, 40))
        self.toggle_f.setStyleSheet("background-color: #748CAB;")
        self.toggle_f.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.toggle_f.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.toggle_f.setObjectName("toggle_f")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.toggle_f)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblTitle = QtWidgets.QLabel(self.toggle_f)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono for Powerline")
        font.setBold(True)
        font.setWeight(QtGui.QFont.Weight.Bold)
        self.lblTitle.setFont(font)
        self.lblTitle.setStyleSheet("color: rgb(240, 235, 216);\nborder: 0px solid;")
        self.lblTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.verticalLayout_2.addWidget(self.lblTitle)
        self.horizontalLayout.addWidget(self.toggle_f)
        self.title_f = QtWidgets.QFrame(self.TopBar)
        self.title_f.setStyleSheet(
            "QPushButton {\n"
            "    color: #F0EBD8;\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #3E5C76\n"
            "}\n"
            "\n"
            "QPushButton:pressed {    \n"
            "    background-color: #748CAB;\n"
            "}"
        )
        self.title_f.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.title_f.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.title_f.setObjectName("title_f")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.title_f)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(self.title_f)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.title_f)
        self.frame_2.setMaximumSize(QtCore.QSize(40, 16777215))
        self.frame_2.setStyleSheet("QPushButton {\n    border: 0px solid;\n    color: #F0EBD8\n}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnClose = QtWidgets.QPushButton(self.frame_2)
        self.btnClose.setMaximumSize(QtCore.QSize(40, 40))
        self.btnClose.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.btnClose.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/icons/images/multiply.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.btnClose.setIcon(icon1)
        self.btnClose.setIconSize(QtCore.QSize(20, 20))
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout_4.addWidget(self.btnClose)
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.title_f)
        self.verticalLayout.addWidget(self.TopBar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.menu_f = QtWidgets.QFrame(self.Content)
        self.menu_f.setMinimumSize(QtCore.QSize(125, 0))
        self.menu_f.setMaximumSize(QtCore.QSize(125, 16777215))
        self.menu_f.setStyleSheet(
            "QFrame {\n"
            "background-color: rgb(29, 45, 68);\n"
            "}\n"
            "\n"
            "QPushButton {\n"
            "    background-color: rgb(29, 45, 68);\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #748CAB\n"
            "}\n"
            "\n"
            "QPushButton:pressed {    \n"
            "    background-color: #748CAB;\n"
            "}"
        )
        self.menu_f.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.menu_f.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.menu_f.setObjectName("menu_f")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.menu_f)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.menu_top_f = QtWidgets.QFrame(self.menu_f)
        self.menu_top_f.setStyleSheet(
            "QPushButton {\n"
            "    color: #F0EBD8;\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #3E5C76\n"
            "}\n"
            "\n"
            "QPushButton:pressed {    \n"
            "    background-color: #748CAB;\n"
            "}"
        )
        self.menu_top_f.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.menu_top_f.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.menu_top_f.setObjectName("menu_top_f")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.menu_top_f)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btnParameters = QtWidgets.QPushButton(self.menu_top_f)
        self.btnParameters.setMinimumSize(QtCore.QSize(0, 45))
        self.btnParameters.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.btnParameters.setStyleSheet("")
        self.btnParameters.setObjectName("btnParameters")
        self.verticalLayout_4.addWidget(self.btnParameters)
        self.btnConverter = QtWidgets.QPushButton(self.menu_top_f)
        self.btnConverter.setObjectName("btnConverter")
        self.btnConverter.setVisible(False)
        self.btnBatchAmount = QtWidgets.QPushButton(self.menu_top_f)
        self.btnBatchAmount.setMinimumSize(QtCore.QSize(0, 45))
        self.btnBatchAmount.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.btnBatchAmount.setStyleSheet("")
        self.btnBatchAmount.setObjectName("btnBatchAmount")
        self.verticalLayout_4.addWidget(self.btnBatchAmount)
        self.verticalLayout_3.addWidget(self.menu_top_f, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.menu_down_f = QtWidgets.QFrame(self.menu_f)
        self.menu_down_f.setStyleSheet(
            "QPushButton {\n"
            "    color: #F0EBD8;\n"
            "    border: 0px solid;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #3E5C76\n"
            "}\n"
            "\n"
            "QPushButton:pressed {    \n"
            "    background-color: #748CAB;\n"
            "}"
        )
        self.menu_down_f.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.menu_down_f.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.menu_down_f.setObjectName("menu_down_f")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.menu_down_f)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btnMDL = QtWidgets.QPushButton(self.menu_down_f)
        self.btnMDL.setMinimumSize(QtCore.QSize(0, 40))
        self.btnMDL.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.btnMDL.setObjectName("btnMDL")
        self.verticalLayout_5.addWidget(self.btnMDL)
        self.verticalLayout_3.addWidget(self.menu_down_f, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        self.horizontalLayout_2.addWidget(self.menu_f)
        self.content_f = QtWidgets.QFrame(self.Content)
        self.content_f.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.content_f.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content_f.setObjectName("content_f")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.content_f)
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.stackedWidget = QtWidgets.QStackedWidget(self.content_f)
        self.stackedWidget.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.stackedWidget.setObjectName("stackedWidget")
        self.verticalLayout_6.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.content_f)
        self.verticalLayout.addWidget(self.Content)
        HEACalculator.setCentralWidget(self.centralwidget)

        self.retranslateUi(HEACalculator)
        self.stackedWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(HEACalculator)
        HEACalculator.setTabOrder(self.btnParameters, self.btnBatchAmount)
        HEACalculator.setTabOrder(self.btnBatchAmount, self.btnMDL)
        HEACalculator.setTabOrder(self.btnMDL, self.btnClose)

    def retranslateUi(self, HEACalculator):
        """Set all translatable string properties on the child widgets.

        Called by ``setupUi`` after the widget hierarchy is fully built.
        Applies window title and button/label text through Qt's translation
        mechanism so the UI can be localised without touching layout code.

        Args:
            HEACalculator: The ``QMainWindow`` instance whose child text
                properties are being populated.
        """
        _translate = QtCore.QCoreApplication.translate
        HEACalculator.setWindowTitle(_translate("HEACalculator", "HEACalculator | MDL"))
        self.lblTitle.setText(_translate("HEACalculator", "HEACalculator"))
        self.btnParameters.setText(_translate("HEACalculator", "HEA\nParameters"))
        self.btnConverter.setText(_translate("HEACalculator", "At% - Wt% - Vol%\nConverter"))
        self.btnBatchAmount.setText(_translate("HEACalculator", "Range\nSearch"))
        self.btnMDL.setText(_translate("HEACalculator", "MDL"))
