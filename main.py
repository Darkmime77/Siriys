import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
)
from avtor import Ui_MainWindow

class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

app = QApplication([])
AppWindow = AppWindow()
AppWindow.show()
sys.exit(app.exec())