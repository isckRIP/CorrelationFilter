from PyQt5.QtWidgets import QApplication
# from Application.MainApp import MainWindow
from presentation.ui.MainAppWindow import MainAppWindow

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # window = MainWindow()
    window = MainAppWindow()
    window.setMinimumSize(1200, 600)
    window.show()
    sys.exit(app.exec())

