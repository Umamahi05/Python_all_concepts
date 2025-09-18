import math
#Classmethod-Staticmethod - DECORATORS
#@classmethod, @staticmethod - called directly using class name 
#@classmethod - controls the class level variable, cls is the first argument, alternative constructors
#@staticmethod - controls the variable within the static method.binds to the class, but it likes the standalone funtion

class CS:

    classvble = "WIPRO"
    
    def __init__(self,a,b):
        self.fnum = a
        self.snum = b
    
    @classmethod
    def cmethod(cls, newvalue):
        cls.classvble = newvalue
        return cls.classvble
    
    @staticmethod
    def calcArea(radius):
        return math.pi * radius * radius
    
    def addition(self):
        return (self.fnum + self.snum)
    

cobj = CS(100,1000)
print(CS.cmethod("Google"))
print(CS.calcArea(6))
print(cobj.addition())
