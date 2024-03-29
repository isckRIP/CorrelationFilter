from data.AppRepositoryImpl import AppRepositoryImpl
from domain.entity.SignalSin import SignalSin
from domain.entity.GraphOfSignal import GraphOfSignal


class MainAppController:
    impl = AppRepositoryImpl()
    signal_probe = SignalSin(0, 0, 0, 0, 0, [], [])
    signal_received = SignalSin(0, 0, 0, 0, 0, [], [])
    signal_product = GraphOfSignal([], [])
    signal_integrate = GraphOfSignal([], [])
    signal_threshold = GraphOfSignal([], [])

    def calculateSignal(self, signal):
        graph_of_signal = GraphOfSignal
        self.impl.getGraphOfSignal(signal)
        return graph_of_signal.x, graph_of_signal.y

    def updatePlotSignalProbe(self):
        x = self.calculateSignal(self.signal_probe)[0]
        y = self.calculateSignal(self.signal_probe)[1]
        self.signal_probe.x = x
        self.signal_probe.y = y
        self.updatePlotSignalProduct()
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

    def changeTimeSignalProbe(self, time):
        self.signal_probe.time = float(time) / 100
        self.calculateSignal(self.signal_probe)

    def changeDurationSignalProbe(self, dur):
        self.signal_probe.duration = int(dur)
        self.calculateSignal(self.signal_probe)

    def updatePlotSignalReceived(self):
        x = self.calculateSignal(self.signal_received)[0]
        y = self.calculateSignal(self.signal_received)[1]
        self.signal_received.x = x
        self.signal_received.y = y
        self.updatePlotSignalProduct()
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

    def changeTimeSignalReceived(self, time):
        self.signal_received.time = float(time) / 100
        self.calculateSignal(self.signal_received)

    def changeDurationSignalReceived(self, dur):
        self.signal_received.duration = int(dur)
        self.calculateSignal(self.signal_received)

    def multiplySignals(self):
        x, y = self.impl.multiplyGraphOfSignals([self.signal_probe, self.signal_received])
        return x, y

    def updatePlotSignalProduct(self):
        x, y = self.multiplySignals()
        self.signal_product.x = x
        self.signal_product.y = y
        return self.signal_product.x, self.signal_product.y

    def changeTimePlots(self, time):
        self.changeTimeSignalReceived(time)
        self.changeTimeSignalProbe(time)

    def changeDurationPlots(self, dur):
        self.changeDurationSignalReceived(dur)
        self.changeDurationSignalProbe(dur)

    def integratePlots(self):
        x, y = self.impl.integrateSignals([self.signal_probe, self.signal_received])
        return x, y

    def updatePlotIntegrate(self):
        x, y = self.integratePlots()
        self.signal_integrate.x = x
        self.signal_integrate.y = y
        return self.signal_integrate.x, self.signal_integrate.y

    def setThreshold(self, value):
        self.signal_threshold.x = self.signal_integrate.x.copy()
        y = []
        for i in range(len(self.signal_threshold.x)):
            y.append(value)
        self.signal_threshold.y = y


    def getPlotThreshold(self):
        return self.signal_threshold.x, self.signal_threshold.y
