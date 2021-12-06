from abc import ABC, abstractmethod
from DisplayResult.Result import Result

class AbstractResultBuilder(ABC):
    @abstractmethod
    def GetResult(self) -> Result:
        pass

    @abstractmethod
    def ProduceOutgoingFlight(self):
        pass

    @abstractmethod
    def ProduceIncomingFlight(self):
        pass