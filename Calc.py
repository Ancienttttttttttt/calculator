# Эта функция складывает два числа 
def add(x, y):
    return x + y

# Эта функция вычитает два числа
def subtract(x, y):
    return x - y

# Эта функция умножает два числа
def multiply(x, y):
    return x * y

# Эта функция делит два числа
def divide(x, y):
    return x / y


print("Выберите операцию.")
print("1.Сложить")
print("2.Вычесть")
print("3.Умножить")
print("4.Делить")

while True:
    # принять ввод от пользователя
    choice = input("Введите номер операции(1/2/3/4): ")

    # проверить, является ли выбор одним из четырех вариантов 
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Ввести первое число: "))
        num2 = float(input("Ввести второе число: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # проверить, хочет ли пользователь другой расчет
        # разорвать цикл while, если ответ отрицательный 
        next_calculation = input("Сделаем следующий расчет? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Неправильный ввод")
