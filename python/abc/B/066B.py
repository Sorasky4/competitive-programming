s = input()
n = len(s)
for i in range(2,n-1,2):
    if s[:(n-i)//2] == s[(n-i)//2:n-i]:
        print(n-i)
        exit()