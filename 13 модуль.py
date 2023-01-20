tickets = int(input('Введите количество билетов: '))
n = tickets
price = 0
sale = 0
while n != 0:
    age = int(input('Введите возраст посетителя: '))
    if age < 18:
        print('Вы проходите бесплатно')
    elif 18 <= age < 25:
        price += 990
        print('Стоимость билета 990 руб.')
    else:
        price += 1390
        print('Стоимость билета 1390 руб.')
    n -= 1

if tickets > 3:
    sale = price - ((price / 100) * 10)
    print(f'Сумма  {sale} руб., учитывая скидку')
else:
    print(f'Сумма к оплате {price} руб.')








