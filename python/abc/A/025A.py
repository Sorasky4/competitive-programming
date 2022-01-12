s = input()
n = int(input()) - 1
t = s
u = [0]*25
k = 0
for i in range(5):
    for j in range(5):
        u[k] = s[i] + t[j]
        k += 1
print(u[n])