'''
Задача 2 Создайте модуль с функцией внутри.
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”.
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
'''


from  random import randint as rndi
'''
Угадай число
'''

START = 0
STOP = 100
AMOUNT = 2

def get_random_num(start: int, end: int, amount = AMOUNT):
    flag = False
    num = rndi(start, end)
    while amount > 0:
      num_user = int(input('Введи число: '))
      if num_user == num:
          print('Угадал!\t')
          flag = True
      elif num_user < num:
          print('Выбери число больше!\t')
          amount -= 1
      elif num_user > num:
        print('Выбери число меньше! \t')
        amount -= 1
    return  flag




# Старт
if __name__ == "__main__":
    data = input('Введите началао диапозона и конец через пробел')
    start, stop = map(int,data.split())
    print(get_random_num(start,stop))