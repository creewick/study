from os import walk, rename, remove, sep
from io import TextIOWrapper
from os.path import join
from sys import argv
from re import match
import logging


def main():
    logging.basicConfig(filename='log', level='INFO')
    for folder, file in get_files(dir=argv[1]):
        if is_md(file):
            menu = get_menu(folder, root=argv[2])
            try_replace_menu(folder, file, menu)


def get_files(dir):
    for folder, _, files in walk(dir):
        for name in files:
            yield folder, name


def is_md(file):
    return file[-3:] == '.md'


def get_menu(path, root):
    folders = path.split(sep)
    folders[0] = root
    count = len(folders)

    for i in range(count-1):
        title = folders[i]
        url = '../' * (count-1-i)

        folders[i] = f'[{title}]({url})'

    return ' > '.join(folders) + '\n\n'


def try_replace_menu(folder, file, menu):
    _path = join(folder, f'_{file}')
    path = join(folder, file)
    try:
        rename(path, _path)
        try:
            with open(_path, 'r') as old:
                with open(path, 'w') as new:
                    replace_menu(old, new, menu)
            remove(_path)
            logging.info(f'path: {path}, ok')
        except:
            logging.info(f'path: {path}, canceled')
            rename(_path, path)
    except:
        logging.info(f'path: {path}, skipped')


def replace_menu(old: TextIOWrapper, new: TextIOWrapper, menu):
    new.write(menu)
    text_started = False
    line = old.readline()

    while line != '':
        if not text_started and is_menu(line):
            old.readline()
        else:
            text_started = True
            new.write(line)

        line = old.readline()


def is_menu(line):
    return match(r'(\[.*?\]\((..\/)*\) > )',
                 line) is not None


if __name__ == '__main__': main()
