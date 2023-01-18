from dataclasses import dataclass


@dataclass
class SignalReceived:
    frequency: float
    amplitude: float
    phase: float
    duration: float
    time: float
    x: list
    y: list
