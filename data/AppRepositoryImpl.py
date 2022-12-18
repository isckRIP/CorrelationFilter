from domain.repository.AppRepository import AppRepository
from domain.entity.GraphOfSignal import GraphOfSignal
from domain.entity.Signal import Signal
from math import pi, cos


class AppRepositoryImpl(AppRepository):
    @property
    def getGraphOfSignal(self, signal: Signal) -> GraphOfSignal:
        x = []
        y = []
        for i in range(int(self.duration) * int(self.time)):
            x.append(i / self.duration)
            y.append(cos(2 * pi * self.frequency * i / self.duration + self.phase) * self.amplitude)
        return GraphOfSignal(x, y)

    @property
    def multiplyGraphOfSignals(self, signals: list[GraphOfSignal]) -> GraphOfSignal:
        for i in range(len(signals[0].x)):
            signals[0].y[i] = signals[0].y[i] * signals[1].y[i]
        return GraphOfSignal(signals[1].x, signals[0].y)
