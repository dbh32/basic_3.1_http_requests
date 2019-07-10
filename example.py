import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

result_path = 'RU.txt'
source_path = 'ES.txt'
from_lang = 'es'


# to_lang='ru'

def write_results(result_path):
    def get_text(source_path):
        with open(source_path, encoding='utf-8') as source:
            return source.read()

    def translate_it(text, from_lang, to_lang='ru'):
        """
        https://translate.yandex.net/api/v1.5/tr.json/translate ?
        key=<API-ключ>
         & text=<переводимый текст>
         & lang=<направление перевода>
         & [format=<формат текста>]
         & [options=<опции перевода>]
         & [callback=<имя callback-функции>]

        :param to_lang:
        :return:
        """

        params = {
            'key': API_KEY,
            'text': text,
            'lang': '{}-{}'.format(from_lang, to_lang),
            # 'lang': 'ru',
        }

        response = requests.get(URL, params=params)
        json_ = response.json()
        return ''.join(json_['text'])

    with open(result_path, 'w') as results:
        results.write(translate_it(get_text(source_path), from_lang))


write_results(result_path)

# print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически определенного языка переводимого текста. Этому соответствует значение 1 этого параметра.', 'no'))
# requests.post('http://requestb.in/10vc0zh1', json=dict(a='goo', b='foo'))
