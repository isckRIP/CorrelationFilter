from dataclasses import dataclass


@dataclass
class Signal:
    frequency: int
    amplitude: int
    phase: int
    duration: int
    time: int
