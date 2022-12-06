from PyQt6.QtWidgets import QMainWindow, QGridLayout, QWidget, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Корреляционный фильтр")
        button = QPushButton()
        button1 = QPushButton()

        layout = QGridLayout()

        widget = QWidget()
        widget.setLayout(layout)

        layout.addWidget(button, 0, 1)
        layout.addWidget(button1, 0, 0)

        self.setCentralWidget(widget)

