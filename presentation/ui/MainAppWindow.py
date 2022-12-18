from PyQt5.QtWidgets import QDialog, QGridLayout
from presentation.ui.ProbeSignal import createProbeSignal
from presentation.ui.ReceivedSignal import createReceivedSignal
from presentation.ui.Plots import createPlots
from presentation.ui.SignalSettings import createSignalSettings


class MainAppWindow(QDialog):
    def __init__(self):
        super().__init__()

        main_layout = QGridLayout()
        main_layout.addWidget(createProbeSignal(self)._params_in_group_box_, 0, 0)
        main_layout.addWidget(createReceivedSignal(self)._params_out_group_box_, 0, 1)
        main_layout.addWidget(createPlots(self)._plots_group_box_, 0, 2, 2, 2)
        main_layout.addWidget(createSignalSettings(self)._math_group_box_, 1, 0, 1, 2)

        self.setLayout(main_layout)

        self.setWindowTitle("Корреляционный фильтр")
