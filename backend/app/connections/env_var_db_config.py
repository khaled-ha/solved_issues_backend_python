import os

class EnvVarExceptions(Exception):
    def __init__(self, message) -> None:
        self.message =  message
        super().__init__(self.message)


class EnvVars:
    def __init__(self) -> None:
        
        self.POSTGRES_USER = os.getenv('POSTGRES_USER', None)
        if not self.POSTGRES_USER:
            raise EnvVarExceptions('missing environment variable user')
        
        self.POSTGTRES_DB = os.getenv('POSTGTRES_DB', None)
        if not self.POSTGTRES_DB:
            raise EnvVarExceptions('missing environment variable databse')        
        
        self.POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', None)        
        if not self.POSTGRES_PASSWORD:
            raise EnvVarExceptions('missing environment variable password')

        self.POSTGRES_HOST = os.getenv('POSTGRES_HOST', None)        
        if not self.POSTGRES_PASSWORD:
            raise EnvVarExceptions('missing environment variable host')

    @property
    def database_url(self):
        return f'postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@db/{self.POSTGTRES_DB}'
