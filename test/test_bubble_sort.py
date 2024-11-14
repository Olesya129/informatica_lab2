import pytest
from library.bubble_sort import bubble_sort

# Тест для нормальных данных
def test_bubble_sort_positive():
    assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]


def test_bubble_sort_edge():
    assert bubble_sort([]) == []                    # Тест для пустого списка
    assert bubble_sort([7]) == [7]                  # Тест для списка с одним элементом
    assert bubble_sort([7, 7, 7]) == [7, 7, 7]      # Тест для списка с одинаковыми элементами

# Тест для некорректных данных (например, строки)
def test_bubble_sort_negative():
    with pytest.raises(TypeError):
        bubble_sort([1, 2, "***", 4])
