s = input()
judge = 0
for i in s:
    if (i == 'I' or i == 'i') and judge == 0:
        judge += 1
    if (i == 'C' or i == 'c') and judge == 1:
        judge += 1
    if (i == 'T' or i == 't') and judge == 2:
        judge += 1
print('YES' if judge == 3 else 'NO')