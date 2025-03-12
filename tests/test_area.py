import pytest  
from src.area import calculate_area_square  
  
def test_calculate_area_square_negative():  
    with pytest.raises(TypeError):  
        calculate_area_square(-2)  
  
def test_calculate_area_square_string():  
    with pytest.raises(TypeError):  
        calculate_area_square("2")  
  
def test_calculate_area_square_list():  
    with pytest.raises(TypeError):  
        calculate_area_square([2])

def test_calculate_area_square_accuracy():  
    # Last two digits of my student ID is 39 -- 100935039
    length = 40
    expected_area = 40 * 40
    assert calculate_area_square(length) == expected_area, f"Expected {expected_area}, but got {calculate_area_square(length)}"
