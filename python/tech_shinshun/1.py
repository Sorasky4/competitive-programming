x = [int(i) for i in input().split()]
print(-(-(max(x[0],x[1]) - min(x[0],x[1]))//2))