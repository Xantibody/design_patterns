# この考え方はもとから持っていたから書けそう
# ざっくり言えばAPI
# 複雑なメソッドの組み合わせ処理をまとめただけのクラスを作っておけば、そのメソッド呼ぶだけでよいよねって話

class Message:
    def create():
        return 'メッセージ作成'

import datetime    
class NowDate:
    def str_add_now_date(str:str)->str:
        now = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S.%f')
        return f'[{now}]:{str}'
    
class View:
    def str_print(str:str):
        print(str)

class Facade():
    def facade_test():
        message = Message.create()
        add_now_date = NowDate.str_add_now_date(message)
        View.str_print(add_now_date)

# これだけ呼べば勝手に処理してくれる
Facade.facade_test()