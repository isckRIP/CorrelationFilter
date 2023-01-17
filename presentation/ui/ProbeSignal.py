from PyQt6.QtWidgets import QGroupBox, QLineEdit, QGridLayout, QLabel
from presentation.controller.MainAppController import MainAppController
from presentation.ui.Plots import PlotsCreator


class SignalProbeCreator:
    controller = MainAppController()
    plot = PlotsCreator()


    def createProbeSignal(self):
        _params_in_group_box_ = QGroupBox("Зондирующий сигнал")
        _params_in_group_box_.setMaximumWidth(200)

        self.controller.setSignalProbe(12, 12, 0, 1000, 10)
        self.controller.calculateSignal(self.controller.getSignalProbe())

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
        self.input_frequency_in.setText(str(self.controller.getSignalProbe().frequency))
        self.input_phase_in.setText(str(self.controller.getSignalProbe().phase))
        self.input_amplitude_in.setText(str(self.controller.getSignalProbe().amplitude))



        # Подключаем коннекторы к полям ввода
        self.input_amplitude_in.textEdited.connect(self.controller.changeAmplitudeSignalProbe)
        self.input_amplitude_in.textEdited.connect(lambda: self.plot.updatePlotProbe())
        self.input_amplitude_in.textEdited.connect(lambda: self.plot.updatePlotProbe())
        self.input_frequency_in.textEdited.connect(self.controller.changeFrequencySignalProbe)
        self.input_frequency_in.textEdited.connect(lambda: self.plot.updatePlotProbe())
        self.input_phase_in.textEdited.connect(self.controller.changePhaseSignalProbe)
        self.input_phase_in.textEdited.connect(lambda: self.plot.updatePlotProbe())

        _params_in_group_box_.setLayout(_params_in_)
        return _params_in_group_box_