# a=10

# def number():
#     a=11
#     print(a)
    
# number()
# print(a)

# a=10
# def number():
#     global a    #override function
#     a=11
#     print(a)
    
# number()
# print(a)

a=10
def outer():
    a=11
    def inner():
        
        print("inner sees a as", a)
    inner()
    print("outer sees a as", a)
    
outer()
print("main sees a as", a)



#list ma append() function xa 