from abc import ABC, abstractclassmethod
from DatabaseServices.IDatabaseService import IDatabaseService

# Create an abstract class for the factory method. New factories
# will override the CreateDatabaseService method to create
# their own version of the database service
class DatabaseServiceFactoryMethod(ABC):
    @abstractclassmethod
    def CreateDatabaseService() -> IDatabaseService:
        pass