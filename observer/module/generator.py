#これがsubjectになるらしい
import random
from abc import ABCMeta, abstractmethod

class NumberGenerator(metaclass=ABCMeta):
    def __init__(self):
        self.__observers = []

# observerの追加と削除のメソッドを作成
    def add_observer(self, observer):
        self.__observers.append(observer)

    def delete_ofserver(self, observer):
        self.__observers.remove(observer)

    def notify_observer(self):
        for o in self.__observers:
            o.update(self)

# 抽象メソッドとして以下を定義
    @abstractmethod
    def get_number(self):
        pass

    @abstractmethod
    def execute(self):
        pass

# 具体的な観測者のことをconcreteSubjectっていうらしい
# めっちゃ堅そうだね
class RandomNumberGenerator(NumberGenerator):
    def __init__(self):
        self.__number = 0
        super().__init__()

    def get_number(self):
        return self.__number
    
    def execute(self):
        for _ in range(20):
            self.__number = random.randint(0,49)
            self.notify_observer()