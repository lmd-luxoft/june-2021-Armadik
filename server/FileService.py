import os
from datetime import datetime, timezone


def create_dir(work_dir):
    """Создание рабочей директории"""
    if not os.path.exists(work_dir):
        os.mkdir(work_dir)


def get_files(args):
    """Get info about all files in working directory.
    """
    work_dir = args.folder
    if os.path.exists(work_dir):
        # Проверяем пустой ли каталог
        if not os.listdir(work_dir):
            print('Пустой')
        else:
            # Выводим список файлов
            print('Список объектов в нем: ', os.listdir(work_dir))
    else:
        create_dir(args.folder)
        # Возврат к выполнению функции
        get_files(args)


def get_file_data(args):
    """Get full info about file.
    """
    data_file = os.path.join(args.folder, args.file_name)
    try:
        with open(data_file, 'r') as fp:
            result = os.stat(data_file).st_mtime
            modified = datetime.fromtimestamp(result, tz=timezone.utc)
            print('data', modified)
    except:
        print('Файл не найден!')


def create_file(args):
    """Create a new file.
    """
    create_dir(args.folder)
    data_file = os.path.join(args.folder, args.file_name)
    create_dir(args.folder)
    with open(data_file, 'w+')as fp:
        print('Создание файла:', data_file)


def read_file(args):
    """Read a new file.
    """
    data_file = os.path.join(args.folder, args.file_name)
    try:
        with open(data_file, 'r') as fp:
            return fp.readline()
    except:
        print('Файл не найден')


def delete_file(args):
    """Delete file.
    """
    data_file = os.path.join(args.folder, args.file_name)
    print('Удаляю файл:', data_file)
    try:
        os.remove(data_file)
    except:
        print('Файл не найден!')
