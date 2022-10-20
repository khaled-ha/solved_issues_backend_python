from abc import ABC, abstractmethod

class BaseAPI(ABC):
    DEFAULT_HEADERS = {"content-type": "application/json", "accept": "application/json"}
    
    @abstractmethod
    def post_user():
        pass

    @abstractmethod
    def get_user():
        pass

    @abstractmethod
    def patch_user():
        pass

    @abstractmethod
    def delete_user():
        pass