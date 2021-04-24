class Cat:

    # не корректная инициализация
    def set_value(self, value, age=0):
        self.name = value
        self.breed = age

    # __init__ - нужен для инициализации, заполнения объекта параметрами (атрибутами)
    def __init__(self, name, breed='seam', age=1, color='black'):
        print(f'Hello {name}, your breed is {breed}, color is {color} and you {age} years old cat')
        # Инициализируем переменные
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
