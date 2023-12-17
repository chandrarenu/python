def sum(*numbers):
    total = 0
    for number in numbers:
        total+=number
    print(total)
        
sum(1,2,3,4)


#task

def introduction(*names):
    
    for name in names:
        print(f'My name is {name}')
        
introduction("Renu")
introduction("Sabita", "Sita")



# def introduction(name, *args):
#      print(f"My name is {name}.")
#      for arg in args:
#       print(f"I am {arg}.")
      
# introduction("ram", 20, "IT engineer")
# introduction("sita", 25, "doctor")

    

