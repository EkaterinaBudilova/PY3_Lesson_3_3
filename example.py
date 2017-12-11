import requests
import os

def text_file(path):

    if os.path.isfile(path):
        with open(path, 'r') as file:
            text = str(file.read())
        return text
    else:
        print('Путь к файлу введен невнрно!')
        pass

def translate_it(text, to_lang, from_lang='ru'):

    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    params = {
        'key': key,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang),
    }

    response = requests.get(url, params=params).json()

    return ''.join(response.get('text', [])),

def result_file(path, text):

    with open(path, 'w') as file:
        result = file.write(text[0])
        return result

if __name__ == '__main__':

    path_to_text = input('Введите путь до файла с текстом: ')
    path_to_result = input('Введите путь до файла с переводом: ')
    translate_from = input('Введите язык текста [de, es, fr...]: ')
    translate_to = input('Введите язык перевода [ru, de, es...]: ')

    result = translate_it(text_file(path_to_text), translate_to, translate_from)
    result_file(path_to_result, result)
    print('Программа завершена!')