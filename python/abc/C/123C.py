'''
WA
n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
sta = -(-n//a) #spend tame a
nb = max(n%a if n%a!=0 else a,n-(b)*(sta-1)) # now b
stb = -(-nb//b)
nc = max(nb%b if nb%b!=0 else b,nb-(c)*(stb-1))
stc = -(-nc//c)
nd = max(nc%c if nc%c!=0 else c,nc-(d)*(stc-1))
std = -(-nd//d)
ne = max(nd%d if nd%d!=0 else d,nd-(e)*(std-1))
ste = -(-ne//e)
ans = sta + stb + stc + std + ste
print(ans)
'''

n,*a=open(0);print(-(-int(n)//min(map(int,a)))+4)