from os import walk, rename, remove, sep
from argparse import ArgumentParser
from re import match, compile
from io import TextIOWrapper
from os.path import join
import logging


def main():
    global latex_script
    latex_script = """<script type="text/x-mathjax-config">MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});</script><script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML' async></script>\n"""
    logging.basicConfig(filename='log')
    args = get_args()
    menu_regex = compile(r'(\[.*?\]\((..\/)*\) > |{args.name})')
    latex_regex = compile(r'<script type="text/x-mathjax-config">')

    for folder, file in get_files_paths(dir=args.dir):
        if file.endswith('.md') and file != 'README.md':
            menu = get_menu(folder, file, root=args.name)
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


def get_menu(path, file, root):
    folders = path.split(sep)
    folders[0] = root

    for i in range(len(folders)-1):
        title = folders[i]
        url = '../' * (len(folders)-1-i)

        folders[i] = f'[{title}]({url})'
    
    if file != 'index.md':
        folders[-1] = f'[{folders[-1]}](./)'
        folders.append(file[:-3])
    
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
        if text_started:
            new.write(line)
        else:
            if not match(menu_regex, line) and not match(latex_regex, line) and line != '\n':
                text_started = True
                new.write(line)

        line = old.readline()


if __name__ == '__main__': main()
