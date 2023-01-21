import sympy

from domain.entity.SignalSin import SignalSin
from domain.repository.AppRepository import AppRepository
from domain.entity.GraphOfSignal import GraphOfSignal
from math import pi, cos, inf
from scipy.integrate import quad

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

    def multiplyGraphOfSignals(self, signals: list[SignalSin]):
        if len(signals[0].x) != len(signals[1].x):
            return 0, 0
        else:
            y1 = signals[0].y.copy()
            for i in range(len(signals[0].x) - 1):
                y1[i] = signals[0].y[i] * signals[1].y[i]
            return signals[0].x, y1

    def integrateSignal(self, signals: list[SignalSin]):
        def f(t):
            return cos((2 * pi * signals[0].frequency * t + signals[0].phase) * signals[0].amplitude) * \
                cos((2 * pi * signals[1].frequency * t + signals[1].phase) * signals[1].amplitude)

        res, err = quad(f, 0, signals[0].time)

        print(f"The numerical result is {res} (+-{err})")
