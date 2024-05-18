from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loading(object):
    def setupUi(self, loading):
        loading.setObjectName("loading")
        loading.resize(500, 115)
        loading.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                           "color: rgb(255, 255, 255);")
        self.progressBar = QtWidgets.QProgressBar(loading)
        self.progressBar.setGeometry(QtCore.QRect(30, 37, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)  # Set initial value to 0
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(loading)
        self.label.setGeometry(QtCore.QRect(210, 90, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(loading)
        QtCore.QMetaObject.connectSlotsByName(loading)

    def retranslateUi(self, loading):
        _translate = QtCore.QCoreApplication.translate
        loading.setWindowTitle(_translate("loading", ""))
        self.label.setText(_translate("loading", "LOADING..."))


class Myloading(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_loading()
        self.ui.setupUi(self)

        # Remove maximize, minimize and close button
        self.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint))

        # Start the timer to increment the progress bar
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(100)  # Timer interval in milliseconds
        self.progress = 0

    def update_progress(self):
        self.progress += 5
        self.ui.progressBar.setValue(self.progress)
        if self.progress >= 100:
            self.timer.stop()
            self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    my_loading = Myloading()
    my_loading.show()
    sys.exit(app.exec_())
