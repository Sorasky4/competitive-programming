import collections
print('1.圧縮  2.解凍')
cmd = int(input())
s = input()
if cmd == 1 and 1 <= len(s) <= 32:
    ss = collections.Counter(s)
    ans = list(ss.keys())
    for i in range(len(ans)):
        ans[i] += str(list(ss.values())[i])
    print(''.join(map(str,ans)))
elif cmd == 2 and 1 <= len(s) <= 32:
    ans = []
    for i in range(0,len(s),2):
        ans.append(s[i]*(int(s[i+1])))
    print(''.join(map(str,ans)))
else:
    print('Error')