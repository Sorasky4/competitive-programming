mail = input()
s = 'abcdefghijklmnopqrstuvwxyz0123456789._@-'
for i in range(len(mail)-1):
    if mail[i] not in s or mail[i+1] not in s:
        print('No')
        break
    elif (mail[i] == '@' and mail[i+1] =='.') or (mail[i] == '.' and mail[i+1] == '@'):
        print('No')
        break
    elif mail[i] == '.' and mail[i+1] == '.':
        print('No')
        break
    elif mail[i] == '_' and mail[i+1] == '_':
        print('No')
        break
else:
    print(mail)