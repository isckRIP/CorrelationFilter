from PyQt5.QtWidgets import QTabWidget, QWidget, QVBoxLayout
from pyqtgraph import PlotWidget, PlotCurveItem
from presentation.controller.MainAppController import MainAppController


class PlotsCreator:
    controller = MainAppController
    plot_in = PlotCurveItem()

    def createPlots(self):

        _plots_group_box_ = QTabWidget()

        signals_group_box = QWidget()
        calculations_group_box = QWidget()

        plots_signals = QVBoxLayout()
        plots_calculations = QVBoxLayout()

        # Создаем виджеты графиков
        plot_signal_in = PlotWidget()
        plot_signal_out = PlotWidget()
        plot_signal_product = PlotWidget()


        self.plot_out = PlotCurveItem()
        self.plot_product = PlotCurveItem()

        self.plot_in.setData(self.controller.updatePlotSignalProbe(MainAppController)[0],
                             self.controller.updatePlotSignalProbe(MainAppController)[1])


        plot_signal_in.addItem(self.plot_in)
        plot_signal_out.addItem(self.plot_out)
        plot_signal_product.addItem(self.plot_product)
        plots_signals.addWidget(plot_signal_in)
        plots_signals.addWidget(plot_signal_out)
        plots_calculations.addWidget(plot_signal_product)


        signals_group_box.setLayout(plots_signals)
        calculations_group_box.setLayout(plots_calculations)

        _plots_group_box_.addTab(signals_group_box, "Сигналы")
        _plots_group_box_.addTab(calculations_group_box, "Рассчёты")
        return _plots_group_box_

    def updatePlot(self):
        self.plot_in.setData(self.controller.updatePlotSignalProbe(MainAppController)[0],
                             self.controller.updatePlotSignalProbe(MainAppController)[1])
        print("График обн")
