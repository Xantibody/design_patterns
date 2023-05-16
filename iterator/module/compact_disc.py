from abc import ABCMeta, abstractmethod
from module.aggregate import Aggregate

class Iterator(metaclass=ABCMeta):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass


class CdShelfIterator(Iterator):
    def __init__(self, cd_Shelf):
        self.__cd_shelf = cd_Shelf
        self.__index = 0


    def has_next(self):
        if self.__index < self.__cd_shelf.get_length():
            return True
        
        else:
            return False
        
    def next(self):
        cd = self.__cd_shelf.get_cd_at(self.__index)
        self.__index += 1
        return cd


class CdShelf(Aggregate):
    def __init__ (self, max_size):
        self.__last= 0
        self.__cd = [None] * max_size

    def get_cd_at(self, index):
        return self.__cd[index]
    
    def append(self, cd):
        self.__cd[self.__last] = cd
        self.__last += 1

    def get_length(self):
        return self.__last
    
    def iterator(self):
        return CdShelfIterator(self)


class Cd(object):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name