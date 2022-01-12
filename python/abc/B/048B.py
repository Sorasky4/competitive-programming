'''
a, b, x = map(int, input().split())
max_div = b // x * x
min_div = -(-a // x) * x
if a <= min_div <= max_div <= b:
    print(-(-(max_div - min_div + 1) // x))
else:
    print(0)
'''

#以下解説コード
#a以上b以下の整数のうち条件を満たすものの個数を求める問題では
#予め0以上n以下の整数のうち条件を満たすものの個数をf(n)と定義すると
# f(b) - f(a-1) で求まるから楽
#ただし、a = 0 のときに f(-1) が呼び出されることに留意する
def f(n, x):
    if n >= 0:
        return n // x + 1
    else:
        return 0

a, b, x = map(int, input().split())
print(f(b,x) - f(a-1,x))