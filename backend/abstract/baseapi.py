from abc import ABC, abstractmethod

class BaseAPI(ABC):
    DEFAULT_HEADERS = {"content-type": "application/json", "accept": "application/json"}
    
    @abstractmethod
    def post():
        pass

    @abstractmethod
    def get():
        pass

    @abstractmethod
    def patch():
        pass

    @abstractmethod
    def delete():
        pass

    @abstractmethod
    def get_token():
        pass