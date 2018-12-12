
__author__ = 'Сергей Ковригин'

import os
import sys

import hw05_easy as my

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


def main():
    while True:
        print(f'\nПуть = {os.getcwd()}\n',
              'Меню:',
              '    1. Перейти в папку...',
              '    2. Просмотреть содержимое текущей папки.',
              '    3. Удалить папку...',
              '    4. Создать папку...',
              '    5. Выход.', sep='\n')
        key = input('Введите число: ')
        if key == '1':
            cd(name())
        elif key == '2':
            my.ls_dirs('a')
        elif key == '3':
            my.rm_dirs(name())
        elif key == '4':
            my.mk_dirs(name())
        elif key == '5':
            sys.exit(0)


def name():
    name = input('Введите имя папки: ')
    return name if name else name()


def cd(dirs):
    try:
        os.chdir(dirs)
        print('Успешно перешел.')
    except FileExistsError:
        print(f'Невозможно перейти. Папки {dirs} не существует.')


if __name__ == '__main__':
    main()
