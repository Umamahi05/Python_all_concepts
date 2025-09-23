from functools import partial

def outer(msg):
    def inner():
        return(f"Message is : {msg}")
    return inner


ret_func  = outer("Welcome here!!!")
print(ret_func())


def calculateRate(amount, taxrate):
    return (amount * (1+taxrate))

price_with_gst = partial(calculateRate,taxrate=0.18)

print(price_with_gst(1000))
print(price_with_gst(1200))

#Composed func:output of one function becomes the input of one func. f(g(x))

def add(x):
    return x+2

def multiply(y):
    return y * 2

def composed(x):
    return add(multiply(x))

print(composed(2))

# A Callback function is a func that you pass as an arg to another func, 
# so that it can be called(exec later), after sone action is completed.

def on_button_click(callback):
    print("Button clicked")
    callback()

def message():
    print("Hello Welcome!!")

on_button_click(message)

# Recursive function - func that calls itself inorder to solva
# a smaller version of the same pbm.

def fact(n):
    if n==1:
        return 1
    return (n * fact(n-1))


print(fact(5))

# Generator function (Yield) to return values one by one, instead of return everything at once
def get_nums(n):
    for i in range(n):
        yield i

for num in get_nums(5):
    print(num)





