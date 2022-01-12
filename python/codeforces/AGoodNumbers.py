'''
t = int(input())
cnt = 0
for i in range(t):
    a,b = map(int,input().split())
    if min(a,b) < abs(a-b) and max(a,b)%min(a,b)!=0:
        print('Finite')
    else:
        for j in range(10**4+1):
            if (j-a)%a==0 or(j-a)%b==0 or (j-b)%a==0 or (j-b)%b==0:
                cnt += 1
                if cnt == min(a,b):
                    print('Finite')
                    cnt = 0
                    break
            else:
                cnt = 0
        else:
            print('Infinite')
            cnt = 0
'''
'''
t = int(input())
cnt = 0
for i in range(t):
    a,b = map(int,input().split())
    if min(a,b) < abs(a-b):
        print('Finite')
    else:
        print('Infinite')
'''
'''
t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    c = [0,a,b]
    cnt = 0
    brcnt = 0
    for j in range(min(a,b),10**4+1):
        if j == 0 or j == a or j == b:
            cnt += 1
        if (j > a and j - a in c) or (j > b and j - b in c):
            c.append(j)
            cnt += 1
            if cnt == min(a,b):
                print('Finite')
                break
        else:
            brcnt += 1
            cnt = 0
    else:
        print('Infinite')
'''