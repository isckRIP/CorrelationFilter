from PyQt6.QtWidgets import QApplication
from Application.MainApp import MainWindow

import sys


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
