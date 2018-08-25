from os import walk, rename, remove, sep
from os.path import join
from sys import argv
from re import match


def get_files(dir):
    for path, _, files in walk(dir):
        for name in files:
            yield path, name


def is_md(filename):
    return filename[-3:] == '.md'


def is_menu(line):
    return match(r'(\[.*?\]\((..\/)*\) > )',
                 line) is not None


def get_menu(path, menu_name):
    result = ''
    folders = path.split(sep)

    for i in range(len(folders) - 2):
        title = folders[i]
        url = '../' * (len(folders) - 2 - i)

        result += f'[{title}]({url}) > '

    return result + folders[-2] + '\n'


def copy_with_menu(old, new, menu):
    new.write(menu)
    first = True

    for line in old:
        if not first or not is_menu(line):
            new.write(line)
            first = False


def update_menu(path, name, menu_name):
    _path = join(path, f'_{name}')
    path = join(path, name)
    try:
        rename(path, _path)
        try:
            with open(_path, 'r') as old:
                with open(path, 'w') as new:
                    menu = get_menu(path, menu_name)
                    copy_with_menu(old, new, menu)
            remove(_path)
        except:
            rename(_path, path)
    except:
        return


if __name__ == '__main__':
    for path, name in get_files(dir=argv[1]):
        if is_md(name):
            update_menu(path, name, menu_name=argv[2])
