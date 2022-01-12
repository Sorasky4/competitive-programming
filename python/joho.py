st = 5
lb = 5
cmb = 0
for i in range(st+1):
    for j in range(st+1):
        for k in range(st+1):
            for l in range(st+1):
                for m in range(st+1):
                    if i + j + k + l + m <= lb:
                        cmb += 1
print(cmb)

'''
生徒5人いて研究室が5個あって
所為とはいくつの研究室に入ってもいい
研究室の定員は一人
どの研究室に所属しないのもあり
さて、組み合わせの総数は？
'''