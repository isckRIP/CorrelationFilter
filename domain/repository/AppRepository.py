from abc import ABC, abstractmethod
from domain.entity.Signal import Signal
from domain.entity.GraphOfSignal import GraphOfSignal


class AppRepository(ABC):

    @abstractmethod
    def getGraphOfSignal(self, signal: Signal) -> GraphOfSignal:
        pass

    @abstractmethod
    def multiplyGraphOfSignals(self, signals: list[GraphOfSignal]) -> GraphOfSignal:
        pass
