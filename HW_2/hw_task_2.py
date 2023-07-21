'''
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions.
'''

def main():

    fraction1_str = str(input("Введите 1-ю дробь: "))
    fraction2_str = str(input("Введите 2-ю дробь: "))

    def process_fractions(fraction1_str, fraction2_str):

        # Преобразуем дроби из строк в числа
        number1, denom1 = map(int, fraction1_str.split("/"))
        number2, denom2 = map(int, fraction2_str.split("/"))

        # Сумма дробей
        sum_fraction_num = number1 * denom2 + number2 * denom1
        sum_fraction_denom = denom1 * denom2
        sum_fraction = (sum_fraction_num, sum_fraction_denom)

        # Произведение дробей
        prod_fraction_num = number1 * number2
        prod_fraction_denom = denom1 * denom2
        prod_fraction = (prod_fraction_num, prod_fraction_denom)

        return sum_fraction, prod_fraction


    sum_fraction, prod_fraction = process_fractions(fraction1_str, fraction2_str)

    print(f"Сумма дробей {fraction1_str} и {fraction2_str} - {sum_fraction[0]}/{sum_fraction[1]}")
    print(f"Произведение дробей {fraction1_str} и {fraction2_str} - {prod_fraction[0]}/{prod_fraction[1]}")

# Старт
if __name__ == "__main__":
    main()