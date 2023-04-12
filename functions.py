# Пользователь вводит число.
# Программа выводит список всех простых чисел, не превосходящих введённое число


num = int(input('Введите число '))

def prime(number):
	# устанавливает счетчик делителей в 0
	counter_divs = 0
	# первое число для проверки, является ли оно делителем
	index = 2
	# цикл для поиска делителей, отличных от 1 и самого числа
	while (counter_divs == 0) and (index < number):
		# проверяет является ли число в index делителем number
		if number % index == 0:
			# если да, то число number не является простым 
			return False
		# берем следующее число для проверки
		index += 1
	# если дошли до этого шага, то число number является простым 
	return True

# цикл проверяет числа от 2 до введёного на простоту
for i in range(2, num):	
	if prime(i):
		# если число простое, выводим его на экран
	    print(i)		  