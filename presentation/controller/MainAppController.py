from data.AppRepositoryImpl import AppRepositoryImpl
from domain.entity.GraphOfSignal import GraphOfSignal
from domain.entity.SignalProbe import SignalProbe


class MainAppController:
    impl = AppRepositoryImpl()
    signal_probe = SignalProbe(0, 0, 0, 0, 0)

    def calculateSignal(self, signal: SignalProbe):
        graph_of_signal_probe = GraphOfSignal
        self.impl.getGraphOfSignal(signal)
        return graph_of_signal_probe.x, graph_of_signal_probe.y

    def updatePlotSignalProbe(self):
        x = self.calculateSignal(MainAppController, self.signal_probe)[0]
        y = self.calculateSignal(MainAppController, self.signal_probe)[1]
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
        print(self.signal_probe)

    def changePhaseSignalProbe(self, amp):
        self.signal_probe.phase = float(amp)
        self.calculateSignal(self.signal_probe)
        print(self.signal_probe)

    def changeFrequencySignalProbe(self, amp):
        self.signal_probe.frequency = float(amp)
        self.calculateSignal(self.signal_probe)
        print(self.signal_probe)
