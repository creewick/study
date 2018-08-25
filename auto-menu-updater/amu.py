from os import walk, rename, remove, sep
from argparse import ArgumentParser
from re import match, compile
from io import TextIOWrapper
from os.path import join
import logging


regex = compile(r'(\[.*?\]\((..\/)*\) > )')


def main():
    logging.basicConfig(filename='log', level='INFO')
    args = get_args()

    for folder, file in get_files_paths(dir=args.root):
        if file.endswith('.md'):
            menu = get_menu(folder, root=args.name)
            try_replace_menu(folder, file, menu)


def get_args():
    parser = ArgumentParser(description='Update navigation links.')
    parser.add_argument('-r', '--root', type=str, required=True,
                        help='navigation start folder')
    parser.add_argument('-n', '--name', type=str, required=True,
                        help='navigation start name')
    return parser.parse_args()


def get_files_paths(dir):
    for folder, _, files in walk(dir):
        for name in files:
            yield folder, name


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
            rename(_path, path)
            logging.info(f'path: {path}, canceled')
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
    global regex
    return match(regex, line) is not None


if __name__ == '__main__': main()
