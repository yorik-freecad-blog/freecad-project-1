#!/usr/bin/env python

import os, sys
from PySide.QtGui import QApplication, QFileDialog, QMainWindow

class Aeneid_FileDialog(QMainWindow):
	"""docstring for Aeneid_FileDialog"QMainWindow"""
	def __init__(self):
		super(Aeneid_FileDialog, self).__init__()
		self.initGui()

	def initGui(self):
		