# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Christopher\PycharmProjects\MayaPyBubble\resources\widget\BubbleWidget\Widget.ui'
#
# Created: Tue Feb 03 19:41:21 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class PySideUiFileSetup(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(608, 422)
        Form.gridLayout = QtGui.QGridLayout(Form)
        Form.gridLayout.setObjectName("gridLayout")
        Form.controlsBox = QtGui.QWidget(Form)
        Form.controlsBox.setObjectName("controlsBox")
        Form.verticalLayout = QtGui.QVBoxLayout(Form.controlsBox)
        Form.verticalLayout.setContentsMargins(0, 0, 0, 0)
        Form.verticalLayout.setObjectName("verticalLayout")
        Form.label = QtGui.QLabel(Form.controlsBox)
        Form.label.setObjectName("label")
        Form.verticalLayout.addWidget(Form.label)
        Form.exampleBtn = QtGui.QPushButton(Form.controlsBox)
        Form.exampleBtn.setObjectName("exampleBtn")
        Form.verticalLayout.addWidget(Form.exampleBtn)
        Form.homeBtn = QtGui.QPushButton(Form.controlsBox)
        Form.homeBtn.setObjectName("homeBtn")
        Form.verticalLayout.addWidget(Form.homeBtn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        Form.verticalLayout.addItem(spacerItem)
        Form.gridLayout.addWidget(Form.controlsBox, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(439, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        Form.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        Form.label.setText(QtGui.QApplication.translate("Form", "Make one Bubble at origin", None, QtGui.QApplication.UnicodeUTF8))
        Form.exampleBtn.setText(QtGui.QApplication.translate("Form", "Make a bubble", None, QtGui.QApplication.UnicodeUTF8))
        Form.homeBtn.setText(QtGui.QApplication.translate("Form", "Return Home", None, QtGui.QApplication.UnicodeUTF8))

