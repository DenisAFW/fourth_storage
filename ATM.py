# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег


# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список

def main():
    choice = 0
    count = 3
    money = 0
    result = []
    print('\nДобро пожаловать в банкомат')
    while choice != 4:
        print('\nВведите номер желаемой операции:')
        print('1 - пополнение счета,')
        print('2 - снятие суммы,')
        print('3 - проведенные операции, ')
        print('4 - выход')
        count -= 1
        choice = int(input('Введите номер операции '))

        if count == 0:
            refill = money * 0.03
            money += refill
            count = 3
            print(f'\nОпераций до бонуса -> {count}')
            print(
                f'\nВы выполнили 3 операции, за это вам начислены 3% от общей сумму равные {money}, процент равен {refill}')

        if choice == 1:
            money = write_on_money(money)
            result.append('Внесение средств')
        elif choice == 2:
            money = write_off_money(money)
            result.append('Снятие средств')
        elif choice == 3:
            print('\nВсе проведенные операции:')
            for i in range(len(result)):
                print(result[i])
        elif choice == 4:
            print('Спасибо за пользование нашим банком!')
        else:
            print('Больше функций нет!')


def write_on_money(money):
    print(f'Текущая сумма на счете - {money}')
    if money > 5000000:
        tax = money * 0.1
        money -= tax
        print(f'Произведены вычеты из суммы в размере {tax}, текущая сумма на счете - {money}, соболезную, ваш банк')

    input_money = int(input('Введите сумму пополнения счета, вводимая сумма должна быть кратна 50 у.е. '))

    if input_money % 50 == 0:
        write_on = input_money * 0.015
        if write_on < 30:
            write_on = 30
            money -= write_on - input_money
            print(f'Счет пополненен на сумму {input_money}, процент за операцию {write_on}')
            print(f'Текущее состояние счета - {money}')
            return money
        elif write_on > 600:
            write_on = 600
            money -= write_on - input_money
            print(f'Счет пополненен на сумму {input_money}, процент за операцию {write_on}')
            print(f'Текущее состояние счета - {money}')
            return money
        else:
            money -= write_on - input_money
            print(f'Счет пополненен на сумму {input_money}, процент за операцию {write_on}')
            print(f'Текущее состояние счета - {money}')
            return money
    else:
        print('Введена неверная сумма')


def write_off_money(money):
    print(f'Текущая сумма на счете - {money}')
    if money > 5000000:
        tax = money * 0.1
        money -= tax
        print(f'Произведены вычеты из суммы в размере {tax}, текущая сумма на счете - {money}, соболезную, ваш банк')

    output_money = int(input('Введите сумму снятия со счета, вводимая сумма должна быть кратна 50 у.е. '))

    if output_money % 50 == 0:
        write_off = output_money * 0.015  # ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
        if output_money < money:
            if write_off < 30:
                write_off = 30
                money -= write_off + output_money
                print(f'Вы сняли со счета {output_money}, процент за операцию {write_off}')
                print(f'Текущее состояние счета - {money}')
                return money
            elif write_off > 600:
                write_off = 600
                money -= write_off + output_money
                print(f'Вы сняли со счета {output_money}, процент за операцию {write_off}')
                print(f'Текущее состояние счета - {money}')
                return money
            else:
                money -= write_off + output_money
                print(f'Вы сняли со счета {output_money}, процент за операцию {write_off}')
                print(f'Текущее состояние счета - {money}')
                return money
        else:
            print(f'Указанная сумма {output_money} превышает сумму на счете {money}!')
    else:
        print('Введена неверная сумма')


if __name__ == '__main__':
    main()
