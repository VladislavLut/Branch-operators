
x = float(input("Введіть перше число: "))
y = float(input("Введіть друге число: "))
z = float(input("Введіть третє число: "))


operation = input("Виберіть операцію: 1 - максимум, 2 - мінімум, 3 - середньоарифметичне: ")


if operation == "1":
    result = max(x, y, z)
elif operation == "2":
    result = min(x, y, z)
elif operation == "3":
    result = (x + y + z) / 3
else:
    print("Неправильний вибір операції!")


print("Результат:", result)