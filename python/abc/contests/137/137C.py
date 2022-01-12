n = int(input())
a = [input() for i in range(n)]
new_a = [0]*len(a)
cnt = 1
ans = 0
for i in range(len(a)):
    new_a[i] = sorted(a[i]) 
b = sorted(new_a)
for i in range(len(b)-1):
    if b[i] == b[i+1]:
        cnt += 1
    else:
        ans += cnt*(cnt - 1)/2 #組み合わせ(cnt C 2)
        cnt = 1
ans += cnt*(cnt - 1)/2
print(int(ans))