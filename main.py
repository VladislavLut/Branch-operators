
meters = float(input("Введіть кількість метрів: "))


units = input("Виберіть одиниці, в які потрібно конвертувати: 1 - милі, 2 - дюйми, 3 - ярди: ")


if units == "1":
    miles = meters * 0.000621371192
    print("Кількість миль:", miles)


elif units == "2":
    inches = meters * 39.3701
    print("Кількість дюймів:", inches)


elif units == "3":
    yards = meters * 1.0936133
    print("Кількість ярдів:", yards)

else:
    print("Неправильний вибір одиниць!")

