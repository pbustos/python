#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PySide import QtGui, QtCore

class MapViewer(QtGui.QGraphicsView):
	def __init__(self, scene, parent=None):
		super(MapViewer, self).__init__(scene, parent)
	
		self.setSceneRect(0,0, parent.width(), parent.height())
		self.show()
	
		##self.frame = parent
		##print parent.width(), parent.height()
		##self.scene = QtGui.QGraphicsScene()
		##self.view = QtGui.QGraphicsView(self.scene)
		#self.show()
		#self.setScene(scene)
		
	##def setBackgroundImage(self,imagePath):
		##pixmap = QtGui.QPixmap(imagePath)
		##pixmapScaled = pixmap.scaled(self.frame.width(), self.frame.height())
		##self.scene.addPixmap(pixmapScaled)
		##self.view.show()
		
	#def drawCerca(self):
		#poly = QtGui.QPolygonF()
		#poly.append(QtCore.QPointF(350.0,150.0))
		#poly.append(QtCore.QPointF(700.0,150.0))
		#poly.append(QtCore.QPointF(700.0,500.0))
		#poly.append(QtCore.QPointF(350.0,500))
		#self.scene().addPolygon(poly,QtGui.QPen(QtCore.Qt.magenta,5))
		#self.show()

	#def showEvent(self, event) :
		#self.fitInView(self.scene().sceneRect(),QtGui.KeepAspectRatio);

	
	def mousePressEvent(self, event):
		if event.button() == QtCore.Qt.LeftButton:
			print "Pressed"