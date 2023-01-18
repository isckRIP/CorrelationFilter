from abc import ABC, abstractmethod
from domain.entity.SignalSin import SignalSin
from domain.entity.GraphOfSignal import GraphOfSignal


class AppRepository(ABC):

    @abstractmethod
    def getGraphOfSignal(self, signal: SignalSin) -> GraphOfSignal:
        pass

    @abstractmethod
    def multiplyGraphOfSignals(self, signals: list[GraphOfSignal]) -> GraphOfSignal:
        pass
