from abc import ABC, abstractclassmethod
from DatabaseServices.IDatabaseService import IDatabaseService

class DatabaseServiceFactoryMethod(ABC):
    @abstractclassmethod
    def CreateDatabaseService() -> IDatabaseService:
        pass