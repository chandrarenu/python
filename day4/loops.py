# while loop
i=0
while i<=10:
   print(f'{i} hello')
   if i==5:
       break
   i+=1

       
 

# For loops

fruits=[
    'apple',
    'banana',
    'orange',
    'grapes',
    'litchi',
    123,
    1.2
]

print("apple" in fruits)

for index,fruit in enumerate (fruits):
    print(index,fruit)
    
numbers=list(range(1,10,2))
print(numbers)

for i in range(10):
    print(i)
    
    if i == 3:
        break


 # for even number

for i in range(1,21):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i}is a odd")
        
        
        
#task 
#1
#12
#123



words="hello world"

for char in words:
    print(char)