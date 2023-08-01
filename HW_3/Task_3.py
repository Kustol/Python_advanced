'''
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
'''


items = {'топор': 2, 'котелок': 1, 'палатка': 3, 'одежда': 2, 'еда': 4, 'лодка': 10}
max_weight = 12
def pack_backpack(items, max_weight):
    possible_items = []
    for item, weight in items.items():
        if weight <= max_weight:
            possible_items.append(item)
            max_weight -= weight
    return possible_items


print(pack_backpack(items, max_weight))