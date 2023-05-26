from exercice1 import Calculator

def test_should_add():
    calc = Calculator()
    a = 3
    b = 7
    expected_value = 10
    assert calc.add(a, b) == expected_value
    
def test_should_sub():
    calc = Calculator()
    a = 30
    b = 7
    expected_value = 23
    assert calc.subtract(a, b) == expected_value
    
def test_should_mult():
    calc = Calculator()
    a = 3
    b = 7
    expected_value = 21
    assert calc.multiply(a, b) == expected_value
    
def test_should_div():
    calc = Calculator()
    a = 10
    b = 2
    expected_value = 5
    assert calc.divide(a, b) == expected_value
    
def test_should_pow():
    calc = Calculator()
    a = 3
    b = 2
    expected_value = 9
    assert calc.power(a, b) == expected_value

def test_should_sqrt():
    calc = Calculator()
    a = 4
    expected_value = 2
    assert calc.sqrt(a) == expected_value