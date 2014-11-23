#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import Image

from PySide import QtGui, QtCore
print QtGui.__file__
from ui_demain import Ui_Demain
from mapviewer import MapViewer

class MainWindow(QtGui.QWidget, Ui_Demain):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		self.show()
		
		self.scene = QtGui.QGraphicsScene(self)
		self.mapViewer = MapViewer(self.scene, self.scrollArea)
		
		#Add map
		pixmap = QtGui.QPixmap("images/finca-pia.jpg")
		pixmapScaled = pixmap.scaled(self.scrollArea.width(),self.scrollArea.height())
		self.scene.addPixmap(pixmapScaled)
				 
		fecha = QtCore.QDate.currentDate()
		self.calendarWidget.setDateRange(fecha.addDays(-100), fecha.addDays(365))
		self.calendarWidget.setSelectedDate(fecha)
		
		model = QtGui.QStandardItemModel(20,2,self)
		model.setHorizontalHeaderItem(0,QtGui.QStandardItem(u'Fecha'))
		model.setHorizontalHeaderItem(1,QtGui.QStandardItem(u'Acción'))
		self.tableView.horizontalHeader().setStretchLastSection(True)
		self.tableView.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignCenter)
		
		f = QtGui.QStandardItem(fecha.toString(QtCore.Qt.SystemLocaleShortDate))
		model.setItem(0,0,f);
		a = QtGui.QStandardItem("Esquilar")
		model.setItem(0,1,a);
	
		self.tableView.setModel(model)
		
		#CONNECTION
		self.timeSlider.sliderMoved.connect(self.barChanged)
		self.dateEdit.dateChanged.connect(self.sliderChanged)
		self.calendarWidget.clicked.connect(self.calendarChanged)

	@QtCore.Slot(str)
	def barChanged(self,days): 
		date = QtCore.QDate.currentDate()
		corDate = date.addDays(days)
		self.calendarWidget.setSelectedDate(corDate) 
		self.dateEdit.setDate(corDate)
	
	@QtCore.Slot(str)
	def sliderChanged(self,date):
		self.calendarWidget.setSelectedDate(date) 
		self.timeSlider.setValue(QtCore.QDate.currentDate().daysTo(date))
		
	@QtCore.Slot(str)
	def calendarChanged(self,date):
		self.dateEdit.setDate(date)
		self.timeSlider.setValue(QtCore.QDate.currentDate().daysTo(date))
	
    
if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	frame = MainWindow()
	frame.show()    
	app.exec_()