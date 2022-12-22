from dataclasses import dataclass


@dataclass
class SignalProbe:
    frequency: float
    amplitude: float
    phase: float
    duration: float
    time: float
