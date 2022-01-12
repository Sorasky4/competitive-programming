'''
import sympy as sym
f = sym.simplify("f(n)") #求める解
s = sym.simplify("f(n)-f(n-1)*2-f(n-2)*3") #漸化式(s=0となるように記述する)
ini = sym.simplify({"f(0)":6,"f(1)":7}) #初期条件({0:0,1:1}としても良い)
FibGeneralTerm = sym.rsolve(s,f,ini) #初期条件iniの漸化式sをfについて解く

print(FibGeneralTerm)
'''

'''
num = int(input('数字を入力してください: '))
for i in range(1,num+1):
    print(i, end = ' ')
'''

eto = ('子','丑','寅','卯','辰','己','午','未','申','酉','戌','亥')
constellations = ('おひつじ座','おうし座','ふたご座','かに座','しし座',
    'おとめ座','てんびん座','さそり座','いて座','やぎ座','みずがめ座','うお座')
birthday = [0]*3
birthday[0] = int(input('あなたの誕生年を西暦4桁で入力してください：'))
birthday[1] = int(input('誕生月を入力してください：'))
birthday[2] = int(input('誕生日を入力してください：'))
now = input('最後に、現在の年月日を8桁で入力してください：')

#入力が間違っていないか確認
if not(1900 <= birthday[0] <= 2020) or not(1 <= birthday[1] <= 12):
    print('エラー1：入力形式が正しくないか、虚偽の誕生日')
    exit()
if birthday[1] == 4 or birthday[1] == 6 or birthday[1] == 9 or birthday[1] == 11:
    if not(1 <= birthday[2] <= 30):
        print('エラー2：入力形式が正しくないか、虚偽の誕生日')
        exit()
elif birthday[1] == 2:
    if birthday[0] % 4 == 0 and birthday[0] % 100 != 0 or birthday[0] % 400 == 0:
        if not(1 <= birthday[2] <= 29):
            print('エラー3：入力形式が正しくないか、虚偽の誕生日　ヒント：うるう年')
            exit()
    else:
        if not(1 <= birthday[2] <= 28):
            print('エラー4：入力形式が正しくないか、虚偽の誕生日　ヒント：うるう年')
            exit()
else:
    if not(1 <= birthday[2] <= 31):
        print('エラー5：入力形式が正しくないか、虚偽の誕生日')
        exit()

date = [0]*3
date[0] = int(now[:4])
date[1] = int(now[4:6]) if now[4] != '0' else int(now[5])
date[2] = int(now[6:8]) if now[6] != '0' else int(now[7])
you = [0]*4

#生まれた和暦を計算
if 1900 <= birthday[0] < 1912:
    you[0] = '明治' + str(birthday[0] - 1867) + '年'
elif birthday[0] == 1912:
    if birthday[1] <= 6 or (birthday[1] == 7 and birthday[2] <= 29):
        you[0] = '明治45年'
    else:
        you[0] = '大正元年'
elif 1912 < birthday[0] <= 1925:
    you[0] = '大正' + str(birthday[0] - 1911) + '年'
elif birthday[0] == 1926:
    if birthday[1] <= 11 or (birthday[1] == 12 and birthday[2] <= 24):
        you[0] = '大正15年'
    else:
        you[0] = '昭和元年'
elif 1926 < birthday[0] <=1988:
    you[0] = '昭和' + str(birthday[0] - 1925) + '年'
elif birthday[0] == 1989:
    if birthday[1] == 1 and birthday[2] <= 7:
        you[0] = '昭和64年'
    else:
        you[0] = '平成元年'
elif 1989 < birthday[0] <= 2018:
    you[0] = '平成' + str(birthday[0] - 1988) + '年'
elif birthday[0] == 2019:
    if birthday[1] <= 4:
        you[0] = '平成31年'
    else:
        you[0] = '令和元年'
else:
    you[0] = '令和' + str(birthday[0] - 2018) + '年'

#干支を計算
you[1] = eto[(birthday[0] + 8) % 12]

#何歳か
if date[1] < birthday[1] or (date[1] == birthday[1] and date[2] < birthday[2]):
    you[2] = date[0] - birthday[0] - 1
else:
    you[2] = date[0] - birthday[0]

#12星座を計算
if (birthday[1] == 3 and 21 <= birthday[2]) or (birthday[1] == 4 and birthday[2] <= 19):
    you[3] = constellations[0]
elif (birthday[1] == 4 and 20 <= birthday[2]) or (birthday[1] == 5 and birthday[2] <= 20):
    you[3] = constellations[1]
elif (birthday[1] == 5 and 21 <= birthday[2]) or (birthday[1] == 6 and birthday[2] <= 21):
    you[3] = constellations[2]
elif (birthday[1] == 6 and 22 <= birthday[2]) or (birthday[1] == 7 and birthday[2] <= 22):
    you[3] = constellations[3]
elif (birthday[1] == 7 and 23 <= birthday[2]) or (birthday[1] == 8 and birthday[2] <= 22):
    you[3] = constellations[4]
elif (birthday[1] == 8 and 23 <= birthday[2]) or (birthday[1] == 9 and birthday[2] <= 22):
    you[3] = constellations[5]
elif (birthday[1] == 9 and 23 <= birthday[2]) or (birthday[1] == 10 and birthday[2] <= 23):
    you[3] = constellations[6]
elif (birthday[1] == 10 and 24 <= birthday[2]) or (birthday[1] == 11 and birthday[2] <= 22):
    you[3] = constellations[7]
elif (birthday[1] == 11 and 23 <= birthday[2]) or (birthday[1] == 12 and birthday[2] <= 21):
    you[3] = constellations[8]
elif (birthday[1] == 12 and 22 <= birthday[2]) or (birthday[1] == 1 and birthday[2] <= 19):
    you[3] = constellations[9]
elif (birthday[1] == 1 and 20 <= birthday[2]) or (birthday[1] == 2 and birthday[2] <= 18):
    you[3] = constellations[10]
else:
    you[3] = constellations[11]

#結果を表示
print(f'あなたは{you[0]}{you[1]}年生まれの{you[2]}歳{you[3]}です。')