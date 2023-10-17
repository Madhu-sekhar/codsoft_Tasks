def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    if y==0:
        return 'it cant possible'
    else:
        return x//y
print('enter "+" for addition')
print('enter "-" for subtraction')
print('enter "*" for multiplication')
print('enter "/" for division')

op=input('Your operator:')
x = float(input('Enter your num1 value:'))
y = float(input('Enter your num2 value:'))
if op=='+':
    print('result:', add(x, y))
elif op=='-':
    print('result:', sub(x,y))
elif op=='*':
    print('result:', mult(x,y))
elif op=='/':
    print('result:', div(x,y))
else:
    print('invalid operator please re enter your operator')





