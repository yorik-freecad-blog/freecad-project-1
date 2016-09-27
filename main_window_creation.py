# pyside main window creation
#
import sys, time
from PySide.QtGui import QMainWindow, QApplication
from PySide.QtGui import QLabel, QRadioButton


class AeneidWindow(QMainWindow):
	def __init__(self):
		super(AeneidWindow, self).__init__()
		self.initGui()

	def initGui(self):
		self.setWindowTitle("Aeneid Window")
		self.setGeometry(200,100,400,200)
		# label
		self.label1=QLabel('today me, tomorrow the world!', self)
		self.label1.setFont('Arial')
		self.label1.move(20,10)
		# check box creation
		self.checkbox1=QCheckBox('OK', self)
		self.checkbox1.clicked.connect(self.onCheckBox1)
		self.checkbox1.toggle()

		# Radio buttons
		self.radioButton=QRadioButton('click me', self)
		self.radioButton.clicked.connect(self.onRadioButton)
		

		# ok cancel button
		self
		self.show()

# main
if __name__=="__main__":
	try:
		aeneidApp=QApplication(sys.argv)
		aeneidWindow=AeneidWindow()
		aeneidApp.exec_()
		sys.exit(0)
	except NameError:
		print("Name error: ", sys.exc_info()[1])
	except SystemExit:
		print("Closing Window...")
	except Exception:
		print(sys.exc_info())
