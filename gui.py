# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PCRJJCAnalyzerGUI(object):
    def setupUi(self, PCRJJCAnalyzerGUI):
        PCRJJCAnalyzerGUI.setObjectName("PCRJJCAnalyzerGUI")
        PCRJJCAnalyzerGUI.resize(825, 648)
        self.team3RadioButton = QtWidgets.QRadioButton(PCRJJCAnalyzerGUI)
        self.team3RadioButton.setEnabled(True)
        self.team3RadioButton.setGeometry(QtCore.QRect(640, 50, 61, 31))
        self.team3RadioButton.setObjectName("team3RadioButton")
        self.activeTeamNumButtonGroup = QtWidgets.QButtonGroup(PCRJJCAnalyzerGUI)
        self.activeTeamNumButtonGroup.setObjectName("activeTeamNumButtonGroup")
        self.activeTeamNumButtonGroup.addButton(self.team3RadioButton)
        self.team2RadioButton = QtWidgets.QRadioButton(PCRJJCAnalyzerGUI)
        self.team2RadioButton.setEnabled(True)
        self.team2RadioButton.setGeometry(QtCore.QRect(580, 55, 61, 21))
        self.team2RadioButton.setObjectName("team2RadioButton")
        self.activeTeamNumButtonGroup.addButton(self.team2RadioButton)
        self.team1RadioButton = QtWidgets.QRadioButton(PCRJJCAnalyzerGUI)
        self.team1RadioButton.setEnabled(True)
        self.team1RadioButton.setGeometry(QtCore.QRect(520, 55, 61, 21))
        self.team1RadioButton.setObjectName("team1RadioButton")
        self.activeTeamNumButtonGroup.addButton(self.team1RadioButton)
        self.pushButton = QtWidgets.QPushButton(PCRJJCAnalyzerGUI)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(120, 10, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.regionSelector = QtWidgets.QLabel(PCRJJCAnalyzerGUI)
        self.regionSelector.setGeometry(QtCore.QRect(220, 10, 81, 31))
        self.regionSelector.setObjectName("regionSelector")
        self.setRegion3 = QtWidgets.QRadioButton(PCRJJCAnalyzerGUI)
        self.setRegion3.setGeometry(QtCore.QRect(410, 10, 51, 31))
        self.setRegion3.setObjectName("setRegion3")
        self.regionButtonGroup = QtWidgets.QButtonGroup(PCRJJCAnalyzerGUI)
        self.regionButtonGroup.setObjectName("regionButtonGroup")
        self.regionButtonGroup.addButton(self.setRegion3)
        self.setRegion2 = QtWidgets.QRadioButton(PCRJJCAnalyzerGUI)
        self.setRegion2.setGeometry(QtCore.QRect(350, 10, 61, 31))
        self.setRegion2.setObjectName("setRegion2")
        self.regionButtonGroup.addButton(self.setRegion2)
        self.setRegion1 = QtWidgets.QRadioButton(PCRJJCAnalyzerGUI)
        self.setRegion1.setGeometry(QtCore.QRect(290, 10, 61, 31))
        self.setRegion1.setObjectName("setRegion1")
        self.regionButtonGroup.addButton(self.setRegion1)
        self.char1Avatar = QtWidgets.QGraphicsView(PCRJJCAnalyzerGUI)
        self.char1Avatar.setGeometry(QtCore.QRect(20, 90, 91, 91))
        self.char1Avatar.setObjectName("char1Avatar")
        self.char1Star = QtWidgets.QGraphicsView(PCRJJCAnalyzerGUI)
        self.char1Star.setGeometry(QtCore.QRect(130, 160, 81, 21))
        self.char1Star.setObjectName("char1Star")
        self.char2Avatar = QtWidgets.QGraphicsView(PCRJJCAnalyzerGUI)
        self.char2Avatar.setGeometry(QtCore.QRect(20, 190, 91, 91))
        self.char2Avatar.setObjectName("char2Avatar")
        self.char3Avatar = QtWidgets.QGraphicsView(PCRJJCAnalyzerGUI)
        self.char3Avatar.setGeometry(QtCore.QRect(20, 290, 91, 91))
        self.char3Avatar.setObjectName("char3Avatar")
        self.char4Avatar = QtWidgets.QGraphicsView(PCRJJCAnalyzerGUI)
        self.char4Avatar.setGeometry(QtCore.QRect(20, 390, 91, 91))
        self.char4Avatar.setObjectName("char4Avatar")
        self.char5Avatar = QtWidgets.QGraphicsView(PCRJJCAnalyzerGUI)
        self.char5Avatar.setGeometry(QtCore.QRect(20, 490, 91, 91))
        self.char5Avatar.setObjectName("char5Avatar")
        self.char2Star = QtWidgets.QGraphicsView(PCRJJCAnalyzerGUI)
        self.char2Star.setGeometry(QtCore.QRect(130, 260, 81, 21))
        self.char2Star.setObjectName("char2Star")
        self.char3Star = QtWidgets.QGraphicsView(PCRJJCAnalyzerGUI)
        self.char3Star.setGeometry(QtCore.QRect(130, 360, 81, 21))
        self.char3Star.setObjectName("char3Star")
        self.char4Star = QtWidgets.QGraphicsView(PCRJJCAnalyzerGUI)
        self.char4Star.setGeometry(QtCore.QRect(130, 460, 81, 21))
        self.char4Star.setObjectName("char4Star")
        self.char5Star = QtWidgets.QGraphicsView(PCRJJCAnalyzerGUI)
        self.char5Star.setGeometry(QtCore.QRect(130, 560, 81, 21))
        self.char5Star.setObjectName("char5Star")
        self.solutionListScrollArea = QtWidgets.QScrollArea(PCRJJCAnalyzerGUI)
        self.solutionListScrollArea.setGeometry(QtCore.QRect(230, 90, 581, 491))
        self.solutionListScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.solutionListScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.solutionListScrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.solutionListScrollArea.setWidgetResizable(True)
        self.solutionListScrollArea.setObjectName("solutionListScrollArea")
        self.solutionListScrollAreaScrollAreaWidgetContents = QtWidgets.QWidget()
        self.solutionListScrollAreaScrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 579, 489))
        self.solutionListScrollAreaScrollAreaWidgetContents.setObjectName("solutionListScrollAreaScrollAreaWidgetContents")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.solutionListScrollAreaScrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 561, 471))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.solutionListLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.solutionListLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.solutionListLayout.setContentsMargins(0, 0, 0, 0)
        self.solutionListLayout.setSpacing(10)
        self.solutionListLayout.setObjectName("solutionListLayout")
        self.solutionListScrollArea.setWidget(self.solutionListScrollAreaScrollAreaWidgetContents)
        self.recognizeAndSolveButton = QtWidgets.QPushButton(PCRJJCAnalyzerGUI)
        self.recognizeAndSolveButton.setGeometry(QtCore.QRect(20, 50, 91, 31))
        self.recognizeAndSolveButton.setObjectName("recognizeAndSolveButton")
        self.manualSetChar = QtWidgets.QPushButton(PCRJJCAnalyzerGUI)
        self.manualSetChar.setEnabled(False)
        self.manualSetChar.setGeometry(QtCore.QRect(20, 10, 91, 31))
        self.manualSetChar.setObjectName("manualSetChar")
        self.TM_CCOEFF_NORMED = QtWidgets.QRadioButton(PCRJJCAnalyzerGUI)
        self.TM_CCOEFF_NORMED.setGeometry(QtCore.QRect(190, 600, 121, 16))
        self.TM_CCOEFF_NORMED.setObjectName("TM_CCOEFF_NORMED")
        self.algorithmButtonGroup = QtWidgets.QButtonGroup(PCRJJCAnalyzerGUI)
        self.algorithmButtonGroup.setObjectName("algorithmButtonGroup")
        self.algorithmButtonGroup.addButton(self.TM_CCOEFF_NORMED)
        self.TMAlgorithm = QtWidgets.QLabel(PCRJJCAnalyzerGUI)
        self.TMAlgorithm.setGeometry(QtCore.QRect(20, 600, 81, 16))
        self.TMAlgorithm.setObjectName("TMAlgorithm")
        self.TM_CCOEFF = QtWidgets.QRadioButton(PCRJJCAnalyzerGUI)
        self.TM_CCOEFF.setGeometry(QtCore.QRect(110, 600, 89, 16))
        self.TM_CCOEFF.setObjectName("TM_CCOEFF")
        self.algorithmButtonGroup.addButton(self.TM_CCOEFF)
        self.TM_CCORR = QtWidgets.QRadioButton(PCRJJCAnalyzerGUI)
        self.TM_CCORR.setGeometry(QtCore.QRect(310, 600, 71, 16))
        self.TM_CCORR.setObjectName("TM_CCORR")
        self.algorithmButtonGroup.addButton(self.TM_CCORR)
        self.TM_CCORR_NORMED = QtWidgets.QRadioButton(PCRJJCAnalyzerGUI)
        self.TM_CCORR_NORMED.setGeometry(QtCore.QRect(380, 600, 121, 16))
        self.TM_CCORR_NORMED.setObjectName("TM_CCORR_NORMED")
        self.algorithmButtonGroup.addButton(self.TM_CCORR_NORMED)
        self.TM_SQDIFF = QtWidgets.QRadioButton(PCRJJCAnalyzerGUI)
        self.TM_SQDIFF.setGeometry(QtCore.QRect(490, 600, 121, 16))
        self.TM_SQDIFF.setObjectName("TM_SQDIFF")
        self.algorithmButtonGroup.addButton(self.TM_SQDIFF)
        self.TM_SQDIFF_NORMED = QtWidgets.QRadioButton(PCRJJCAnalyzerGUI)
        self.TM_SQDIFF_NORMED.setGeometry(QtCore.QRect(570, 600, 121, 16))
        self.TM_SQDIFF_NORMED.setObjectName("TM_SQDIFF_NORMED")
        self.algorithmButtonGroup.addButton(self.TM_SQDIFF_NORMED)
        self.handleSelectorComboBox = QtWidgets.QComboBox(PCRJJCAnalyzerGUI)
        self.handleSelectorComboBox.setGeometry(QtCore.QRect(110, 620, 201, 22))
        self.handleSelectorComboBox.setObjectName("handleSelectorComboBox")
        self.HandleSelector = QtWidgets.QLabel(PCRJJCAnalyzerGUI)
        self.HandleSelector.setGeometry(QtCore.QRect(20, 620, 81, 16))
        self.HandleSelector.setObjectName("HandleSelector")
        self.apiKeylineEdit = QtWidgets.QLineEdit(PCRJJCAnalyzerGUI)
        self.apiKeylineEdit.setGeometry(QtCore.QRect(500, 620, 113, 20))
        self.apiKeylineEdit.setObjectName("apiKeylineEdit")
        self.apiKeyLabel = QtWidgets.QLabel(PCRJJCAnalyzerGUI)
        self.apiKeyLabel.setGeometry(QtCore.QRect(440, 620, 51, 16))
        self.apiKeyLabel.setObjectName("apiKeyLabel")
        self.queryStatusTag = QtWidgets.QLabel(PCRJJCAnalyzerGUI)
        self.queryStatusTag.setGeometry(QtCore.QRect(700, 50, 111, 31))
        self.queryStatusTag.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.queryStatusTag.setObjectName("queryStatusTag")
        self.recognizeAndSolveButton_TeamTwoFromHisotry = QtWidgets.QPushButton(PCRJJCAnalyzerGUI)
        self.recognizeAndSolveButton_TeamTwoFromHisotry.setGeometry(QtCore.QRect(220, 50, 91, 31))
        self.recognizeAndSolveButton_TeamTwoFromHisotry.setObjectName("recognizeAndSolveButton_TeamTwoFromHisotry")
        self.recognizeAndSolveButton_TeamThreeFromHisotry = QtWidgets.QPushButton(PCRJJCAnalyzerGUI)
        self.recognizeAndSolveButton_TeamThreeFromHisotry.setGeometry(QtCore.QRect(320, 50, 91, 31))
        self.recognizeAndSolveButton_TeamThreeFromHisotry.setObjectName("recognizeAndSolveButton_TeamThreeFromHisotry")
        self.recognizeAndSolveButton_OwnTeam = QtWidgets.QPushButton(PCRJJCAnalyzerGUI)
        self.recognizeAndSolveButton_OwnTeam.setGeometry(QtCore.QRect(420, 50, 91, 31))
        self.recognizeAndSolveButton_OwnTeam.setObjectName("recognizeAndSolveButton_OwnTeam")
        self.recognizeAndSolveButton_TeamOneFromHisotry = QtWidgets.QPushButton(PCRJJCAnalyzerGUI)
        self.recognizeAndSolveButton_TeamOneFromHisotry.setGeometry(QtCore.QRect(120, 50, 91, 31))
        self.recognizeAndSolveButton_TeamOneFromHisotry.setObjectName("recognizeAndSolveButton_TeamOneFromHisotry")
        self.char1Dropbox = QtWidgets.QComboBox(PCRJJCAnalyzerGUI)
        self.char1Dropbox.setGeometry(QtCore.QRect(130, 130, 81, 22))
        self.char1Dropbox.setObjectName("char1Dropbox")
        self.char2Dropbox = QtWidgets.QComboBox(PCRJJCAnalyzerGUI)
        self.char2Dropbox.setGeometry(QtCore.QRect(130, 230, 81, 22))
        self.char2Dropbox.setObjectName("char2Dropbox")
        self.char3Dropbox = QtWidgets.QComboBox(PCRJJCAnalyzerGUI)
        self.char3Dropbox.setGeometry(QtCore.QRect(130, 330, 81, 22))
        self.char3Dropbox.setObjectName("char3Dropbox")
        self.char4Dropbox = QtWidgets.QComboBox(PCRJJCAnalyzerGUI)
        self.char4Dropbox.setGeometry(QtCore.QRect(130, 430, 81, 22))
        self.char4Dropbox.setObjectName("char4Dropbox")
        self.char5Dropbox = QtWidgets.QComboBox(PCRJJCAnalyzerGUI)
        self.char5Dropbox.setGeometry(QtCore.QRect(130, 530, 81, 22))
        self.char5Dropbox.setObjectName("char5Dropbox")
        self.resetExclusionCurrentTeamButton = QtWidgets.QPushButton(PCRJJCAnalyzerGUI)
        self.resetExclusionCurrentTeamButton.setGeometry(QtCore.QRect(520, 10, 91, 31))
        self.resetExclusionCurrentTeamButton.setObjectName("resetExclusionCurrentTeamButton")
        self.resetExclusionAllTeamButton = QtWidgets.QPushButton(PCRJJCAnalyzerGUI)
        self.resetExclusionAllTeamButton.setGeometry(QtCore.QRect(620, 10, 91, 31))
        self.resetExclusionAllTeamButton.setObjectName("resetExclusionAllTeamButton")
        self.resetAllButton = QtWidgets.QPushButton(PCRJJCAnalyzerGUI)
        self.resetAllButton.setGeometry(QtCore.QRect(720, 10, 91, 31))
        self.resetAllButton.setObjectName("resetAllButton")
        self.configDialogButton = QtWidgets.QPushButton(PCRJJCAnalyzerGUI)
        self.configDialogButton.setGeometry(QtCore.QRect(720, 610, 91, 31))
        self.configDialogButton.setObjectName("configDialogButton")
        self.updateHandleSelectorListButton = QtWidgets.QPushButton(PCRJJCAnalyzerGUI)
        self.updateHandleSelectorListButton.setGeometry(QtCore.QRect(320, 620, 51, 23))
        self.updateHandleSelectorListButton.setObjectName("updateHandleSelectorListButton")

        self.retranslateUi(PCRJJCAnalyzerGUI)
        QtCore.QMetaObject.connectSlotsByName(PCRJJCAnalyzerGUI)

    def retranslateUi(self, PCRJJCAnalyzerGUI):
        _translate = QtCore.QCoreApplication.translate
        PCRJJCAnalyzerGUI.setWindowTitle(_translate("PCRJJCAnalyzerGUI", "Dialog"))
        self.team3RadioButton.setText(_translate("PCRJJCAnalyzerGUI", "第三队"))
        self.team2RadioButton.setText(_translate("PCRJJCAnalyzerGUI", "第二队"))
        self.team1RadioButton.setText(_translate("PCRJJCAnalyzerGUI", "第一队"))
        self.pushButton.setText(_translate("PCRJJCAnalyzerGUI", "自有角色限制"))
        self.regionSelector.setText(_translate("PCRJJCAnalyzerGUI", "服务器选择"))
        self.setRegion3.setText(_translate("PCRJJCAnalyzerGUI", "日服"))
        self.setRegion2.setText(_translate("PCRJJCAnalyzerGUI", "繁中服"))
        self.setRegion1.setText(_translate("PCRJJCAnalyzerGUI", "简中服"))
        self.recognizeAndSolveButton.setText(_translate("PCRJJCAnalyzerGUI", "识别求解"))
        self.manualSetChar.setText(_translate("PCRJJCAnalyzerGUI", "手动设定阵容"))
        self.TM_CCOEFF_NORMED.setText(_translate("PCRJJCAnalyzerGUI", "TM_CCOEFF_NORMED"))
        self.TMAlgorithm.setText(_translate("PCRJJCAnalyzerGUI", "图像识别算法"))
        self.TM_CCOEFF.setText(_translate("PCRJJCAnalyzerGUI", "TM_CCOEFF"))
        self.TM_CCORR.setText(_translate("PCRJJCAnalyzerGUI", "TM_CCORR"))
        self.TM_CCORR_NORMED.setText(_translate("PCRJJCAnalyzerGUI", "TM_CCORR_NORMED"))
        self.TM_SQDIFF.setText(_translate("PCRJJCAnalyzerGUI", "TM_SQDIFF"))
        self.TM_SQDIFF_NORMED.setText(_translate("PCRJJCAnalyzerGUI", "TM_SQDIFF_NORMED"))
        self.HandleSelector.setText(_translate("PCRJJCAnalyzerGUI", "游戏句柄"))
        self.apiKeyLabel.setText(_translate("PCRJJCAnalyzerGUI", "APIKey"))
        self.queryStatusTag.setText(_translate("PCRJJCAnalyzerGUI", "TextLabel"))
        self.recognizeAndSolveButton_TeamTwoFromHisotry.setText(_translate("PCRJJCAnalyzerGUI", "履历解第二队"))
        self.recognizeAndSolveButton_TeamThreeFromHisotry.setText(_translate("PCRJJCAnalyzerGUI", "履历解第三队"))
        self.recognizeAndSolveButton_OwnTeam.setText(_translate("PCRJJCAnalyzerGUI", "查防守阵容"))
        self.recognizeAndSolveButton_TeamOneFromHisotry.setText(_translate("PCRJJCAnalyzerGUI", "履历解第一队"))
        self.resetExclusionCurrentTeamButton.setText(_translate("PCRJJCAnalyzerGUI", "重置本队锁定"))
        self.resetExclusionAllTeamButton.setText(_translate("PCRJJCAnalyzerGUI", "重置全部锁定"))
        self.resetAllButton.setText(_translate("PCRJJCAnalyzerGUI", "全部重置"))
        self.configDialogButton.setText(_translate("PCRJJCAnalyzerGUI", "设定"))
        self.updateHandleSelectorListButton.setText(_translate("PCRJJCAnalyzerGUI", "刷新"))
