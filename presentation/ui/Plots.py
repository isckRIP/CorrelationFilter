from PyQt6.QtWidgets import QTabWidget, QWidget, QVBoxLayout
from pyqtgraph import PlotWidget, PlotCurveItem
from presentation.controller.MainAppController import MainAppController


class PlotsCreator:
    controller = MainAppController()
    plot_probe = PlotCurveItem()
    plot_received = PlotCurveItem()
    plot_product = PlotCurveItem()
    plot_integrate = PlotCurveItem()

    def createPlots(self):
        plots_group_box = QTabWidget()
        signals_group_box = QWidget()
        calculations_group_box = QWidget()
        plots_signals = QVBoxLayout()
        plots_calculations = QVBoxLayout()

        # Создаем виджеты графиков
        plot_signal_in = PlotWidget()
        plot_signal_out = PlotWidget()
        plot_signal_product = PlotWidget()
        plot_signal_integrate = PlotWidget()

        # Устанавливаем координаты графиков
        self.plot_probe.setData(self.controller.updatePlotSignalProbe()[0],
                                self.controller.updatePlotSignalProbe()[1])
        self.plot_received.setData(self.controller.updatePlotSignalReceived()[0],
                                   self.controller.updatePlotSignalReceived()[1])
        self.plot_product.setData(self.controller.updatePlotSignalProduct()[0],
                                  self.controller.updatePlotSignalProduct()[1])
        self.plot_integrate.setData(self.controller.updatePlotIntegrate()[0],
                                    self.controller.updatePlotIntegrate()[1])

        plot_signal_in.addItem(self.plot_probe)
        plot_signal_out.addItem(self.plot_received)
        plot_signal_product.addItem(self.plot_product)
        plot_signal_integrate.addItem(self.plot_integrate)
        plots_signals.addWidget(plot_signal_in)
        plots_signals.addWidget(plot_signal_out)
        plots_calculations.addWidget(plot_signal_product)
        plots_calculations.addWidget(plot_signal_integrate)

        signals_group_box.setLayout(plots_signals)
        calculations_group_box.setLayout(plots_calculations)

        plots_group_box.addTab(signals_group_box, "Сигналы")
        plots_group_box.addTab(calculations_group_box, "Рассчёты")
        return plots_group_box

    # Обновление графиков
    def updatePlotProbe(self):
        self.plot_probe.setData(self.controller.updatePlotSignalProbe()[0],
                                self.controller.updatePlotSignalProbe()[1])

    def updatePlotReceived(self):
        self.plot_received.setData(self.controller.updatePlotSignalReceived()[0],
                                   self.controller.updatePlotSignalReceived()[1])

    def updatePlotProduct(self):
        self.plot_product.setData(self.controller.updatePlotSignalProduct()[0],
                                  self.controller.updatePlotSignalProduct()[1])

    def updatePlotIntegrate(self):
        self.plot_integrate.setData(self.controller.updatePlotIntegrate()[0],
                                    self.controller.updatePlotIntegrate()[1])

    def updateAll(self):
        self.updatePlotIntegrate()
        self.updatePlotProduct()
        self.updatePlotReceived()
        self.updatePlotProbe()
