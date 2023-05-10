
# Нужно создать программу которая умножает 2 числа без оператора *
   
# Просим пользователя ввести первое число 
first_number = int(input("Введите число: "))
# Просим пользователя ввести второе число
second_number = int(input("Введите второе число: "))
# Создаём вспомогательную переменную для хранения промежуточных вычислений
assist = second_number
# Создаём цикл, в котором будем прибавлять second_number  к самому себе
# first_number раз
for i in range(1,first_number):    
    assist = second_number + assist
    
print(f'{first_number} * {second_number} = {assist}')