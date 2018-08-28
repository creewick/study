from os import walk, rename, remove, sep
from argparse import ArgumentParser
from re import match, compile
from io import TextIOWrapper
from os.path import join
import logging


def main():
    global latex_script
    latex_script = """<script type="text/x-mathjax-config">MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});</script><script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML' async></script>\n\n"""
    logging.basicConfig(filename='log')
    args = get_args()
    menu_regex = compile(rf'(\[.*?\]\((..\/)*\) > |{args.name})')
    latex_regex = compile(r'<script type="text/x-mathjax-config">')

    for folder, file in get_files_paths(dir=args.dir):
        if file.endswith('.md'):
            menu = get_menu(folder, name=args.name)
            try_update_file(folder, file, menu, menu_regex, latex_regex)


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


def try_update_file(folder, file, menu, menu_regex, latex_regex):
    _path = join(folder, f'_{file}')
    path = join(folder, file)
    log_path = path.encode('ascii', 'ignore').decode('ascii')
    try:
        rename(path, _path)
        try:
            with open(_path, 'r', encoding='utf-8', errors='ignore') as old:
                with open(path, 'w', encoding='utf-8', errors='ignore') as new:
                    update_file(old, new, menu, menu_regex, latex_regex)
            remove(_path)
            logging.info(f'path: {log_path}, ok')
        except Exception as e:
            remove(path)
            rename(_path, path)
            logging.error(f'path: {log_path}, canceled: {e}')
    except Exception as e:
        logging.warning(f'path: {log_path}, skipped: {e}')


def update_file(old: TextIOWrapper, new: TextIOWrapper, menu, menu_regex, latex_regex):
    global latex_script
    new.write(latex_script)
    new.write(menu)
    text_started = False
    line = old.readline()

    while line != '':
        if not text_started and match(menu_regex, line) or match(latex_regex, line):
            old.readline()
        else:
            text_started = True
            new.write(line)

        line = old.readline()


if __name__ == '__main__': main()
