from PyQt5.QtWidgets import (
    QGridLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
    QDialog,
)
from pyqtgraph import PlotWidget, plot, PlotCurveItem
import pyqtgraph as pg
from PyQt5.QtCore import Qt
from Components.Signal import Signal


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()

        # Создание виджетов
        self.createParamsIn()
        self.createParamsOut()
        self.createPlots()
        self.createMath()

        # Задаем родительскую сетку
        main_layout = QGridLayout()
        main_layout.addWidget(self._params_in_group_box_, 0, 0)
        main_layout.addWidget(self._params_out_group_box_, 0, 1)
        main_layout.addWidget(self._plots_group_box_, 0, 2, 2, 2)
        main_layout.addWidget(self._math_group_box_, 1, 0, 1, 2)

        self.setLayout(main_layout)

        self.setWindowTitle("Корреляционный фильтр")

    # Коннекторы
    def amplitudeInChanged(self, amp):
        self.signal_in.amplitude = int(amp)
        x, y = self.signal_in.calculations()
        self.plot_in.setData(x, y)

    def phaseInChanged(self, ph):
        self.signal_in.phase = int(ph)
        x, y = self.signal_in.calculations()
        self.plot_in.setData(x, y)

    def frequencyInChanged(self, fr):
        self.signal_in.frequency = int(fr)
        x, y = self.signal_in.calculations()
        self.plot_in.setData(x, y)

    def amplitudeOutChanged(self, amp):
        self.signal_out.amplitude = int(amp)
        x, y = self.signal_out.calculations()
        self.plot_out.setData(x, y)

    def phaseOutChanged(self, ph):
        self.signal_out.phase = int(ph)
        x, y = self.signal_out.calculations()
        self.plot_out.setData(x, y)

    def frequencyOutChanged(self, fr):
        self.signal_out.frequency = int(fr)
        x, y = self.signal_out.calculations()
        self.plot_out.setData(x, y)

    # Виджеты
    def createParamsIn(self):
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

        # Устанавливаем значения поумолчанию
        self.input_frequency_in.setText("2")
        self.input_phase_in.setText("0")
        self.input_amplitude_in.setText("5")

        # Подключаем коннекторы к полям ввода
        self.input_amplitude_in.textEdited.connect(self.amplitudeInChanged)
        self.input_phase_in.textEdited.connect(self.phaseInChanged)
        self.input_frequency_in.textEdited.connect(self.frequencyInChanged)

        self._params_in_group_box_.setLayout(_params_in_)

    def createParamsOut(self):
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

        # Устанавливаем значения поумолчанию
        self.input_frequency_out.setText("2")
        self.input_phase_out.setText("0")
        self.input_amplitude_out.setText("5")

        # Подключаем коннекторы к полям ввода
        self.input_amplitude_out.textEdited.connect(self.amplitudeOutChanged)
        self.input_phase_out.textEdited.connect(self.phaseOutChanged)
        self.input_frequency_out.textEdited.connect(self.frequencyOutChanged)

        self._params_out_group_box_.setLayout(_params_out_)

    def createPlots(self):
        self._plots_group_box_ = QGroupBox("Графики")

        plots = QVBoxLayout()

        # Создаем виджеты графиков
        plot_signal_in = PlotWidget()
        plot_signal_out = PlotWidget()

        self.plot_in = PlotCurveItem()
        self.plot_out = PlotCurveItem()

        self.signal_in = Signal(2, 5, 0, 400, 10)
        self.signal_out = Signal(2, 5, 0, 400, 10)

        x_signal_in, y_signal_in = self.signal_in.calculations()
        x_signal_out, y_signal_out = self.signal_out.calculations()
        self.plot_in.setData(x_signal_in, y_signal_in)
        self.plot_out.setData(x_signal_out, y_signal_out)

        plot_signal_in.addItem(self.plot_in)
        plot_signal_out.addItem(self.plot_out)
        plots.addWidget(plot_signal_in)
        plots.addWidget(plot_signal_out)

        self._plots_group_box_.setLayout(plots)

    def createMath(self):
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
