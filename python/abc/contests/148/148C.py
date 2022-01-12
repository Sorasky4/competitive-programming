import fractions
def lcm(a, b):
    return (a*b) // fractions.gcd(a, b)
x = [int(i) for i in input().split()]
print(lcm(x[0], x[1]))