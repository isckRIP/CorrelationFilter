from PyQt5.QtWidgets import QTabWidget, QWidget, QVBoxLayout
from pyqtgraph import PlotWidget, PlotCurveItem
from domain.entity.Signal import Signal


def createPlots(self):

    self._plots_group_box_ = QTabWidget()

    signals_group_box = QWidget()
    calculations_group_box = QWidget()

    plots_signals = QVBoxLayout()
    plots_calculations = QVBoxLayout()

    # Создаем виджеты графиков
    plot_signal_in = PlotWidget()
    plot_signal_out = PlotWidget()
    plot_signal_product = PlotWidget()

    self.plot_in = PlotCurveItem()
    self.plot_out = PlotCurveItem()
    self.plot_product = PlotCurveItem()


    # self.signal_in = Signal(2, 5, 0, 400, 10)
    # self.signal_out = Signal(2, 5, 0, 400, 10)
    # self.signal_product = Signal(2, 5, 0, 400, 10)
    #
    # x_signal_in, y_signal_in = self.signal_in.calculationsSingnal()
    # x_signal_out, y_signal_out = self.signal_out.calculationsSingnal()
    # x_signal_product, y_signal_product = self.signal_product.calculationsSingnal()
    # self.plot_in.setData(x_signal_in, y_signal_in)
    # self.plot_out.setData(x_signal_out, y_signal_out)
    # self.plot_product.setData(x_signal_product, y_signal_product)

    plot_signal_in.addItem(self.plot_in)
    plot_signal_out.addItem(self.plot_out)
    plot_signal_product.addItem(self.plot_product)
    plots_signals.addWidget(plot_signal_in)
    plots_signals.addWidget(plot_signal_out)
    plots_calculations.addWidget(plot_signal_product)

    signals_group_box.setLayout(plots_signals)
    calculations_group_box.setLayout(plots_calculations)

    self._plots_group_box_.addTab(signals_group_box, "Сигналы")
    self._plots_group_box_.addTab(calculations_group_box, "Рассчёты")
    return self