from PyQt6.QtWidgets import QGroupBox, QGridLayout, QLineEdit, QDial, QLabel
from presentation.controller.MainAppController import MainAppController
from presentation.ui.Plots import PlotsCreator


class SignalSettingsCreator:
    controller = MainAppController()
    plot = PlotsCreator()
    math = QGridLayout()

    def createSignalSettings(self):
        # Создаем виджеты
        self.math_group_box = QGroupBox("Настройки графиков")
        self.input_duration = QLineEdit()
        self.input_time = QLineEdit()
        self.dial_time = QDial()
        self.dial_duration = QDial()

        # Устанавливаем настройки виджетов
        self.dial_time.setMaximum(100)
        self.dial_time.setMinimum(1)
        self.dial_duration.setFixedWidth(150)
        self.dial_duration.setMaximum(4800)
        self.dial_duration.setMinimum(10)
        self.dial_time.setFixedWidth(150)
        self.input_time.setFixedWidth(50)
        self.input_duration.setFixedWidth(50)

        # Добавляем виджеты в сетку
        self.math.addWidget(QLabel("Частота дискретизации:"), 0, 0)
        self.math.addWidget(QLabel("Время:"), 0, 1)
        self.math.addWidget(self.dial_duration, 1, 0)
        self.math.addWidget(self.dial_time, 1, 1)

        # Подключаем коннекторы
        self.dial_time.valueChanged.connect(self.controller.changeTimePlots)
        self.dial_time.valueChanged.connect(lambda: self.plot.updateAll())
        self.dial_duration.valueChanged.connect(self.controller.changeDurationPlots)
        self.dial_duration.valueChanged.connect(lambda: self.plot.updateAll())

        self.math_group_box.setLayout(self.math)
        return self.math_group_box
