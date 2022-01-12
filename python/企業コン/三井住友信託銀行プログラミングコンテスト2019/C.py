x = input()
if int(x) < 100:
    print(0)
    exit(0)
if 0 <= int(x[-2]+x[-1]) <= 5:
    print(1)
    exit(0)
elif 6 <= int(x[-2]+x[-1]) <= 10 and 2 <= int(x)//100:
    print(1)
elif 11 <= int(x[-2]+x[-1]) <= 15 and 3 <= int(x)//100:
    print(1)
elif 16 <= int(x[-2]+x[-1]) <= 20 and 4 <= int(x)//100:
    print(1)
elif 21 <= int(x[-2]+x[-1]) <= 25 and 5 <= int(x)//100:
    print(1)
elif 26 <= int(x[-2]+x[-1]) <= 30 and 6 <= int(x)//100:
    print(1)
elif 31 <= int(x[-2]+x[-1]) <= 35 and 7 <= int(x)//100:
    print(1)
elif 36 <= int(x[-2]+x[-1]) <= 40 and 8 <= int(x)//100:
    print(1)
elif 41 <= int(x[-2]+x[-1]) <= 45 and 9 <= int(x)//100:
    print(1)
elif 46 <= int(x[-2]+x[-1]) <= 50 and 10 <= int(x)//100:
    print(1)
elif 51 <= int(x[-2]+x[-1]) <= 55 and 11 <= int(x)//100:
    print(1)
elif 56 <= int(x[-2]+x[-1]) <= 60 and 12 <= int(x)//100:
    print(1)
elif 61 <= int(x[-2]+x[-1]) <= 65 and 13 <= int(x)//100:
    print(1)
elif 66 <= int(x[-2]+x[-1]) <= 70 and 14 <= int(x)//100:
    print(1)
elif 71 <= int(x[-2]+x[-1]) <= 75 and 15 <= int(x)//100:
    print(1)
elif 76 <= int(x[-2]+x[-1]) <= 80 and 16 <= int(x)//100:
    print(1)
elif 81 <= int(x[-2]+x[-1]) <= 85 and 17 <= int(x)//100:
    print(1)
elif 86 <= int(x[-2]+x[-1]) <= 90 and 18 <= int(x)//100:
    print(1)
elif 91 <= int(x[-2]+x[-1]) <= 95 and 19 <= int(x)//100:
    print(1)
elif 96 <= int(x[-2]+x[-1]) <= 99 and 20 <= int(x)//100:
    print(1)
else:
    print(0)