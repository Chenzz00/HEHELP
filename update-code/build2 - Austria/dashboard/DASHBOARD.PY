from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class Ui_dashboard(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_dashboard, self).__init__()
        uic.loadUi("Dashboard_Transaction_with_icon.ui", self)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  
        self.pushButton_2.clicked.connect(self.openSearch)
        
        
        self.update_time()

    def openSearch(self):
        from searching import Ui_searching
        self.window = Ui_searching()  
        self.window.setWindowModality(Qt.ApplicationModal) 
        self.window.show()

    def update_time(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        time_text = current_time.toString("hh:mm:ss AP")
        date_text = current_date.toString("MM/dd/yy")
        self.label.setText(f"{time_text}  {date_text}")
        font = self.label.font()
        font.setPointSize(45)  
        self.label.setFont(font)

app = QtWidgets.QApplication(sys.argv)
window = Ui_dashboard()
window.show()
app.exec_()
