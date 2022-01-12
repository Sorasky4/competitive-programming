w = input()
ng = ['a', 'i', 'u', 'e', 'o']
ans = ''
for i in w:
    if i not in ng:
        ans += i
print(ans)