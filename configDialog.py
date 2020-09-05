# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\configDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_configDialog(object):
    def setupUi(self, configDialog):
        configDialog.setObjectName("configDialog")
        configDialog.resize(452, 510)
        self.closeConfigDialogButton = QtWidgets.QPushButton(configDialog)
        self.closeConfigDialogButton.setGeometry(QtCore.QRect(360, 470, 81, 31))
        self.closeConfigDialogButton.setObjectName("closeConfigDialogButton")
        self.marginOffsetPreviewBox = QtWidgets.QGraphicsView(configDialog)
        self.marginOffsetPreviewBox.setEnabled(False)
        self.marginOffsetPreviewBox.setGeometry(QtCore.QRect(70, 70, 320, 180))
        self.marginOffsetPreviewBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.marginOffsetPreviewBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.marginOffsetPreviewBox.setObjectName("marginOffsetPreviewBox")
        self.marginOffsetSpinBoxLeft = QtWidgets.QSpinBox(configDialog)
        self.marginOffsetSpinBoxLeft.setEnabled(False)
        self.marginOffsetSpinBoxLeft.setGeometry(QtCore.QRect(20, 140, 42, 22))
        self.marginOffsetSpinBoxLeft.setObjectName("marginOffsetSpinBoxLeft")
        self.marginOffsetSpinBoxRight = QtWidgets.QSpinBox(configDialog)
        self.marginOffsetSpinBoxRight.setEnabled(False)
        self.marginOffsetSpinBoxRight.setGeometry(QtCore.QRect(400, 140, 42, 22))
        self.marginOffsetSpinBoxRight.setObjectName("marginOffsetSpinBoxRight")
        self.marginOffsetSpinBoxTop = QtWidgets.QSpinBox(configDialog)
        self.marginOffsetSpinBoxTop.setEnabled(False)
        self.marginOffsetSpinBoxTop.setGeometry(QtCore.QRect(200, 40, 42, 21))
        self.marginOffsetSpinBoxTop.setObjectName("marginOffsetSpinBoxTop")
        self.marginOffsetSpinBoxBottom = QtWidgets.QSpinBox(configDialog)
        self.marginOffsetSpinBoxBottom.setEnabled(False)
        self.marginOffsetSpinBoxBottom.setGeometry(QtCore.QRect(200, 260, 42, 22))
        self.marginOffsetSpinBoxBottom.setObjectName("marginOffsetSpinBoxBottom")
        self.marginOffsetSetterLabel = QtWidgets.QLabel(configDialog)
        self.marginOffsetSetterLabel.setGeometry(QtCore.QRect(10, 10, 91, 21))
        self.marginOffsetSetterLabel.setObjectName("marginOffsetSetterLabel")
        self.marginOffsetPresetComboBox = QtWidgets.QComboBox(configDialog)
        self.marginOffsetPresetComboBox.setEnabled(False)
        self.marginOffsetPresetComboBox.setGeometry(QtCore.QRect(110, 10, 151, 21))
        self.marginOffsetPresetComboBox.setObjectName("marginOffsetPresetComboBox")
        self.marginOffsetHint = QtWidgets.QLabel(configDialog)
        self.marginOffsetHint.setGeometry(QtCore.QRect(10, 290, 331, 16))
        self.marginOffsetHint.setObjectName("marginOffsetHint")
        self.testScreenshotButton = QtWidgets.QPushButton(configDialog)
        self.testScreenshotButton.setEnabled(False)
        self.testScreenshotButton.setGeometry(QtCore.QRect(370, 40, 75, 21))
        self.testScreenshotButton.setObjectName("testScreenshotButton")
        self.marginOffsetSetterLabel_2 = QtWidgets.QLabel(configDialog)
        self.marginOffsetSetterLabel_2.setGeometry(QtCore.QRect(10, 30, 91, 21))
        self.marginOffsetSetterLabel_2.setObjectName("marginOffsetSetterLabel_2")

        self.retranslateUi(configDialog)
        QtCore.QMetaObject.connectSlotsByName(configDialog)

    def retranslateUi(self, configDialog):
        _translate = QtCore.QCoreApplication.translate
        configDialog.setWindowTitle(_translate("configDialog", "Dialog"))
        self.closeConfigDialogButton.setText(_translate("configDialog", "关闭"))
        self.marginOffsetSetterLabel.setText(_translate("configDialog", "模拟器偏移设定"))
        self.marginOffsetHint.setText(_translate("configDialog", "(注：应当设定至刚好只留下完整的游戏界面，且画面为16:9）"))
        self.testScreenshotButton.setText(_translate("configDialog", "截屏测试"))
        self.marginOffsetSetterLabel_2.setText(_translate("configDialog", "（已弃用）"))