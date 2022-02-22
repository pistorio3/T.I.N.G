def exists_word(word, instance):
    words_list = []

    for file in instance.data:
        occurrences = []

        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                info = ({"linha": index + 1})
            else:
                return words_list
            occurrences.append(info)

        if occurrences:
            words_list.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )
    return words_list


def search_by_word(word, instance):
    words_list = []

    for file in instance.data:
        occurrences = []

        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                info = ({"linha": index + 1, "conteudo": line})
            else:
                return words_list
            occurrences.append(info)

        if occurrences:
            words_list.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )
    return words_list
