from PyQt5.QtWidgets import QGroupBox, QLineEdit, QGridLayout, QLabel
from presentation.controller.MainAppController import MainAppController
from presentation.ui.Plots import PlotsCreator


class SignalReceivedCreator:
    controller = MainAppController()
    plot = PlotsCreator()

    def createReceivedSignal(self):
        self._params_received_group_box_ = QGroupBox("Принимаемый сигнал")
        self._params_received_group_box_.setMaximumWidth(200)

        self.controller.setSignalReceived(12, 12, 0, 1000, 10)
        self.controller.calculateSignal(self.controller.getSignalReceived())

        # Задаём виджеты полей ввода и их размер
        self.input_frequency_received = QLineEdit()
        self.input_phase_received = QLineEdit()
        self.input_amplitude_received = QLineEdit()
        self.input_frequency_received.setFixedWidth(50)
        self.input_phase_received.setFixedWidth(50)
        self.input_amplitude_received.setFixedWidth(50)

        # Создаем сетку для элементов
        _params_received_ = QGridLayout()
        _params_received_.addWidget(QLabel("Частота (Гц):"), 0, 0)
        _params_received_.addWidget(QLabel("Фаза:"), 1, 0)
        _params_received_.addWidget(QLabel("Амплитуда (мВ):"), 2, 0)
        _params_received_.addWidget(self.input_frequency_received, 0, 1)
        _params_received_.addWidget(self.input_phase_received, 1, 1)
        _params_received_.addWidget(self.input_amplitude_received, 2, 1)
        _params_received_.setColumnStretch(2, 1)

        # Устанавливаем значения поумолчанию
        self.input_frequency_received.setText(str(self.controller.getSignalReceived().frequency))
        self.input_phase_received.setText(str(self.controller.getSignalReceived().phase))
        self.input_amplitude_received.setText(str(self.controller.getSignalReceived().amplitude))

        self.input_amplitude_received.textEdited.connect(self.controller.changeAmplitudeSignalReceived)
        self.input_amplitude_received.textEdited.connect(lambda: self.plot.updatePlotReceived())
        self.input_frequency_received.textEdited.connect(self.controller.changeFrequencySignalReceived)
        self.input_frequency_received.textEdited.connect(lambda: self.plot.updatePlotReceived())
        self.input_phase_received.textEdited.connect(self.controller.changePhaseSignalReceived)
        self.input_phase_received.textEdited.connect(lambda: self.plot.updatePlotReceived())

        self._params_received_group_box_.setLayout(_params_received_)

        return self._params_received_group_box_