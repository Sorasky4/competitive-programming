# 普通のFizzBuzz
'''
a = int(input())
for i in range(1,a+1):
    if i % 15 == 0:
        print("fizzbuzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)
'''

# 手法1 strで格納型のFizzBuzz
'''
def FizzBuzz(n):
    ans = [''] * n
    for i in range(1,n+1):
        if i % 3 == 0:
            ans[i-1] += 'Fizz'
        if i % 5 == 0:
            ans[i-1] += 'Buzz'
        if not ans[i-1]:
            ans[i-1] += str(i)
    return ans

print(FizzBuzz(int(input())))
'''

# 手法2 トリッキーな格納型FizzBuzz
'''
FizzBuzz = lambda n: [n%3//2*'Fizz' + n%5//4*'Buzz' or str(-~n) for n in range(n)]

# -~n == (n + 1), ~-n == (n - 1)
# for n in range(n) で 0, 1, 2, ... , n-1 を生成
# 順番に見ていくと、
#                           Fizzの個数↓       +       Buzzの個数↓ or str(n+1)
# n == 0 のとき n % 3 == 0, 0 // 2 == 0, n % 5 == 0, 0 // 4 == 0, -~n == 1
# n == 1 のとき n % 3 == 1, 1 // 2 == 0, n % 5 == 1, 1 // 4 == 0, -~n == 2
# n == 2 のとき n % 3 == 2, 2 // 2 == 1, n % 5 == 2, 2 // 4 == 0, -~n == 3
# という流れで成り立っている

print(FizzBuzz(int(input())))
'''

# 手法1,2ともに10**6をinputしたときの実行時間は約15.2sだった