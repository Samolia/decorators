from datetime import datetime as dt
from application.dir_create import dir_create


def path_to_logs(path):
    def my_logger(old_function):
        def new_function(*args, **kwargs):
            print(f'Логи успешно записаны. Проверьте файл - {kwargs["file_name"]}')
            result = old_function(*args, **kwargs)
            with open(f'{path}/{kwargs["file_name"]}', 'a', encoding='utf-8') as log:
                log.write(f'Вызвана функция: "{old_function.__name__}"\n')
                log.write(f'Дата и время вызова функции: "{old_function.__name__}" - {dt.now()}\n')
                log.write(f'Аргументы, с которыми вызвалась функция: {args}\n')
                log.write(f'{kwargs["text"]} {args} - {result}\n\n')
            return result
        return new_function
    return my_logger


@path_to_logs(dir_create('output'))
def my_fibonacci(n: int, file_name: str, text: str):
    fib1 = fib2 = 1
    while n > 2:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1
    return fib2


@path_to_logs(dir_create('output'))
def area_of_a_rectangle(a, b, file_name, text):
    return a * b
