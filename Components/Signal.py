from math import pi, cos





class Signal:
    def __init__(self, frequency, amplitude, phase, duration, time):
        self.frequency = frequency
        self.amplitude = amplitude
        self.phase = phase
        self.duration = duration
        self.time = time

    def calculationsSingnal(self):
        x = []
        y = []
        for i in range(int(self.duration)*int(self.time)):
            x.append(i/self.duration)
            y.append(cos(2*pi*self.frequency*i/self.duration+self.phase)*self.amplitude)
        return x, y

    def calculationsProduct(self, x1, y1, x2, y2):
        for i in range(len(x1)):
            y1[i] = y1[i] * y2[i]
        return x2, y1