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
        
        self.POSTGRES_DB = os.getenv('POSTGRES_DB', None)
        if not self.POSTGRES_DB:
            raise EnvVarExceptions('missing environment variable database')        
        
        self.POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', None)        
        if not self.POSTGRES_PASSWORD:
            raise EnvVarExceptions('missing environment variable password')

        self.POSTGRES_HOST = os.getenv('POSTGRES_HOST', None)        
        if not self.POSTGRES_PASSWORD:
            raise EnvVarExceptions('missing environment variable host')
        
        self.AUTH_SERVER_HOST = os.getenv('AUTH_SERVER_HOST')
        if not self.POSTGRES_PASSWORD:
            raise EnvVarExceptions('missing environment variable AUTH Server is not yet set')

        self.AUTH_SERVER_PORT = os.getenv('AUTH_SERVER_PORT')
        if not self.POSTGRES_PASSWORD:
            raise EnvVarExceptions('missing environment variable AUTH Server Port')
        
    @property
    def database_docker_url(self):
        return f'postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@db/{self.POSTGRES_DB}'

    @property
    def database_session_url(self):
        return f'postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@db/{self.POSTGRES_DB}'