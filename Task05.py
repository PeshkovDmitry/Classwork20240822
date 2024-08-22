"""
Задание №5
📌 Объедините функции из прошлых задач.
📌 Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
📌 Выберите верный порядок декораторов.
"""

from typing import Callable
import json
import os.path
from random import randint


def check_params(func: Callable):
    def wrapper(*args, **kwargs):
        num, cnt = args
        if num not in range(1, 101):
            new_num = randint(1, 101)
            print(f'Загаданное число изменено с {num} на {new_num}')
            num = new_num
        if cnt not in range(1, 11):
            new_cnt = randint(1, 11)
            print(f'Количество попыток изменено с {cnt} на {new_cnt}')
            cnt = new_cnt
        args = (num, cnt)
        result = func(*args, **kwargs)
        return result

    return wrapper


def save_result(func: Callable):
    def wrapper(*args, **kwargs):
        num, cnt = args
        result = func(*args, **kwargs)
        info = []
        path = func.__name__ + '.json'
        if os.path.exists(path):
            with open(path, 'r') as f:
                info = json.load(f)
        with open(path, 'w') as f:
            info.append({'num': num, 'cnt': cnt, 'result': result})
            json.dump(info, f, indent=4)
        return result

    return wrapper


def count(num: int = 1):
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            result = []
            for cnt in range(num):
                print(f'Вызов функции {func.__name__} # {cnt}')
                result.append(func(*args, **kwargs))
            return result

        return wrapper

    return deco


@check_params
@save_result
@count(2)
def attempt(num: int, cnt: int) -> bool:
    current_attempt: int = 0
    while current_attempt < cnt:
        num_from_console = int(input("Введите число -> "))
        if num_from_console == num:
            print("Вы угадали")
            return True
        current_attempt += 1
        print("Вы не угадали")
    print("Попытки закончились")
    return False


print(attempt(25, 15))
