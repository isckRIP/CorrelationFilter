from PyQt5.QtWidgets import QApplication
from Application.MainApp import MainWindow

import sys


app = QApplication(sys.argv)
window = MainWindow()
window.setFixedSize(1300, 800)
window.show()

app.exec()
