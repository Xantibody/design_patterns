# 通知を発する奴と、それを監視して察知したら相応の動きをする奴
# 2つそろった構造をobserver

from module.generator import RandomNumberGenerator
from module.observer import DigitObserver, GraphObserver

def main():
    generator = RandomNumberGenerator()
    observer1 = DigitObserver()
    observer2 = GraphObserver()
    generator.add_observer(observer1)
    generator.add_observer(observer2)
    generator.execute()

if __name__ == '__main__':
    main()

# 基本構造はここのgeneratorクラスで、各observerクラスを管理する
# ⇒削除、追加、通知

# 管理方法は抽象メソッドを継承した各クラスを配列なりリストで管理
# generator内の通知メソッドで管理しているobserverリストをループする。
# ループでobserverクラス内の通知処理メソッドを呼ぶ。
# observerクラスは継承した通知処理メソッドを個別処理に書き換える。
# そうすることでいろいろな処理が出来る