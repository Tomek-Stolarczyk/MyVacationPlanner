from DatabaseServices.IDatabaseService import IDatabaseService
from DatabaseServices.PostgresDatabaseService import PostgresDatabaseService
from DatabaseServices.DatabaseServiceFactoryMethod import DatabaseServiceFactoryMethod

class PostgresDatabaseServiceFactory(DatabaseServiceFactoryMethod):
    def CreateDatabaseService() -> IDatabaseService:
        return PostgresDatabaseService()