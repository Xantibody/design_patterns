class Singleton:
    message = ''

    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance
    


def main():
    instance_A = Singleton()
    instance_B = Singleton()

    print('instance_Aのmessageを変更')
    instance_A.message = 'instance_Aから変更したよ'
    print(f'instance_A:{instance_A.message}')
    print(f'instance_B:{instance_B.message}')
    
    instance_A.message = 'instance_Bから変更したよん'
    print('instance_Bのmessageを変更')
    print(f'instance_A:{instance_A.message}')
    print(f'instance_B:{instance_B.message}')

    print('instanceは一つしか生成できないように担保される')

main()