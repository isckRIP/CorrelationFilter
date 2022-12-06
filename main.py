from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QMenu
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction
from random import choice
from Components.Test import MainWindow

import sys

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
