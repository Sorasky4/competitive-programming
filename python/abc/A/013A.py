x = input()
alpha = 'ABCDE'
for i in range(5):
    if x == alpha[i]:
        ans = i
        break
print(int(ans+1))