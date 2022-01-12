# 2進数表記による自乗を利用した繰り返し2乗法
def pow_mod(n, k, mod):
    ans = 1
    # kの下の桁から処理
    # 右シフトで処理し終わった桁を追い出す
    # ゼロになるまでやる
    while k > 0:
        if k & 1: # kの一番下の桁が立っているとき
            ans = (ans * n) % mod # その桁に対応するnの累乗数をかけ合わせる
        n = (n * n) % mod # nの累乗数をkの次の桁へ対応させる
        k >>= 1 # kを右シフト
    return ans


'''
# 再帰による自乗を利用した繰り返し2乗法
def pow_mod(n, k, mod):
    if k == 0:
        return 1
    elif k & 1:
        return pow_mod(n, k - 1, mod) * n % mod
    else:
        t = pow_mod(n, k // 2, mod)
        return t * t % mod
'''

if __name__ == '__main__':
    n, m, p = map(int, input().split())
    print(pow_mod(n, p, m))