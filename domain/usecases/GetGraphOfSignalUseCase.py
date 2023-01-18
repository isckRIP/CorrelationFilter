from domain.entity.SignalSin import SignalSin
from domain.entity.GraphOfSignal import GraphOfSignal
from domain.repository.AppRepository import AppRepository


class GetGraphOfSignalUseCase:
    def __init__(self, repository: AppRepository):
        self.repository = repository

    def __call__(self, signal: SignalSin) -> GraphOfSignal:
        return self.repository.getGraphOfSignal(signal)
