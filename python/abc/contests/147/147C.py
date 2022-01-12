n = int(input())
a = [0 for i in range(n)]
x = [[] for i in range(n)]
y = [[] for i in range(n)]
for i in range(n):
    a[i] = int(input())
    for j in range(a[i]):
        xx, yy = map(int,input().split())
        x[i].append(xx)
        y[i].append(yy)
ans = 0
for i in range(2**n):  #ビット全探索 今回は不親切を0,正直者を1とする
    ok = True  #フラグをたてる
    for j in range(n):
        if ((1 << j) & i):  #正直者の話だけを聞く
            for k in range(a[j]):
                if y[j][k] == 0:
                    if (1 << (x[j][k] - 1)) & i:  #正直者が不親切だと言った人を正直者とみなしているとき
                        ok = False  #矛盾するのでフラグを折る
                else:
                    if not((1 << (x[j][k] - 1)) & i):  #正直者が正直者だと言った人を不親切とみなしているとき
                        ok = False  #矛盾するのでフラグを折る
    if ok:
        cnt = bin(i).count('1')  #iを2進数表記したときの1の数(正直者の数)をカウント
        ans = max(ans, cnt)
print(ans)