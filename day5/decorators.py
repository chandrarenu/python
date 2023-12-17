# def star(func):
#     def wrapper():
#         print("*"*10)
#         func()
#         print("*"*10)
#     return wrapper

# @star
# def hello():
#     print('hello')
    
# hello()

# @star
# def world():
#     print('world')

def hash_star(func):
    def wrapper():
        print("#"*10)
        print("*"*10)
        func()
        print("*"*10)
        print("#"*10)
    return wrapper

@hash_star
def world():
    print('world')
world()




    