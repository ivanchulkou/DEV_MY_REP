import time


def decorator_function(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function(*args, **kwargs)
        end_time = time.time()
        whole_time = end_time - start_time
        print(f'Время затраченное на выполнение функции: {whole_time} c')

    return wrapper


@decorator_function
def some_function(*args, **kwargs):
    print(type(args))
    print(type(kwargs))
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)
    time.sleep(3)  # добавляем задержку на 3 секунды, чтобы не выдавало пезультат 0.0 с


some_function(1, 2, 3, '4', key1=10, key2=20, key3=30)
