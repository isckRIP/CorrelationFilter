from PyQt5.QtWidgets import QGroupBox, QLineEdit, QGridLayout, QLabel


def createReceivedSignal(self):
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
    # self.input_amplitude_out.textEdited.connect(self.amplitudeOutChanged)
    # self.input_phase_out.textEdited.connect(self.phaseOutChanged)
    # self.input_frequency_out.textEdited.connect(self.frequencyOutChanged)

    self._params_out_group_box_.setLayout(_params_out_)
    return self