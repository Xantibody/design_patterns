# 参考記事
#https://qiita.com/ttsubo/items/97d7dd23e8f939c81d78

from module.compact_disc import CdShelf,Cd

def main():
    cd_shelf = CdShelf(5)
    cd_shelf.append(Cd('尾崎紀世彦の世界'))
    cd_shelf.append(Cd('ロックマンエグゼ アドバンスドコレクション オリジナル・サウンドトラック'))
    cd_shelf.append(Cd('ケロラバー'))
    cd_shelf.append(Cd('ENSON3'))
    cd_shelf.append(Cd('キン肉マン 超人大全集'))
    it = cd_shelf.iterator()
    while it.has_next():
        cd = it.next()
        print(cd.get_name())
    
    
    
if __name__ == '__main__':
    main()

# 要はlistみたいなものの認識
# listにオブジェクトを入れる
# でそのiteratorを作成する
# そうすることで、earch文のようにすべての要素に対して簡単にアクセスできる。
# また、今回の書き方ではなく__iter__メソッド、__next__メソッドを実装すると同様の性質をもったクラスが作れるそう