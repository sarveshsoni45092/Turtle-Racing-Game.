def sum(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multi(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

def math(n1,n2,func):
    return func(n1,n2)


ans =math(3,5,sum)

print (ans)