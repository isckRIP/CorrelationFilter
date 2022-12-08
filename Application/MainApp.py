from PyQt5.QtWidgets import (
    QGridLayout,
    QWidget,
    QPushButton,
    QLabel,
    QLineEdit,
    QHBoxLayout,
    QVBoxLayout,
    QGroupBox,
    QLayout,
    QDialog,
    QSpacerItem,
    QSizePolicy
)
from PyQt5.QtCore import Qt



class MainWindow(QDialog):
    def __init__(self):
        super().__init__()

        # Создание виджетов
        self.create_params_in()
        self.create_params_out()
        self.create_plots()
        self.create_math()

        # Задаем родительскую сетку
        main_layout = QGridLayout()
        main_layout.addWidget(self._params_in_group_box_, 0, 0)
        main_layout.addWidget(self._params_out_group_box_, 0, 1)
        main_layout.addWidget(self._plots_group_box_, 0, 2, 2, 2)
        main_layout.addWidget(self._math_group_box_, 1, 0, 1, 2)

        self.setLayout(main_layout)

        self.setWindowTitle("Корреляционный фильтр")

    def create_params_in(self):
        self._params_in_group_box_ = QGroupBox("Зондирующий сигнал")
        self._params_in_group_box_.setMaximumWidth(200)

        # Задаём виджеты полей ввода и их размер
        self.input_frequency_in = QLineEdit()
        self.input_phase_in = QLineEdit()
        self.input_amplitude_in = QLineEdit()
        self.input_frequency_in.setFixedWidth(50)
        self.input_phase_in.setFixedWidth(50)
        self.input_amplitude_in.setFixedWidth(50)

        # Создаем сетку для элементов
        _params_in_ = QGridLayout()
        _params_in_.addWidget(QLabel("Частота (Гц):"), 0, 0)
        _params_in_.addWidget(QLabel("Фаза:"), 1, 0)
        _params_in_.addWidget(QLabel("Амплитуда (мВ):"), 2, 0)
        _params_in_.addWidget(self.input_frequency_in, 0, 1)
        _params_in_.addWidget(self.input_phase_in, 1, 1)
        _params_in_.addWidget(self.input_amplitude_in, 2, 1)
        _params_in_.setColumnStretch(2, 1)

        self._params_in_group_box_.setLayout(_params_in_)

    def create_params_out(self):
        self._params_out_group_box_ = QGroupBox("Принимаемый сигнал")
        self._params_out_group_box_.setMaximumWidth(200)

        # Задаём виджеты полей ввода и их размер
        self.input_frequency_out = QLineEdit()
        self.input_phase_out = QLineEdit()
        self.input_amplitude_out = QLineEdit()
        self.input_frequency_out.setFixedWidth(50)
        self.input_phase_out.setFixedWidth(50)
        self.input_amplitude_out.setFixedWidth(50)

        # Создаем сетку для элементов
        _params_out_ = QGridLayout()
        _params_out_.addWidget(QLabel("Частота (Гц):"), 0, 0)
        _params_out_.addWidget(QLabel("Фаза:"), 1, 0)
        _params_out_.addWidget(QLabel("Амплитуда (мВ):"), 2, 0)
        _params_out_.addWidget(self.input_frequency_out, 0, 1)
        _params_out_.addWidget(self.input_phase_out, 1, 1)
        _params_out_.addWidget(self.input_amplitude_out, 2, 1)
        _params_out_.setColumnStretch(2, 1)

        self._params_out_group_box_.setLayout(_params_out_)

    def create_plots(self):
        self._plots_group_box_ = QGroupBox("Графики")

        plots = QVBoxLayout()

        self._plots_group_box_.setLayout(plots)

    def create_math(self):
        self._math_group_box_ = QGroupBox("Настройки графиков")

        math = QGridLayout()

        self.button_generate = QPushButton("Отрисовать")
        self.input_duration = QLineEdit()
        self.input_time = QLineEdit()
        self.input_time.setFixedWidth(50)
        self.input_duration.setFixedWidth(50)

        math.addWidget(QLabel("Частота дискретизации:"), 0, 0)
        math.addWidget(QLabel("Время:"), 1, 0)
        math.addWidget(self.input_duration, 0, 1)
        math.addWidget(self.input_time, 1, 1)
        math.addWidget(self.button_generate, 2, 2, 1, 2)
        math.setColumnStretch(2, 1)

        self._math_group_box_.setLayout(math)
