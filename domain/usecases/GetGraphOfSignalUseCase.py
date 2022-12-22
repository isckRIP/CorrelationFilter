from domain.entity.SignalProbe import SignalProbe
from domain.entity.GraphOfSignal import GraphOfSignal
from domain.repository.AppRepository import AppRepository


class GetGraphOfSignalUseCase:
    def __init__(self, repository: AppRepository):
        self.repository = repository

    def __call__(self, signal: SignalProbe) -> GraphOfSignal:
        return self.repository.getGraphOfSignal(signal)
