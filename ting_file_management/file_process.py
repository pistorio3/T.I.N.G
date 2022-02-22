import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for file in range(len(instance.data)):
        if path_file == instance.search(file)['nome_do_arquivo']:
            return None

    content = txt_importer(path_file)

    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content),
        "linhas_do_arquivo": content,
    }

    instance.enqueue(result)
    sys.stdout.write(str(result))


def remove(instance):
    if bool(instance.__len__()) is False:
        return sys.stdout.write('não há elementos\n')

    removed = instance.dequeue()

    sys.stdout.write(
        f"Arquivo {removed['nome_do_arquivo']} removido com sucesso\n"
    )
    print('test')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
