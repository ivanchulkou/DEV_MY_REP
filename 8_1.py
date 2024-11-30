while True:
    try:
        weight = int(input('Введите ваш вес, кг:'))
        height = float(input('Введите ваш рост, м:'))
        if weight < 0 or height < 0:
            raise ValueError("Рост/вес не могут быть отрицательными!")
        imt = weight / (height ** 2)
        print(f'Ваш индекс массы тела: {imt}')
        break
    except ValueError:
        print('Вводите числа!')
    except ZeroDivisionError:
        print('Нельзя делить на 0')
    if weight < 0 or height < 0:
        raise ValueError("Рост/вес не могут быть отрицательными!")

if imt <= 16:
    print('У вас выраженный дефицит массы тела.')
if 16 <= imt < 18:
    print('У вас недостаточная масса тела.')
if 18 <= imt < 25:
    print('Ваша масса тела в норме.')
if 25 <= imt < 30:
    print('У вас избыточная масса тела.')
if 30 <= imt < 35:
    print('У вас ожирение первой степени.')
if 35 <= imt < 40:
    print('У вас ожирение второой степени.')
if imt >= 40:
    print('Вероятно, вы - Эрик Картман!')
