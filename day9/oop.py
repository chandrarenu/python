class House:
    # window=3
    # door=1
    # color="blue"
    
    def __init__(self,name,window=2,color="blue",door=3,price=1000):
        self.price=price
        self.name=name
        self.window=window
        self.color=color
        self.door=door
        
    def __str__(self) -> str:
        return f"{self.name} ko ghar"
    
    def __eq__(self, value: object) -> bool:
        return self.window==value.window
    
    def __gt__(self,value) -> bool:
        return self.price==value.price
        
        
    
    def set_color(self,color):
        self.color=color
        
    def get_color(self):
        return self.color
    
ram_ko_ghar=House(name="ram")
print(ram_ko_ghar)
shyam_ko_ghar=House(name="shyam",color="green")
# # ram_ko_ghar.set_color("red")
# print(ram_ko_ghar.get_color())
# print(shyam_ko_ghar.get_color)
# # print(ram_ko_ghar.window)


    