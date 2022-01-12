n, m = map(int, input().split())
base_n = (n % 12) * 30
rad_m = m * 6
rad_n = base_n + m * 0.5
rad = abs(rad_m - rad_n)
print(min(rad, 360 - rad))