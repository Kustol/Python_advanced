'''
Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%».
В результате получаем словарь с именем в качестве ключа
и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии
'''

def generate_dictionary(name, salary, bonus):
    return {name: salary * float(bonus.rstrip('%')) / 100 for name, salary, bonus in zip(name, salary, bonus)}

if __name__ == '__main__':
    name = ['Леонид', 'Артём', 'Ярослав']
    salary = [60000, 100000, 150000]
    bonus = ['10.25%', '5%', '12.5%']

    bonus_dict = generate_dictionary(name, salary, bonus)
    print(bonus_dict)