# property - свойство атрибута, т.е. методы которые применимы к нему
# getter - показывает значение приватной  переменной
# setter - устанавливает новое значение переменной
# deleter - удаляет эдемент
class BankAccount:

    def __init__(self, name, balance):
        # создаём приватные переменные к которых будем обращаться через другие функции
        self.__name = name
        self.__balance = balance

    # показываем баланс
    def get_balance(self):
        return self.__balance

    # изменяем баланс
    def set_balance(self, value):
        # isinstance(object, classinfo) - проверка есть ли в объекте элемент
        if not isinstance(value, (int, float)):
            raise ValueError("Вы ввели не число ")
        self.__balance = value

    def del_instance(self):
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance, fdel=del_instance)
