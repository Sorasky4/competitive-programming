'''後日再挑戦'''

# 全部の頂点を根として初期化
def init(n):
    for i in range(n):
        par[i] = -1


# 木の根を求める
def root(x):
    # 根であるとき、その値を返す
    if par[x] < 0:
        return x
    # 根でないとき、根までの経路上の頂点を根に繋げ(経路圧縮)、根の値を返す
    else:
        par[x] = root(par[x])
        return par[x]


# 2頂点が同じ集合に属するか(根が同じか)を判定
def same(x, y):
    return root(x) == root(y)


def unite(x, y):
    x = root(x)
    y = root(y)
    if x == y:
        return

    # 木の高さが低い方を高い方に繋げる
    if par[x] > par[y]:
        x, y = y, x
    par[x] += par[y]
    par[y] = x

def size(x):
    return -par[root(x)]

if __name__ == '__main__':
    n, m = map(int, input().split())
    par = [0]*n
    ans = [0]*m
    cur = n * (n-1) // 2
    init(n)

    for i in range(m):
        ans[i] = cur
        a, b = map(int, input().split())
        if same(a, b):
            continue
        cur -= size(a) * size(b)
        unite(a, b)
reversed(ans)
for i in range(m):
    print(ans[i])