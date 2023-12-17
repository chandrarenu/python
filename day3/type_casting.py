pie=3.14
print(pie)
print(int(pie))

string="hello"         #string cannot be converted into number
int(string)             #string ma vako hello lai int or float ma convert grda error auxa

print(type(str(pie)))   #number can be converted into string


# converting list into tuple  (tuple directly convert hudina )
      #firtst tuple ma banaune
fruits=(
    'apple',
    'mango',
)
fruits=list(fruits)

fruits[0]= 'abc'
print(type(fruits))      #yo gresi tuple list ma convert vayo

print(tuple(fruits))     #yo list bata tuple ma convert vayo