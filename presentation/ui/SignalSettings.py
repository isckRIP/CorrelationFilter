from PyQt5.QtWidgets import QGroupBox, QGridLayout, QLineEdit, QDial, QLabel


def createSignalSettings(self):
    self._math_group_box_ = QGroupBox("Настройки графиков")

    math = QGridLayout()

    # Создаем виджеты
    self.input_duration = QLineEdit()
    self.input_time = QLineEdit()
    self.dial_time = QDial()
    self.dial_duration = QDial()

    # Устанавливаем настройки виджетов
    self.dial_time.setMaximum(100)
    self.dial_time.setMinimum(0)
    self.dial_duration.setFixedWidth(150)
    self.dial_duration.setMaximum(4800)
    self.dial_duration.setMinimum(10)
    self.dial_time.setFixedWidth(150)
    self.input_time.setFixedWidth(50)
    self.input_duration.setFixedWidth(50)

    # Добавляем виджеты в сетку
    math.addWidget(QLabel("Частота дискретизации:"), 0, 0)
    math.addWidget(QLabel("Время:"), 0, 1)
    math.addWidget(self.dial_duration, 1, 0)
    math.addWidget(self.dial_time, 1, 1)

    # Подключаем коннекторы
    # self.dial_duration.valueChanged.connect(self.durationIsChanged)
    # self.dial_time.valueChanged.connect(self.timeIsChanged)

    self._math_group_box_.setLayout(math)
    return self