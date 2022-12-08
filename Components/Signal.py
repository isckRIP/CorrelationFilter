from math import pi, cos


class Signal:
    def __init__(self, frequency, amplitude, phase, duration, time):
        self.frequency = frequency
        self.amplitude = amplitude
        self.phase = phase
        self.duration = duration
        self.time = time

    def calculations(self):
        x = []
        y = []
        for i in range(self.duration*self.time):
            x.append(cos(2*pi*self.frequency*i/self.duration+self.phase)*self.amplitude)
            y.append(i/self.duration)
        return x, y


signal_in = Signal(100, 200, 300, 400, 500)
x, y = signal_in.calculations()
print(x, y)
