# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil
import re
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print('cp < file_name > - создает копию указанного файла')
    print('rm <file_name> - удаляет указанный файл (запросить подтверждение операции)')
    print('cd <full_path or relative_path> - меняет текущую директорию на указанную')
    print('ls - отображение полного пути текущей директории')

def copy_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(os.getcwd(), dir_name)
    try:
        shutil.copyfile(file_path, file_path + '.copy')
        print('копия файла {} создана'.format(dir_name))
    except FileNotFoundError:
        print('файл {} не существует'.format(dir_name))
    except OSError:
        print('Синтаксическая ошибка в имени файла')


def remove_file():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    file_path = os.path.join(os.getcwd(), dir_name)
    choice = input('Вы точно хотите удалить файл {}? (y/n)'.format(dir_name))
    if choice == 'y' or choice == 'Y':
        try:
            os.remove(file_path)
            print('файл {} удален'.format(dir_name))
        except FileNotFoundError:
            print('файл {} не существует'.format(dir_name))
        except PermissionError:
            print('нет доступа к файлу {}'.format(dir_name))
        except OSError:
            print('Синтаксическая ошибка в имени файла, имени папки или метке тома')
    else:
        print('отмена удаления файла')

def change_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    # Проверка какой путь введен (относительный или абсолютный)
    pattern_dir = '^[a-zA-Z]:\\\\'
    search_pattern = re.search(pattern_dir, dir_name)
    if search_pattern:
        dir_path = os.path.join(os.getcwd(), dir_name)
        try:
            os.chdir(dir_path)
            print('вы в директории {}'.format(dir_path))
        except FileNotFoundError:
            print('директории {} не существует'.format(dir_path))
        except OSError:
            print('Синтаксическая ошибка в имени файла, имени папки или метке тома')
    else:
        dir_path = os.path.join(os.getcwd(), dir_name)
        try:
            os.chdir(dir_path)
            print('вы в директории {}'.format(dir_path))
        except FileNotFoundError:
            print('директории {} не существует'.format(dir_path))
        except OSError:
            print('Синтаксическая ошибка в имени файла, имени папки или метке тома')

def list_dir():
    print(os.getcwd())


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": remove_file,
    "cd": change_dir,
    "ls": list_dir
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")