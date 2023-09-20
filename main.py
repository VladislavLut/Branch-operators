
x = float(input("Введіть перше число: "))
y = float(input("Введіть друге число: "))
z = float(input("Введіть третє число: "))


operation = input("Виберіть операцію: 1 - сума, 2 - добуток: ")


if operation == "1":
    result = x + y + z
elif operation == "2":
    result = x * y * z
else:
    print("Неправильний вибір операції!")



print("Результат:", result)