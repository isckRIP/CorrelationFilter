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
    QDialog
)



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

        self.label_frequency_in = QLabel()
        self.label_phase_in = QLabel()

        _params_in_ = QGridLayout()
        _params_in_.addWidget(self.label_frequency_in, 0, 0)
        _params_in_.addWidget(self.label_phase_in, 1, 0)

        self._params_in_group_box_.setLayout(_params_in_)

    def create_params_out(self):
        self._params_out_group_box_ = QGroupBox("Принимаемый сигнал")

        self.label_frequency_out = QLabel()
        self.label_phase_out = QLabel()

        _params_out_ = QGridLayout()
        _params_out_.addWidget(self.label_frequency_out, 0, 0)
        _params_out_.addWidget(self.label_phase_out, 1, 0)

        self._params_out_group_box_.setLayout(_params_out_)

    def create_plots(self):
        self._plots_group_box_ = QGroupBox("Графики")

        plots = QVBoxLayout()

        self._plots_group_box_.setLayout(plots)

    def create_math(self):
        self._math_group_box_ = QGroupBox("Настройки графиков")

        math = QGridLayout()

        self._math_group_box_.setLayout(math)
