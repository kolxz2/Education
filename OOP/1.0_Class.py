# создаём класс
class Mykalss:
    car = 'BMV'
    voulume = 2929


callable_class = Mykalss()
callable_class.car = 'Lada'
print("Volume = ", callable_class.voulume)
print("\n", Mykalss.__dict__)
