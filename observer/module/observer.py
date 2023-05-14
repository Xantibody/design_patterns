import time
from abc import ABCMeta, abstractmethod

# observerの抽象クラスを作っておく
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update():
        pass

class DigitObserver(Observer):
    def update(self, generator):
        print('DigitObservser: {0}'.format(generator.get_number()))
        time.sleep(0.1)


class GraphObserver(Observer):
    def update(self, generator):
        print('GraphicObserver:', end='')
        count = generator.get_number()
        for _ in range(count):
            print('漢', end='')
        print("")
        time.sleep(0.1)