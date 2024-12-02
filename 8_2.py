def summ(x, y):
    return x + y


def diff(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def degree(x, y):
    return x ** y


while True:
    try:
        a = int(input('Введите первое число:'))
        b = int(input('Введите второе число:'))
        break
    except ValueError:
        print('Вводите числа!')


operations = ['+', '-', '*', '/', '**']
while True:
    try:
        operation = input("Введите операцию: ")
        if operation not in operations:
            raise ValueError("Недопустимая операция, пожалуйста, выберите операцию из предложeнных")
        print(f"Вы выбрали операцию: {operation}")
        break
    except ValueError as e:
        print(e)

try:
    if operation == '+':
        print(f'{a} + {b} = {summ(a, b)}')
    elif operation == '-':
        print(f'{a} - {b} = {diff(a, b)}')
    elif operation == '*':
        print(f'{a} * {b} = {multiply(a, b)}')
    elif operation == '/':
        print(f'{a} / {b} = {divide(a, b)}')
    elif operation == '**':
        print(f'{a} ** {b} = {degree(a, b)}')
except ZeroDivisionError:
    print("На ноль делить нельзя")
except Exception as e:
    print(f'Failure: {e}')





