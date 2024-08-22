"""
Задание №3
📌 Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
📌 Каждый ключевой параметр сохраните как отдельный ключ
json словаря.
📌 Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
📌 Имя файла должно совпадать с именем декорируемой
функции.
"""
import json
import os.path
from typing import Callable


def main(func: Callable):
    def wrapper(*args, **kwargs):
        num = None
        cnt = None
        if 'num' in kwargs.keys():
            num = kwargs['num']
        if 'cnt' in kwargs.keys():
            cnt = kwargs['cnt']
        if len(args) == 2:
            num = args[0]
            cnt = args[1]
        elif len(args) == 1:
            if num == None:
                num = args[0]
            else:
                cnt = args[0]
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


def attemp(num: int, cnt: int) -> bool:
    current_attempt: int = 0
    while current_attempt < cnt:
        num_from_console = int(input("Введите число -> "))
        if num_from_console == num:
            return True
        current_attempt += 1
    return False


run = main(attemp)
if run(25, cnt=5):
    print("Вы угадали")
else:
    print("Попытки закончились")
