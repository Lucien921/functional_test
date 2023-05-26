from exercice2 import StringAnalyzer

def test_should_count_vowels():
    str = StringAnalyzer("coucou")
    expected_value = 4
    assert str.count_vowels() == expected_value
    
def test_should_count_consonants():
    str = StringAnalyzer("coucou")
    expected_value = 2
    assert str.count_consonants() == expected_value
    
def test_should_count_digit():
    str = StringAnalyzer("coucou1")
    expected_value = 1
    assert str.count_digits() == expected_value
    
def test_should_count_words():
    str = StringAnalyzer("coucou ca va")
    expected_value = 3
    assert str.count_words() == expected_value
    
def test_should_count_lines():
    str = StringAnalyzer("Coucou\nComment ca va ?")
    expected_value = 2
    assert str.count_lines() == expected_value