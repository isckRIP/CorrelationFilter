from PyQt6.QtWidgets import QDialog, QGridLayout
from presentation.ui.ProbeSignal import SignalProbeCreator
from presentation.ui.ReceivedSignal import SignalReceivedCreator
from presentation.ui.Plots import PlotsCreator
from presentation.ui.SignalSettings import SignalSettingsCreator


class MainAppWindow(QDialog):

    def __init__(self):
        super().__init__()

        main_layout = QGridLayout()
        main_layout.addWidget(SignalProbeCreator.createProbeSignal(SignalProbeCreator), 0, 0)
        main_layout.addWidget(SignalReceivedCreator.createReceivedSignal(SignalReceivedCreator), 0, 1)
        main_layout.addWidget(PlotsCreator.createPlots(PlotsCreator), 0, 2, 2, 2)
        main_layout.addWidget(SignalSettingsCreator.createSignalSettings(SignalSettingsCreator), 1, 0, 1, 2)

        self.setLayout(main_layout)

        self.setWindowTitle("Корреляционный фильтр")
