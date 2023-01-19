from domain.repository.AppRepository import AppRepository
from domain.entity.GraphOfSignal import GraphOfSignal
from domain.entity.SignalSin import SignalSin
from math import pi, cos

data = GraphOfSignal

class AppRepositoryImpl(AppRepository):

    def getGraphOfSignal(self, signal):
        x = []
        y = []
        for i in range(int(signal.duration * signal.time)):
            x.append(i / signal.duration)
            y.append(cos(2 * pi * signal.frequency * i / signal.duration + signal.phase) * signal.amplitude)
            data.x = x
            data.y = y

    def multiplyGraphOfSignals(self, signals: list):
        if len(signals[0].x) != len(signals[1].x):
            return 0, 0
        else:
            y1 = signals[0].y.copy()
            for i in range(len(signals[0].x)-1):
                y1[i] = signals[0].y[i] * signals[1].y[i]
            return signals[0].x, y1
