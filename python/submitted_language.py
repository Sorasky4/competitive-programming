import requests
import numpy as np
import matplotlib.pyplot as plt

'''
def count_language():
    url = 'https://kenkoooo.com/atcoder/resources/lang.json'
    r = requests.get(url)
    data = r.json()
    la_dict = {}
    for info in data:
        la = info['language']
        cnt = info['count']
        if la not in la_dict.keys():
            la_dict[la] = 0
        la_dict[la] += cnt
    dic = sorted(la_dict, key=lambda x: x.value(), reverse=True)
    print(dic)

count_language()
'''

#結果は以下
top10 = [('C++', 3162641), ('Python', 1126138), ('Java', 256788), ('PyPy', 181800), ('C', 140908),
        ('Ruby', 112392), ('C#', 103705), ('Rust', 53601), ('Go', 42374), ('Haskell', 31045)]

left = np.array([i for i in range(1,11)])
label = np.array([i[0] for i in top10])
height = np.array([i[1] for i in top10])
plt.bar(left, height, tick_label=label, align='center')
plt.show()