sa = input()
sb = input()
sc = input()
turn = sa[0]
sa = sa[1:]
while True:
    if turn == 'a':
        if not sa:
            win = 'A'
            break
        else:
            turn = sa[0]
            sa = sa[1:]
    if turn == 'b':
        if not sb:
            win = 'B'
            break
        else:
            turn = sb[0]
            sb = sb[1:]
    if turn == 'c':
        if not sc:
            win = 'C'
            break
        else:
            turn = sc[0]
            sc = sc[1:]
print(win)