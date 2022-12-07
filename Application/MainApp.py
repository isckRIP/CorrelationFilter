from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QPushButton, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QColor, QPalette


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Корреляционный фильтр")

        # Элементы интерфейса
        self.button_generate = QPushButton("Рассчитать")
        label_frequency = QLabel("Частота:")
        label_phase = QLabel("Фаза:")
        label_amplitude = QLabel("Амплитуда:")
        label_duration = QLabel("Частота дискретизации:")
        label_time = QLabel("Время:")
        label_probing_signal = QLabel("Зондирующий сигнал")
        label_reflected_signal = QLabel("Отражённый сигнал:")
        label_plots = QLabel("Грфики:")
        label_params = QLabel("Параметры сигналов:")
        input_frequency_in = QLineEdit()
        input_phase_in = QLineEdit()
        input_amplitude_in = QLineEdit()
        input_frequency_out = QLineEdit()
        input_phase_out = QLineEdit()
        input_amplitude_out = QLineEdit()
        input_duration = QLineEdit()
        input_time = QLineEdit()

        layout = QHBoxLayout()

        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))

        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)