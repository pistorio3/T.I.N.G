import sys


def txt_importer(path_file):
    try:
        bool(path_file.split('.txt', 1)[1])
    except Exception:
        sys.stderr.write('Formato inválido\n')
    try:
        with open(path_file) as file:
            content = file.read()
            return content.splitlines
    except FileNotFoundError:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
