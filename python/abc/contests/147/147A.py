a = [int(i) for i in input().split()]
print('bust' if sum(a) >= 22 else 'win')