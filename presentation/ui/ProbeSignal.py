from PyQt5.QtWidgets import QGroupBox, QLineEdit, QGridLayout, QLabel


def createProbeSignal(self):
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
    # self.input_amplitude_in.textEdited.connect(self.amplitudeInChanged)
    # self.input_phase_in.textEdited.connect(self.phaseInChanged)
    # self.input_frequency_in.textEdited.connect(self.frequencyInChanged)

    self._params_in_group_box_.setLayout(_params_in_)
    return self
