# объявляем класс
class Cat:
    # создаём переменнную всего класса общую
    breed = 'pers'

    # self - оъект от которого вызван метод;
    # Метод - тоже функция но внутри класса, привязанная к конкретному объекту
    def hello(self):
        print('Hello word from kitty', self)

    # описываем новый метод для показывания породы
    def show_breed(self):
        # вводим эф строку
        print(f'My breed is {self.breed}')

    # Метод для показываения клички и имени
    # создаём внутри функции переменную имени и бкдем ко всем обращаться как Том, пока не поменяем
    def show_name(self, name='Tom'):
        # присваеваем оъекту класса 'name' значение 'name'
        self.name = name
        print(f'Hello {self.name} your breed is {self.breed}')

