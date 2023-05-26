from exercice3 import *


def test_should_calculate_rect():
    rect = Rectangle(2, 4)
    expected_area = 8
    expected_perimeter = 12
    assert rect.area() == expected_area
    assert rect.perimeter() == expected_perimeter
    
def test_should_calculate_circle():
    circ = Circle(2)
    expected_area = 12.566370614359172
    expected_perimeter = 12.566370614359172
    assert circ.area() == expected_area
    assert circ.perimeter() == expected_perimeter
    
def test_should_calculate_square():
    square = Square(5)
    expected_area = 25
    expected_perimeter = 20
    assert square.area() == expected_area
    assert square.perimeter() == expected_perimeter