from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Ui_searching(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_searching, self).__init__()
        uic.loadUi("Searching.ui", self)

        self.pushButton_2.clicked.connect(self.closeWindow)

    def closeWindow(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window1 = Ui_searching()
    window1.show()
    sys.exit(app.exec_())
