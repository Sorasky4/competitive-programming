s = input()

stack = []
ans = []

for i in s:
    if i == '(':
        stack.append(i)
    elif i == ')':
        while len(stack) > 0:
            tmp = stack.pop()
            if tmp == '(':
                break
            else:
                ans.append(tmp)
        if len(stack) > 0:
            if stack[-1] == 'c' or stack[-1] == 's' or stack[-1] == 't':
                ans.append(stack.pop())
    elif i == '*' or i == '/':
        while len(stack) > 0:
            if stack[-1] == '*' or stack[-1] == '/':
                ans.append(stack.pop())
            else:
                break
        stack.append(i)
    elif i == '+' or i == '-':
        while len(stack) > 0:
            if stack[-1] == '*' or stack[-1] == '/' or stack[-1] == '+' or stack[-1] == '-':
                ans.append(stack.pop())
            else:
                break
        stack.append(i)
    else:
        ans.append(i)

while len(stack) > 0:
    ans.append(stack.pop())
ans_ = []
for i in range(len(ans)):
    if ans[i] != ' ':
        ans_.append(ans[i])
print(''.join(map(str,ans_)))
