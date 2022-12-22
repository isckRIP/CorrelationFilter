from domain.repository.AppRepository import AppRepository
from domain.entity.GraphOfSignal import GraphOfSignal
from domain.entity.SignalProbe import SignalProbe
from math import pi, cos

data = GraphOfSignal

class AppRepositoryImpl(AppRepository):

    def getGraphOfSignal(self, signal: SignalProbe):
        x = []
        y = []
        for i in range(int(signal.duration * signal.time)):
            x.append(i / signal.duration)
            y.append(cos(2 * pi * signal.frequency * i / signal.duration + signal.phase) * signal.amplitude)
            # data(x, y)
            data.x = x
            data.y = y

    def multiplyGraphOfSignals(self, signals: list[GraphOfSignal]) -> GraphOfSignal:
        for i in range(len(signals[0].x)):
            signals[0].y[i] = signals[0].y[i] * signals[1].y[i]
        return GraphOfSignal(signals[1].x, signals[0].y)
