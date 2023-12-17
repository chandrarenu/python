#single inheritance
# class GrandFather:
#     house= "Luxerxy"
    
# class Father(GrandFather):
#     car= "Mercedes"
    
# Father=Father()
# print(Father.house)


#multiple inheritance

class GrandFather:
    
    house= "Luxerxy House"
    
    def __init__(self) -> None:
        print("GrandFather")
    
    def get_house(self):
        return self.house
    
    
class GrandMother:
    jewellary="suun wala diamond"
    
class Father(GrandFather,GrandMother):
    car= "Mercedes"
    
    def get_house(self):
        print(super().get_house())
        return "jhan ramro"
    
class Son(Father):
    console="PASS"
    
son=Son()
print(son.console)

print(isinstance(son,object))

    
Father=Father()
print(Father.house)