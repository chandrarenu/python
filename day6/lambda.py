# def sum_by_ten(a):
#     return a+10


# s= lambda a:a+10
# print(s(10))



#task multiple parameter

def mul(a,b):
    return a,b

s = lambda a,b:a*b
print(s(5,6))

def myfuc(n):
    return lambda X:X*n

#lambda X:X*2
doubler = myfuc(2)
print(doubler(10))
print(doubler(20))


def myfuc(n):
    return lambda X:X*n

#lambda X:X*3
tripler = myfuc(3)
print(tripler(10))
print(tripler(20))

def myfuc(n):
    return lambda X:X*n

#lambda X:X*4
fourler = myfuc(4)
print(fourler(10))
print(fourler(20))




