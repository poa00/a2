# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'numpad.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from a2qt.QtCore import *
from a2qt.QtGui import *
from a2qt.QtWidgets import *


class Ui_Numpad(object):
    def setupUi(self, Numpad):
        if not Numpad.objectName():
            Numpad.setObjectName(u"Numpad")

        self.gridLayout = QGridLayout(Numpad)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.numlock = QPushButton(Numpad)
        self.numlock.setObjectName(u"numlock")

        self.gridLayout.addWidget(self.numlock, 1, 0, 1, 1)

        self.numpaddiv = QPushButton(Numpad)
        self.numpaddiv.setObjectName(u"numpaddiv")

        self.gridLayout.addWidget(self.numpaddiv, 1, 1, 1, 1)

        self.numpad1 = QPushButton(Numpad)
        self.numpad1.setObjectName(u"numpad1")

        self.gridLayout.addWidget(self.numpad1, 4, 0, 1, 1)

        self.numpad5 = QPushButton(Numpad)
        self.numpad5.setObjectName(u"numpad5")

        self.gridLayout.addWidget(self.numpad5, 3, 1, 1, 1)

        self.numpadmult = QPushButton(Numpad)
        self.numpadmult.setObjectName(u"numpadmult")

        self.gridLayout.addWidget(self.numpadmult, 1, 2, 1, 1)

        self.numpad8 = QPushButton(Numpad)
        self.numpad8.setObjectName(u"numpad8")

        self.gridLayout.addWidget(self.numpad8, 2, 1, 1, 1)

        self.numpad4 = QPushButton(Numpad)
        self.numpad4.setObjectName(u"numpad4")

        self.gridLayout.addWidget(self.numpad4, 3, 0, 1, 1)

        self.numpad3 = QPushButton(Numpad)
        self.numpad3.setObjectName(u"numpad3")

        self.gridLayout.addWidget(self.numpad3, 4, 2, 1, 1)

        self.numpad6 = QPushButton(Numpad)
        self.numpad6.setObjectName(u"numpad6")

        self.gridLayout.addWidget(self.numpad6, 3, 2, 1, 1)

        self.numpad7 = QPushButton(Numpad)
        self.numpad7.setObjectName(u"numpad7")

        self.gridLayout.addWidget(self.numpad7, 2, 0, 1, 1)

        self.numpad2 = QPushButton(Numpad)
        self.numpad2.setObjectName(u"numpad2")

        self.gridLayout.addWidget(self.numpad2, 4, 1, 1, 1)

        self.numpaddot = QPushButton(Numpad)
        self.numpaddot.setObjectName(u"numpaddot")

        self.gridLayout.addWidget(self.numpaddot, 5, 2, 1, 1)

        self.numpad9 = QPushButton(Numpad)
        self.numpad9.setObjectName(u"numpad9")

        self.gridLayout.addWidget(self.numpad9, 2, 2, 1, 1)

        self.numpad0 = QPushButton(Numpad)
        self.numpad0.setObjectName(u"numpad0")

        self.gridLayout.addWidget(self.numpad0, 5, 0, 1, 2)

        self.numpadsub = QPushButton(Numpad)
        self.numpadsub.setObjectName(u"numpadsub")

        self.gridLayout.addWidget(self.numpadsub, 1, 3, 1, 1)

        self.num_spacer = QWidget(Numpad)
        self.num_spacer.setObjectName(u"num_spacer")
        self.numpadsub.raise_()

        self.gridLayout.addWidget(self.num_spacer, 0, 0, 1, 5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.numpadadd = QPushButton(Numpad)
        self.numpadadd.setObjectName(u"numpadadd")
        self.numpadadd.setMinimumSize(QSize(0, 120))

        self.verticalLayout_2.addWidget(self.numpadadd, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout_2, 2, 3, 2, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.numpadenter = QPushButton(Numpad)
        self.numpadenter.setObjectName(u"numpadenter")
        self.numpadenter.setMinimumSize(QSize(0, 90))

        self.verticalLayout.addWidget(self.numpadenter)

        self.verticalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.verticalLayout, 4, 3, 2, 1)

        self.gridLayout.setRowStretch(0, 1)

        self.retranslateUi(Numpad)

        QMetaObject.connectSlotsByName(Numpad)
    # setupUi

    def retranslateUi(self, Numpad):
        Numpad.setWindowTitle(QCoreApplication.translate("Numpad", u"Form", None))
        self.numlock.setText(QCoreApplication.translate("Numpad", u"Num\n"
"Lock", None))
        self.numpaddiv.setText(QCoreApplication.translate("Numpad", u"/", None))
        self.numpad1.setText(QCoreApplication.translate("Numpad", u"1", None))
        self.numpad5.setText(QCoreApplication.translate("Numpad", u"5", None))
        self.numpadmult.setText(QCoreApplication.translate("Numpad", u"*", None))
        self.numpad8.setText(QCoreApplication.translate("Numpad", u"8", None))
        self.numpad4.setText(QCoreApplication.translate("Numpad", u"4", None))
        self.numpad3.setText(QCoreApplication.translate("Numpad", u"3", None))
        self.numpad6.setText(QCoreApplication.translate("Numpad", u"6", None))
        self.numpad7.setText(QCoreApplication.translate("Numpad", u"7", None))
        self.numpad2.setText(QCoreApplication.translate("Numpad", u"2", None))
        self.numpaddot.setText(QCoreApplication.translate("Numpad", u".", None))
        self.numpad9.setText(QCoreApplication.translate("Numpad", u"9", None))
        self.numpad0.setText(QCoreApplication.translate("Numpad", u"0", None))
        self.numpadsub.setText(QCoreApplication.translate("Numpad", u"-", None))
        self.numpadadd.setText(QCoreApplication.translate("Numpad", u"+", None))
        self.numpadenter.setText(QCoreApplication.translate("Numpad", u"Enter", None))
    # retranslateUi

