from Parent_Inheritance import dad

#Class_Object - Maintainability, Reusability, Readability
#Class - blueprint ex: Classroom
#Object - allocate space
#self - to notify which obj is calling the class, always 1st argument
#constructor - __init__ -  creating instance vbles and store the value those passed
'''
class Student:

    def say_hello(self):
        print("Hi I am a student")


s1 = Student()
s1.say_hello()



class Student:

    def __init__(self,s_name,s_age):
        self.name = s_name # stored once
        self.age = s_age # stored once

    
    def display_name_and_age(self):
        print(f"Name: {self.name} and Age : {self.age}")


stud1 = Student("Nan",21)
stud2 = Student("Kan",32)

stud1.display_name_and_age()
stud2.display_name_and_age()


# Class without constructor
class Mathtools:

    def square(self,num):
        return num * num
    
    def cube(self,num):
        return num * num * num
    

obj1 = Mathtools()
print(obj1.cube(12))
print(obj1.square(4))
'''

# Inheritance - Reuse the code - resuability
'''
class dad:

    def house(self):
        print("White")

'''
class son(dad): # creating relationships - Here 2 clases are in the same file. 

    def factory(self):
        print("Red")

    def house(self):
        print("Green")

son_obj = son()
son_obj.factory()
son_obj.house() 



