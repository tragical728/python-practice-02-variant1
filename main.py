print("=== КОНСОЛЬНЫЙ КАЛЬКУЛЯТОР ===")

try:
    first = float(input("Введите первое число: "))
    operation = input("Введите операцию (+, -, *, /, //, %, ^): ")
    second = float(input("Введите второе число: "))

    if operation == "+":
        result = first + second
    elif operation == "-":
        result = first - second
    elif operation == "*":
        result = first * second
    elif operation == "/":
        if second == 0:
            print("Ошибка: деление на ноль.")
        else:
            result = first / second
    elif operation == "//":
        if second == 0:
            print("Ошибка: деление на ноль.")
        else:
            result = first // second
    elif operation == "%":
        if second == 0:
            print("Ошибка: деление на ноль.")
        else:
            result = first % second
    elif operation == "^":
        result = first ** second
    else:
        print("Ошибка: неизвестная операция.")

    if operation in ["+", "-", "*", "^"] or (
        operation in ["/", "//", "%"] and second != 0
    ):
        print(f"Результат: {result}")

except ValueError:
    print("Ошибка: необходимо вводить числа.")
