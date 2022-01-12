T = int(input())
for case in range(1,T+1):
    s = input()
    S = ''
    for i in s:
        for j in range(int(i)):
            S += '('
        S += i
        for j in range(int(i)):
            S += ')'
    too_long = True
    ans = S
    while too_long:
        too_long = False
        S = ans
        ans = S[:1]
        for i in range(1,len(S)-1):
            if S[i] == ')' and S[i+1] == '(' or S[i-1] == ')' and S[i] == '(':
                too_long = True
                pass
            else:
                ans += S[i]
            if i == len(S)-2:
                ans += S[-1]
    print('Case #{}:'.format(case), ans)