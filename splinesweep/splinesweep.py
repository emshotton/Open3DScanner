#!/usr/bin/python

#Splinesweep software.
#Version 1.0 - Withnail
#by Matthew Shotton
#licenced under GPLv3.0 see http://www.gnu.org/licenses/gpl-3.0.txt

import sys
from PyQt4 import QtGui


class GUI(QtGui.QWidget):
    def __init__(self):
        super(GUI, self).__init__()
        self.__initUI()
        
    def __initUI(self):
        layout = QtGui.QGridLayout()
        self.setLayout(layout)
        self.setWindowTitle('Splinesweep v1.0 - \"Withnail\"')
        self.resize(300, 300)

app = QtGui.QApplication(sys.argv)
ex = GUI()
ex.show()
sys.exit(app.exec_())
