from abc import ABC, abstractmethod, abstractproperty


class IStorage(ABC):
    @abstractproperty
    def movies(self):
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        pass

    @abstractmethod
    def delete_movie(self, title):
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        pass
