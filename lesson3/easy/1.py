# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

def passport(name,age,city):
    print(name+',',age, 'год(a),', 'проживает в городе', city)

passport('Иван',21, 'Москва')