from domain.repository.AppRepository import AppRepository
from domain.entity.GraphOfSignal import GraphOfSignal


class GetMultiplyGraphOfSignalsUseCase:
    def __init__(self, repository: AppRepository):
        self.repository = repository

    def __call__(self, signals: list[GraphOfSignal]):
        return self.repository.multiplyGraphOfSignals(signals)
