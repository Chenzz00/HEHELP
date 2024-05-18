from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget
from View_Masterlist import Ui_Masterlist

class Ui_Loading(object):
    def setupUi(self, Loading):
        Loading.setObjectName("Loading")
        Loading.resize(500, 115)
        Loading.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                              "color: rgb(255, 255, 255);")
        self.progressBar = QtWidgets.QProgressBar(Loading)
        self.progressBar.setGeometry(QtCore.QRect(30, 37, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(Loading)
        self.label.setGeometry(QtCore.QRect(210, 10, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Loading)
        QtCore.QMetaObject.connectSlotsByName(Loading)
        

    def retranslateUi(self, Loading):
        _translate = QtCore.QCoreApplication.translate
        Loading.setWindowTitle(_translate("Loading", "Form"))
        self.label.setText(_translate("Loading", "LOADING..."))


class LoadingWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Loading()
        self.ui.setupUi(self)
        

        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.FramelessWindowHint)


        # Set up timer for updating progress
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.progress = 0
        self.timer.start(100)  # Update every 100 milliseconds

    def update_progress(self):
        self.progress += 5
        self.ui.progressBar.setValue(self.progress)
        if self.progress >= 100:
            self.timer.stop()
            self.close()
            

    

    
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loading_window = LoadingWindow()
    loading_window.show()
    sys.exit(app.exec_())
