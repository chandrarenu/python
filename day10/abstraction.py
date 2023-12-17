from abc import ABC, abstractmethod

class Computer(ABC):
    
    def run(self,app):
        self.process(app)
    
    @abstractmethod
    def process(self):
        pass
    
class Mobile(Computer):
    def process(self,app):
        print("Mobile is running",app)
        
class Laptop(Computer):
    def process(self,app):
        print("Laptop is running",app)
    
   
samsung=Laptop()
samsung.run("PUBG")