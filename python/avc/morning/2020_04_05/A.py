s = list(input())
if ('W' in s and 'E' not in s) or\
   ('N' in s and 'S' not in s) or\
   ('W' not in s and 'E' in s) or\
   ('N' not in s and 'S' in s):
   print('No')
else:
    print('Yes')