while True:
    name = input("Введите ваше имя: ")
    if name.lower() == 'выход':
        print("До свидания!")
        break
    print(f"Привет, {name}!")
