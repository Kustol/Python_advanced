'''
Возьмите задачу о банкомате из семинара 2.
Напишите программу банкомат.
Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег

Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
'''
class Bank:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        if amount % 50 != 0:
            print('Сумма пополнения должна быть кратна 50 у.е.')
            return

        self.balance += amount
        self.transactions.append(f'Пополнение: +{amount} у.е.')

        if len(self.transactions) % 3 == 0:
            self.balance *= 1.03

        self.print_balance()

    def withdraw(self, amount):
        if amount % 50 != 0:
            print('Сумма снятия должна быть кратна 50 у.е.')
            return

        if amount > self.balance:
            print('Недостаточно средств на счете.')
            return

        if self.balance > 5000000:
            self.balance -= self.balance * 0.1

        fee = min(max(amount * 0.015, 30), 600)
        self.balance -= (amount + fee)
        self.transactions.append(f'Снятие: -{amount} у.е. (включая комиссию {fee} у.е.)')

        if len(self.transactions) % 3 == 0:
            self.balance *= 1.03

        self.print_balance()

    def print_balance(self):
        print(f'Текущий баланс: {self.balance} у.е.')

    def exit(self):
        print('Спасибо, что воспользовались услугами банка "Зойка - золотая ручка".')
        return False

    def print_transactions(self):
        print("История операций:")
        for transaction in self.transactions:
            print(transaction)

if __name__ == "__main__":
    bank = Bank()

    while True:
        print('Банк - "Зойка - золотая ручка". Позолоти процентами!"')
        print('Выберите действие:\n 1 - пополнить счёт\n 2 - снять со счёта\n 3 - вывести список операций\n 4 - выход')
        choice = input()

        if choice == '1':
            amount = int(input('Введите сумму для пополнения: '))
            bank.deposit(amount)
        elif choice == '2':
            amount = int(input('Введите сумму для снятия: '))
            bank.withdraw(amount)
        elif choice == '3':
            bank.print_transactions()
        elif choice == '4':
            bank.exit()
            break
        else:
            print('Вы выбрали несуществующий номер. Попробуйте снова.')

