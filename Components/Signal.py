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
        for i in range(int(self.duration)*int(self.time)):
            x.append(i/self.duration)
            y.append(cos(2*pi*self.frequency*i/self.duration+self.phase)*self.amplitude)
        return x, y


signal_in = Signal(100, 200, 300, 400, 500)
x, y = signal_in.calculations()
print(signal_in.amplitude)
