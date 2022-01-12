n = int(input())
cnt = 'abcde'
for i in range(1,n+1):
    ans = []
    for j in range(2,7):
        if i % j == 0:
            ans.append(cnt[j-2])
    print(''.join(map(str,ans)) if ans else i)