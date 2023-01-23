from abc import ABC, abstractmethod
from domain.entity.SignalSin import SignalSin
from domain.entity.GraphOfSignal import GraphOfSignal


class AppRepository(ABC):

    @abstractmethod
    def getGraphOfSignal(self, signal: SignalSin):
        pass

    @abstractmethod
    def multiplyGraphOfSignals(self, signals: list[SignalSin]) -> SignalSin:
        pass


    @abstractmethod
    def integrateSignals(self, signals: list[SignalSin]):
        pass