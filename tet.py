try:
    d = input('[enter  your postfix expression here] : ')
    k = []
    for i in d:
        if i in ['+','-','*']:
            k.append(i)
        else:
            k.append(int(i))
    stack = []
    for i in k:
        if i in ['+','-','*']:
            if i =='+':
                stack.append(stack.pop(-2) + stack.pop(-1))
            elif i == '-':
                stack.append(stack.pop(-2) - stack.pop(-1))
            elif i =='*':
                stack.append(stack.pop(-2) * stack.pop(-1))
            elif i == '/':
                stack.append(stack.pop(-2) / stack.pop(-1))
            else:
                stack.append(stack.pop(-2) % stack.pop(-1))

        else:
            stack.append(i)
    print(stack[0])
except :
    print(-1)














