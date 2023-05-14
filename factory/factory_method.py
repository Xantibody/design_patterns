# factory method
# 前回のFactoryに作成メソッドを作る
# Factoryクラスを継承して、各々のFactoryクラスを作成
# 作成メソッドをそれぞれのインスタンスを返すようにする


class Factory:
    def factory_method(self):
        pass

class FactoryA(Factory):
    def factory_method(self):
        return ConcreateProductA()

class FactoryB(Factory):
    def factory_method(self):
        return ConcreateProductB()

class Product:
    #基盤のクラス
    pass

class ConcreateProductA(Product):
    pass

class ConcreateProductB(Product):
    pass

def main():
    factory_a = FactoryA()
    factory_b = FactoryB()
    product_a = factory_a.factory_method()
    product_b = factory_b.factory_method()

# 判別する引数いらないから間違えにくい
# そこそこクラスがかさばる