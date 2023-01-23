from PyQt6.QtWidgets import QApplication
from presentation.ui.MainAppWindow import MainAppWindow

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainAppWindow()
    window.setMinimumSize(1200, 600)
    window.show()
    sys.exit(app.exec())
