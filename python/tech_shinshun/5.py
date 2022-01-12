n = input()
if n[-1] == '0':
    ans = int(n)
elif n[-1] == '1':
    ans = int(n) + 9
elif n[-1] == '2':
    ans = int(n) + 8
elif n[-1] == '3':
    ans = int(n) + 7
elif n[-1] == '4':
    ans = int(n) + 6
elif n[-1] == '5':
    ans = int(n) + 5
elif n[-1] == '6':
    ans = int(n) + 4
elif n[-1] == '7':
    ans = int(n) + 3
elif n[-1] == '8':
    ans = int(n) + 2
elif n[-1] == '9':
    ans = int(n) + 1
print(ans)