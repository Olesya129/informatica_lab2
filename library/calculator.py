def calculator(num1, num2, operation):
    """калькулятор"""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ZeroDivisionError("Деление на ноль невозможно.")
        return num1 / num2
    else:
        raise ValueError("Некорректная операция. Доступные операции: +, -, *, /")

