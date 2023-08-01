'''
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
'''

def keyword_arguments_to_dict(**kwargs):
    result_dict = {}
    for key, value in kwargs.items():
        if isinstance(key, (int, float, str, tuple, frozenset)):
            result_dict[key] = value
        else:
            result_dict[str(key)] = value
    return result_dict

if __name__ == "__main__":
    result = keyword_arguments_to_dict(a=11, b="привет", c=(1, 2, 3), d=3.14, e=True, f=['January', 'February', 'March'])
    print(result)

