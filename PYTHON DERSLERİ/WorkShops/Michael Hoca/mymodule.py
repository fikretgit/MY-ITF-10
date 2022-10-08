def my_function():
    print('Hello Michael')


person={'name':'Michael', 'profession':'Data Scientist'}

def calculator2():
    operation=input().split()
    a,o,b=int(operation[0]),operation[1],int(operation[2])
    
    if o=='+':
        return a+b
    elif o=='-':
        return a-b
    elif o=='*':
        return a*b
    elif o=='/':
        return a/b
    else:
        return ('Please enter a valid operator sign')


if (__name__=='__main__'):
    my_function()
    print(person)
    x=calculator2()
    print(x)