# создаём класс
class Mykalss:
    car = 'BMV'
    voulume = 2929



# Присваеваем переменной значение класса
callable_class = Mykalss()
# Меняем знасение элемента "car"
callable_class.car = 'Lada'
# Выводим значение "volume"
print("Volume = ", callable_class.voulume)
# выводим все объекты, которые есть в классе
print("\n", Mykalss.__dict__)
