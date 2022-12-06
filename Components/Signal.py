from math import pi, cos


class Signal:
    def __init__(self, friquency, amplitude, phase, duration, time):
        self.friquency = friquency
        self.amplitude = amplitude
        self.phase = phase
        self.duration = duration
        self.time = time

    def calculations(self):
        coordinates = {}
        for i in range(self.duration*self.time):
            coordinates[i/self.duration] = cos(2*pi*i*1/self.duration+self.phase)*self.amplitude
        return coordinates
