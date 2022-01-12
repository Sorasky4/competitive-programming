# 全部の頂点を根として初期化
def init(n):
    for i in range(n):
        par[i] = i


# 木の根を求める
def root(x):
    # 根であるとき、その値を返す
    if par[x] == x:
        return x
    # 根でないとき、根までの経路上の頂点を根に繋げ(経路圧縮)、根の値を返す
    else:
        par[x] = root(par[x])
        return par[x]


# 2頂点が同じ集合に属するか(根が同じか)を判定
def same(x, y):
    return root(x) == root(y)


'''
# ランク無しの場合
# 2頂点の属する集合を合併
def unite(x, y):
    x = root(x)
    y = root(y)
    if x == y:
        return

    par[x] = y
'''


# ランク有りの場合
def unite(x, y):
    x = root(x)
    y = root(y)
    if x == y:
        return

    # 木の高さが低い方を高い方に繋げる
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
    if rank[x] == rank[y]:
        rank[x] += 1

if __name__ == '__main__':
    n, q = map(int, input().split())
    par = [0]*n
    rank = [0]*n
    init(n)

    for _ in range(q):
        p, a, b = map(int, input().split())
        if p == 0:
            unite(a, b)
        else:
            if same(a, b):
                print('Yes')
            else:
                print('No')

'''
Union-Find木だね。
とりあえずいくつか整理しよう。
まずこのアルゴリズムは木でグループ分けを管理するアルゴリズムだってところは大丈夫かな。親が同じ要素は同じグループに属している、と。
で、ある要素Aとある要素Bが同じグループに属しているかどうかを判定したいとき、それぞれの親を見れば良いんだけど、グループ分けのときに単純に1つの根に次々と辺を張っていったら木が縦長になって辿るときに時間がかかるよね。
それを避けるために1つは経路圧縮といって、どのグループに属しているか調べるときにint root()の中でついでにその要素を親に直接つなぐ処理をしている。もうひとつの処理が質問の部分なんだけど、根が同じでない二つの木を合併する(例えばParent[B] = A はBの親をAとする)ときにそれぞれのグループ(木)の高さを持っておいて、高い方の親に直接低い方をつなぐ処理をすることで、木が縦長になることを防いでいるんだよね。そうして繋がった木の高さを持つために、
'''