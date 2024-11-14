import pytest
from library.calculator import calculator

# Тесты для корректных операций
def test_calculator_positive():
    assert calculator(10, 5, '+') == 15
    assert calculator(10, 5, '-') == 5
    assert calculator(10, 5, '*') == 50
    assert calculator(10, 5, '/') == 2.0

# Тесты для граничных значений
def test_calculator_edge():
    with pytest.raises(ZeroDivisionError):
        calculator(10, 0, '/')

# Тесты для некорректных данных
def test_calculator_negative():
    with pytest.raises(ValueError):
        calculator(10, 5, '%')       # Некорректная операция
    with pytest.raises(TypeError):
        calculator("$$$", 5, '+')    # Некорректный тип для num1
    with pytest.raises(TypeError):
        calculator(10, "ке", '-')    # Некорректный тип для num2
