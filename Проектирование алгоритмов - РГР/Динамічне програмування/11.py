
def inToPost(eq):
    '''
            Only one digit numbers
    '''

    precedence = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
    stack = []
    post = []

    for c in eq:
        if c.isspace():
            continue
        elif c.isdigit():
            post.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            top = stack.pop()
            while top != '(':
                post.append(top)
                top = stack.pop()
        else:
            while len(stack) != 0 and precedence[stack[-1]] >= precedence[c]:
                post.append(stack.pop())
            stack.append(c)

    while len(stack) != 0:
        post.append(stack.pop())

    return post


def evalPost(post):
    stack = []

    for e in post:
        if e in '+-*/':
            op2, op1 = stack.pop(), stack.pop()
            if e == '+':
                stack.append(op1 + op2)
            elif e == '-':
                stack.append(op1 - op2)
            elif e == '*':
                stack.append(op1 * op2)
            else:
                stack.append(op1 / op2)
        else:
            stack.append(int(e))

    return stack.pop()


def calculate(equation):
    post = inToPost(equation)
    return evalPost(post)


print(calculate('2 + 2 * 2'))
print(calculate('(2 + 2) * 2'))
print(calculate('2 * (6 / 2 * 5) + 1'))
