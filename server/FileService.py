import os
import pathlib

def create_dir(work_dir):
    """Создание рабочей директории"""
    if os.path.exists(work_dir):
        print('КАТАЛОГ:', work_dir)
        # Проверяем пустой ли каталог
        if os.listdir(work_dir) == []:
            print('Пустой')
        else:
            # Выводим список файлов
            print('Список объектов в нем: ',os.listdir(work_dir))
    else:
        print('Создание директории:', work_dir)
        # Создаем директорию для файла
        os.mkdir(work_dir)


def get_files(args):
    """Get info about all files in working directory.

    Returns:
        List of dicts, which contains info about each file. Keys:
        - name (str): filename
        - create_date (datetime): date of file creation.
        - edit_date (datetime): date of last file modification.
        - size (int): size of file in bytes.
    """
    work_dir=args.folder
    if os.path.exists(work_dir):
            print('КАТАЛОГ:', work_dir)
            # Проверяем пустой ли каталог
            if os.listdir(work_dir) == []:
                print('Пустой')
            else:
                # Выводим список файлов
                print('Список объектов в нем: ',os.listdir(work_dir))
    else:
        create_dir(args.folder)
        # Возврат к выполнению функции
        get_files(args)

    pass


def get_file_data(args):
    """Get full info about file.

    Args:
        filename (str): Filename.

    Returns:
        Dict, which contains full info about file. Keys:
        - name (str): filename
        - content (str): file content
        - create_date (datetime): date of file creation
        - edit_date (datetime): date of last file modification
        - size (int): size of file in bytes

    Raises:
        RuntimeError: if file does not exist.
        ValueError: if filename is invalid.
    """
    data_file = str(args.folder + '/' + args.file_name)
    print('Проверяю файл:', data_file)
    try:
        with open(data_file,'r') as fp:
            print(os.stat(data_file))
    except:
        print('Файл не найден!')

    pass


def create_file(args):
    """Create a new file.

    Args:
        filename (str): Filename.
        content (str): String with file content.

    Returns:
        Dict, which contains name of created file. Keys:
        - name (str): filename
        - content (str): file content
        - create_date (datetime): date of file creation
        - size (int): size of file in bytes

    Raises:
        ValueError: if filename is invalid.
    """
    create_dir(args.folder)
    data_file = str(args.folder + '/' + args.file_name)
    print('Проверяю файл:', data_file)
    try:
        with open(data_file,'r') as fp:
            fp.readline()
            print('Файл создан:', data_file)
    except:
        print('Создание файла:', data_file)
        file = open(data_file, 'w+')

    pass

def read_file(args):
    """Read a new file.
    """
    data_file = str(args.folder + '/' + args.file_name)
    print('Проверяю файл:', data_file)
    try:
        with open(data_file,'r') as fp:
            print(fp.readline())
    except:
        print('Файл не найден')

    pass


def delete_file(args):
    """Delete file.

    Args:
        filename (str): filename

    Raises:
        RuntimeError: if file does not exist.
        ValueError: if filename is invalid.
    """
    data_file = str(args.folder + '/' + args.file_name)
    print('Удаляю файл:', data_file)
    try:
        os.remove(data_file)
    except:
        print('Файл не найден!')
    pass
