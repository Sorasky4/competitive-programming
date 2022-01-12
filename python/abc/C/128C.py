n, m = map(int, input().split())  #n個のスイッチとm個の電球
s = []
k = []
for i in range(m):
    s.append(list(map(int,input().split())))
    k.append(s[i].pop(0))
p = [int(i) for i in input().split()]

ans = 0
for i in range(2**n):
    ok = True
    for j in range(m):
        cnt = 0  #各電球の点灯条件に指定されているスイッチの内、onになっているものの数
        for l in range(k[j]):
            if i & (1 << (s[j][l]-1)):  #1をs[j][l]ビット左シフトしてiとの論理積をとる
                cnt += 1
        if cnt % 2 != p[j]:
            ok = False
    if ok:
        ans += 1
print(ans)

'''
例えばスイッチが2つあった場合、on,offの組み合わせをビットで表すと
00
01
10
11
の4通りで、右からスイッチ1,2とすると
1を左に0ビットシフトしたものが01
1を左に1ビットシフトしたものが10
となり、それぞれスイッチ1がonの状態と
スイッチ2がonの状態を表すことができる
これを利用する
'''