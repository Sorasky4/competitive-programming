n = int(input())
zero = ['###', '#.#', '#.#','#.#', '###']
one = ['.#.', '##.', '.#.','.#.', '###']
two = ['###', '..#', '###', '#..', '###']
three = ['###', '..#', '###', '..#', '###']
four = ['#.#', '#.#', '###', '..#', '..#']
five = ['###', '#..', '###', '..#', '###']
six = ['###', '#..', '###', '#.#', '###']
seven = ['###', '..#', '..#', '..#', '..#']
eight = ['###', '#.#', '###', '#.#', '###']
nine = ['###', '#.#', '###', '..#', '###']
num = [zero, one, two, three, four, five, six, seven, eight, nine]
s = []
for _ in range(5):
    s.append(input())
ans = ''
for i in range(n):
    match = []
    for j in range(5):
        match.append(s[j][4*i+1:4*i+4])
    for j, v in enumerate(num):
        if match == v:
            ans += str(j)
print(ans)