horizontals = [[int(i) for i in input().split()] for j in range(3)]
n = int(input())

for i in range(n):
    b = int(input())
    for j, k in enumerate(horizontals):
        if b in k:
            horizontals[j][k.index(b)] = 0

verticals = [[horizontals[i][j] for i in range(3)] for j in range(3)]
diagonals = [[horizontals[i][i] for i in range(3)],
            [horizontals[j][2-j] for j in range(3)]]
card = horizontals + verticals + diagonals
bingo = [0, 0, 0]
if bingo in card:
    print('Yes')
else:
    print('No')