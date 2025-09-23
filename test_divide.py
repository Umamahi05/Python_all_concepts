from testFile import divide

def test1():
    assert divide(6,2) == 3

def test2():
    assert divide(10.0,10.0) == 1.0
    
test1()
test2()