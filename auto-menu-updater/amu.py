from os import walk, rename, remove, sep
from argparse import ArgumentParser
from re import match, compile
from io import TextIOWrapper
from os.path import join
import logging


def main():
    logging.basicConfig(filename='log', level='INFO')
    args = get_args()
    regex = compile(rf'(\[.*?\]\((..\/)*\) > |{args.name})')

    for folder, file in get_files_paths(dir=args.dir):
        if file.endswith('.md'):
            menu = get_menu(folder, name=args.name)
            try_replace_menu(folder, file, menu, regex)


def get_args():
    parser = ArgumentParser(description='Update navigation links.')
    parser.add_argument('-d', '--dir', type=str, required=True,
                        help='navigation start folder')
    parser.add_argument('-n', '--name', type=str, required=True,
                        help='navigation start name')
    return parser.parse_args()


def get_files_paths(dir):
    for folder, _, files in walk(dir):
        for name in files:
            yield folder, name


def get_menu(path, name):
    folders = path.split(sep)
    folders[0] = name
    count = len(folders)

    for i in range(count-1):
        title = folders[i]
        url = '../' * (count-1-i)

        folders[i] = f'[{title}]({url})'

    return ' > '.join(folders) + '\n\n'


def try_replace_menu(folder, file, menu, regex):
    _path = join(folder, f'_{file}')
    path = join(folder, file)
    try:
        rename(path, _path)
        try:
            with open(_path, 'r') as old:
                with open(path, 'w') as new:
                    replace_menu(old, new, menu, regex)
            remove(_path)
            logging.info(f'path: {path}, ok')
        except Exception as e:
            rename(_path, path)
            logging.error(f'path: {path}, canceled: {e}')
    except Exception as e:
        logging.warning(f'path: {path}, skipped: {e}')


def replace_menu(old: TextIOWrapper, new: TextIOWrapper, menu, regex):
    new.write(menu)
    text_started = False
    line = old.readline()

    while line != '':
        if not text_started and is_menu(line, regex):
            old.readline()
        else:
            text_started = True
            new.write(line)

        line = old.readline()


def is_menu(line, regex):
    return match(regex, line) is not None


if __name__ == '__main__': main()
