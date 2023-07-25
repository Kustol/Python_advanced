'''
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
'''

import re
from collections import Counter

def most_frequent(text):
    words = re.findall(r'\b\w+\b', text.lower()) # использовала регулярку \w. поставила границы слова (\b), хотя в данном тексте и без них результат не меняется.
    return Counter(words).most_common(10)

text = """Вот дом,
        Который построил Джек.
        
        А это пшеница,
        Которая в темном чулане хранится
        В доме,
        Который построил Джек.

        А это веселая птица-синица,
        Которая часто ворует пшеницу,
        Которая в темном чулане хранится
        В доме,
        Который построил Джек.
        
        Вот кот,
        Который пугает и ловит синицу,
        Которая часто ворует пшеницу,
        Которая в темном чулане хранится
        В доме,
        Который построил Джек.
        
        Вот пес без хвоста,
        Который за шиворот треплет кота,
        Который пугает и ловит синицу,
        Которая часто ворует пшеницу,
        Которая в темном чулане хранится
        В доме,
        Который построил Джек.
        
        А это корова безрогая,
        Лягнувшая старого пса без хвоста,
        Который за шиворот треплет кота,
        Который пугает и ловит синицу,
        Которая часто ворует пшеницу,
        Которая в темном чулане хранится
        В доме,
        Который построил Джек.
        
        А это старушка, седая и строгая,
        Которая доит корову безрогую,
        Лягнувшую старого пса без хвоста,
        Который за шиворот треплет кота,
        Который пугает и ловит синицу,
        Которая часто ворует пшеницу,
        Которая в темном чулане хранится
        В доме,
        Который построил Джек.
        
        А это ленивый и толстый пастух,
        Который бранится с коровницей строгою,
        Которая доит корову безрогую,
        Лягнувшую старого пса без хвоста,
        Который за шиворот треплет кота,
        Который пугает и ловит синицу,
        Которая часто ворует пшеницу,
        Которая в темном чулане хранится
        В доме,
        Который построил Джек."""
print(most_frequent(text))