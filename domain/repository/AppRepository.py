from abc import ABC, abstractmethod
from domain.entity.SignalProbe import SignalProbe
from domain.entity.GraphOfSignal import GraphOfSignal


class AppRepository(ABC):

    @abstractmethod
    def getGraphOfSignal(self, signal: SignalProbe) -> GraphOfSignal:
        pass

    @abstractmethod
    def multiplyGraphOfSignals(self, signals: list[GraphOfSignal]) -> GraphOfSignal:
        pass
