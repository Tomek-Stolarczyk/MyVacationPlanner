from DisplayResult.AbstractResultBuilder import AbstractResultBuilder

def ConcreteResultBuilder(AbstractResultBuilder):
    def __init__(self):
        self._result = Result()

    def GetResult(self):
        pass

    def ProduceOutgoingFlight(self):
        pass

    def ProduceIncomingFlight(self):
        pass