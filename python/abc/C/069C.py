n = int(input())
a = [int(i) for i in input().split()]
two = 0
four = 0
for i in range(n):
    if a[i] % 4 == 0:
        four += 1
    elif a[i] % 2 == 0:
        two += 1
if n == 2:
    ans = 'Yes' if 1 <= four or two == n else 'No'
elif n == 3:
    ans = 'Yes' if 1 <= four or two == n else 'No'
else:
    ans = 'Yes' if (2 <= four and (n-four*2 <= two or (n-4)//2 <= four-2)) or (four == 1 and n-2 <= two) or two == n else 'No'
print(ans)