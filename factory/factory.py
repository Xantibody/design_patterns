# オブジェクトを生成するclass
#Factoryにcreate_xxx_objectみたいなことかな？


class Factory:
    def create_product(self, product_type):
        if product_type == 'A':
            return ConcreateProductA()
        
        elif product_type == 'B':
            return ConcreateProductB()
        
class Product:
    #基盤のクラス
    pass

class ConcreateProductA(Product):
    pass

class ConcreateProductB(Product):
    pass

def main():
    factory = Factory()
    product_a = factory.create_product('A')
    product_b = factory.create_product('B')