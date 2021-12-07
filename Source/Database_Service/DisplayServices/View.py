from abc import ABC, abstractclassmethod

# An abstract view. Allows the builder to operate on views consistently as well
# as the html pages when we forward the results to them
class View(ABC):
    @abstractclassmethod
    def GetViewTableHeaders(self) -> list:
        pass

    @abstractclassmethod
    def GetViewTableRow(self) -> list:
        pass

    @abstractclassmethod
    def GetViewID(self) -> str:
        pass