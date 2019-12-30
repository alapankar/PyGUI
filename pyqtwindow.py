import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow): # just creating a subclass of QMainWindow so that we can customize our main window according to our needs
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("My awesome app")
        label=QLabel("This is a PyQt5 window")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)
app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()
