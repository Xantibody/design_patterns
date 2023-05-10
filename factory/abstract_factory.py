# AbstractFactory
# 一つのFactoryクラスで複数のインスタンスを作る必要があるときに必要？
# 



class Factory:
    def create_product_a(self):
        pass

    def create_product_b(self):
        pass

class FactoryA(Factory):
    def create_product_a(self):
        return ConcreateProductA()
    
    def create_product_b(self):
        return ConcreateProductC()

class FactoryB(Factory):
    def create_product_a(self):
        return ConcreateProductB()

    def create_product_b(self):
        return ConcreateProductD()

class ProductA:
    #基盤のクラス
    pass

class ProductB:
    pass

class ConcreateProductA(ProductA):
    pass

class ConcreateProductB(ProductA):
    pass

class ConcreateProductC(ProductB):
    pass

class ConcreateProductD(ProductB):
    pass

def main():
    factory_a = FactoryA()
    factory_b = FactoryB()
    product_a = factory_a.create_product_a()
    product_c = factory_a.create_product_b()

    product_b = factory_b.create_product_a()
    product_d = factory_b.create_product_b()

# 同じ継承元のインスタンスを2つつかう場合はこういう書き方のほうがよさそう
# 名称が違うだけで細かく設定するならこっちになってくのかな？
# Factoryだと、判別を固定文字列にするの嫌なので、Factory_methodから使っていきたさはある