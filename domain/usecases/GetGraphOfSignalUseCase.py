from domain.entity.Signal import Signal
from domain.entity.GraphOfSignal import GraphOfSignal
from domain.repository.AppRepository import AppRepository


class GetGraphOfSignalUseCase:
    def __init__(self, repository: AppRepository):
        self.repository = repository

    def __call__(self, signal: Signal) -> GraphOfSignal:
        return self.repository.getGraphOfSignal(signal)
