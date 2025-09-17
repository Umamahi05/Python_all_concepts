from abc import ABC, abstractmethod
#Abstract - architect designing a model [login,logout,order,checkout - Food ind]
#Obj cant be created for the Abstract class
#the method defined under @abstractmethod must be used in the child class with the definition

class FPlan(ABC):

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

    def checkout(self):
        print( "I am a method from the Parent - Abstract class")

    def order(self):
        pass


class abschild(FPlan):

    def login(self):
        print("Since the login method is mentioned as abstract method , \n i must implement the functionality for this method")

    def logout(self):
        print("Same like login method, i must imp my functionality ")

    def checkout(self):
        print("I am an ordinary func from abstract class, yet i want to use the abstract class func")
        return super().checkout()
    
    def order(self):
        print("I am an ordinary function from abstract class.\n Iam doing method overriding \n I am implementing my own functionality")

    

child1 = abschild()
child1.login()
child1.logout()
child1.checkout()
child1.order()



