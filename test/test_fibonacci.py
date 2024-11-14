import pytest
from library.fibonacci import fibonacci


# Тест для корректных входных данных
def test_fibonacci_positive():
    # Проверяем последовательность Фибоначчи для различных значений n
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(6) == [0, 1, 1, 2, 3, 5]
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]


# Тест для некорректных данных (ошибка ValueError)
def test_fibonacci_negative():
    # Проверяем, что ошибка возникает при передаче отрицательных, нецелых чисел, строк и нуля
    with pytest.raises(ValueError):
        fibonacci(-5)

    with pytest.raises(ValueError):
        fibonacci(2.1)

    with pytest.raises(ValueError):
        fibonacci("wert")

    with pytest.raises(ValueError):
        fibonacci(0)


# Тест для граничных значений
def test_fibonacci_edge():
    # Проверка для минимального значения n
    assert fibonacci(1) == [0]

    # Проверка для последовательности из 2 чисел
    assert fibonacci(2) == [0, 1]
