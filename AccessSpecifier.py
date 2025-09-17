#AccessSpecifier
class Parent():

    def __init__(self):
        self.publicvble = 10
        self._protectvble = 100 #var name must start with single underscore
        self.__privatevble = 1000 #var name must start with double underscore


    def display_values(self): 
        print(self.publicvble) #accesible from the same parent class
        print(self._protectvble) #accesible from the same parent class
        print(self.__privatevble) #accesible from the same parent class

    def public_method(self):
        print("I am a public method from the parent class")

    def _protect_method(self):
        print("I am a protected method from the parent class")

    def __private_method(self):
        print("I am a private method from the parent class")

    def access_from_sameclass(self):
        self.public_method()
        self._protect_method()
        self.__private_method()

    

class Child(Parent):

    def child_display(self):
        print(self.publicvble) #i am in Child class and its accessible the public  vble
        print(self._protectvble) #i am in Child class and its accessible the protected vble
        print(self._Parent__privatevble) # accessing the private vble from the child class, its not advisable
        try:
            print(self.__privatevble) #i am in Child class and its not accessible private class vlbe
        except AttributeError:
            print("Cannot access the Private vble")

    def access_from_subclass(self):
        self.public_method()
        self._protect_method()
        try:
            self.__private_method()
            #self._Parent__private_method()
        except AttributeError:
            print("cannot accss the private meth from the subclass")

class Stranger():

    def access_from_otherclass(self, obj):
        print(obj.publicvble) #Public vble accessing
        print(obj._protectvble) #Not recommended
        try:
            print(obj.__privatevble) #i am in Child class and its not accessible private class vlbe
        except AttributeError:
            print("Cannot access the Private vble")

    def access_method_from_othercls(self, obj):
        obj.public_method()
        obj._protect_method() # not advisable
        try:
            obj.__private_method()
            #self._Parent__private_method()
        except AttributeError:
            print("cannot accss the private meth from the subclass")

pobj = Parent()
pobj.display_values()
pobj.access_from_sameclass()

cobj = Child()
cobj.child_display()
cobj.access_from_subclass()

sobj = Stranger()
sobj.access_from_otherclass(pobj)
sobj.access_method_from_othercls(pobj)