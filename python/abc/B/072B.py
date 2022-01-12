s = input()
ans = [s[i] for i in range(len(s)) if i%2 == 0]
print(''.join(ans))

'''
↑と多分同じ結果
print(input()[::2])
'''