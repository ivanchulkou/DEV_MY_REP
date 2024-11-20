while True:
    name = input("Как тебя зовут?: ")
    if name.lower() == 'выход':
        print("До свидания!")
        break
    print(f"Привет, {name}!")
