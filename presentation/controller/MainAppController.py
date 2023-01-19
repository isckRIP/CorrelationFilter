from data.AppRepositoryImpl import AppRepositoryImpl
from domain.entity.GraphOfSignal import GraphOfSignal
from domain.entity.SignalSin import SignalSin
from domain.entity.SignalProduct import SignalProduct


class MainAppController:
    impl = AppRepositoryImpl()
    signal_probe = SignalSin(0, 0, 0, 0, 0,  [], [])
    signal_received = SignalSin(0, 0, 0, 0, 0, [], [])
    signal_product = SignalProduct([], [])

    def calculateSignal(self, signal):
        graph_of_signal = GraphOfSignal
        self.impl.getGraphOfSignal(signal)
        return graph_of_signal.x, graph_of_signal.y

    def updatePlotSignalProbe(self):
        x = self.calculateSignal(MainAppController, self.signal_probe)[0]
        y = self.calculateSignal(MainAppController, self.signal_probe)[1]
        self.signal_probe.x = x
        self.signal_probe.y = y
        self.updatePlotSignalProduct(MainAppController)
        return x, y

    def getSignalProbe(self):
        return self.signal_probe

    def setSignalProbe(self, fr, amp, ph, dur, time):
        self.signal_probe.frequency = fr
        self.signal_probe.amplitude = amp
        self.signal_probe.phase = ph
        self.signal_probe.duration = dur
        self.signal_probe.time = time

    def changeAmplitudeSignalProbe(self, amp):
        self.signal_probe.amplitude = float(amp)
        self.calculateSignal(self.signal_probe)

    def changePhaseSignalProbe(self, ph):
        self.signal_probe.phase = float(ph)
        self.calculateSignal(self.signal_probe)

    def changeFrequencySignalProbe(self, fr):
        self.signal_probe.frequency = float(fr)
        self.calculateSignal(self.signal_probe)

    def updatePlotSignalReceived(self):
        x = self.calculateSignal(MainAppController, self.signal_received)[0]
        y = self.calculateSignal(MainAppController, self.signal_received)[1]
        self.signal_received.x = x
        self.signal_received.y = y
        self.updatePlotSignalProduct(MainAppController)
        return x, y

    def getSignalReceived(self):
        return self.signal_received

    def setSignalReceived(self, fr, amp, ph, dur, time):
        self.signal_received.frequency = fr
        self.signal_received.amplitude = amp
        self.signal_received.phase = ph
        self.signal_received.duration = dur
        self.signal_received.time = time

    def changeAmplitudeSignalReceived(self, amp):
        self.signal_received.amplitude = float(amp)
        self.calculateSignal(self.signal_received)

    def changePhaseSignalReceived(self, ph):
        self.signal_received.phase = float(ph)
        self.calculateSignal(self.signal_received)

    def changeFrequencySignalReceived(self, fr):
        self.signal_received.frequency = float(fr)
        self.calculateSignal(self.signal_received)

    def multiplySignals(self):
        x, y = self.impl.multiplyGraphOfSignals([self.signal_probe, self.signal_received])
        return x, y

    def updatePlotSignalProduct(self):
        x, y = self.multiplySignals(MainAppController)
        self.signal_product.x = x
        self.signal_product.y = y
        return self.signal_product.x, self.signal_product.y
