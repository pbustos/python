# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demain.ui'
#
# Created: Sun Nov 23 23:18:31 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Demain(object):
    def setupUi(self, Demain):
        Demain.setObjectName("Demain")
        Demain.resize(1262, 834)
        self.calendarWidget = QtGui.QCalendarWidget(Demain)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 650, 361, 191))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setHorizontalHeaderFormat(QtGui.QCalendarWidget.SingleLetterDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtGui.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setObjectName("calendarWidget")
        self.frame_2 = QtGui.QFrame(Demain)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1261, 91))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.timeSlider = QtGui.QSlider(self.frame_2)
        self.timeSlider.setGeometry(QtCore.QRect(20, 30, 1111, 29))
        self.timeSlider.setMinimum(-100)
        self.timeSlider.setMaximum(366)
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setInvertedAppearance(False)
        self.timeSlider.setInvertedControls(False)
        self.timeSlider.setObjectName("timeSlider")
        self.dateEdit = QtGui.QDateEdit(self.frame_2)
        self.dateEdit.setGeometry(QtCore.QRect(1140, 10, 110, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.scrollArea = QtGui.QScrollArea(Demain)
        self.scrollArea.setGeometry(QtCore.QRect(360, 90, 901, 751))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 899, 749))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tableView = QtGui.QTableView(Demain)
        self.tableView.setGeometry(QtCore.QRect(0, 90, 361, 561))
        self.tableView.setObjectName("tableView")

        self.retranslateUi(Demain)
        QtCore.QMetaObject.connectSlotsByName(Demain)

    def retranslateUi(self, Demain):
        Demain.setWindowTitle(QtGui.QApplication.translate("Demain", "Demain", None, QtGui.QApplication.UnicodeUTF8))

