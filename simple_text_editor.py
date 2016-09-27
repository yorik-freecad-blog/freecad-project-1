#!/usr/bin/env python
# simple text editor
import sys, os
from PySide.QtGui import QApplication, QMainWindow, QStatusBar
from PySide.QtGui import QTextEdit, QAction, QMessageBox
from PySide.QtGui import QIcon, QKeySequence

class MainWindow(QMainWindow):
	"""docstring for MainWindow"""
	def __init__(self):
		super(MainWindow,self).__init__()
		self.initGui()

	def initGui(self):
		self.setWindowTitle('Aeneid Text Editor')
		self.setWindowIcon(QIcon())
		self.setGeometry(300,300, 400,300)
		self.setupComponents()
		self.show()

	def setupComponents(self):
		""" Function to setup status bar, central widget
			and menu bar
		"""
		self.myStatusBar = QStatusBar()
		self.setStatusBar(self.myStatusBar)
		self.myStatusBar.showMessage('Ready', 10000)
		self.textEdit=QTextEdit()
		self.setCentralWidget(self.textEdit)

		# 
		self.createActions()
		self.createMenus()

		#
		self.fileMenu.addAction(self.newAction)
		self.fileMenu.addSeparator()
		self.fileMenu.addAction(self.exitAction)
		self.fileMenu.addSeparator()
		self.editMenu.addAction(self.copyAction)
		self.editMenu.addSeparator()
		self.editMenu.addAction(self.pasteAction)
		self.helpMenu.addAction(self.aboutAction)

	# slots called when the menu actions are triggered
	def newFile(self):
		self.textEdit.setText('Aeneid Applicatioon')

	def exitFile(self):
		self.close()

	def aboutHelp(self):
		QMessageBox.about( self, 
						   "About Simple Text Editor", 
						   "Demonstrate use of menu bar")

	def createActions(self):
		""" Function to create actions for menus
		"""
		self.newAction=QAction( QIcon(), '&New', 
								self, 
								shortcut=QKeySequence.New, 
								statusTip="Create a New file" )
		self.exitAction=QAction( QIcon(), '&Exit',
								 self,
								 shortcut="Ctrl+Q",
								 statusTip="Exit the application",
								 triggered=self.exitFile )
		self.copyAction=QAction( QIcon(), '&Copy',
								 self,
								 shortcut="Ctrl+C",
								 statusTip="Copy",
								 triggered=self.textEdit.copy )
		self.pasteAction=QAction( QIcon(), '&Paste',
								  self,
								  shortcut="Ctrl+V",
								  triggered=self.textEdit.paste)
		self.aboutAction=QAction( QIcon(), '&About',
								  self,
								  statusTip="Displays info",
								  triggered=self.aboutHelp )

	# Actual menu bar item creation
	def createMenus(self):
		""" Function to create actual menu bar
		"""
		self.fileMenu = self.menuBar().addMenu("&File")
		self.editMenu = self.menuBar().addMenu("&Edit")
		self.helpMenu = self.menuBar().addMenu("&Help")

if __name__=='__main__':
	try:
		Aeneid_app=QApplication(sys.argv)
		Aeneid_win=MainWindow()
		sys.exit( Aeneid_app.exec_() )
	except NameError: print("Name Error: ", sys.exc_info()[1])
	except SystemExit: print("Closing Window...")
	except Exception: print (sys.exc_info()[1])