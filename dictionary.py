# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.

def dict_input(**kwargs):
    new_dict = {}
    for key, value in kwargs.items():
        try:
            new_dict[value] = key
        except:
            new_dict[str(value)] = key
    return new_dict


print(dict_input(bob='Moss', name='Филицисс', cat='Йотун', dog='Бисирис'))
