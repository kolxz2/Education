# Публичные, приватные, защищённые атрибуты классса
class BancAccaont:

    def __init__(self, name, balance, passport):
        self._name = name
        self._balance = balance
        self._passport = passport

    # защищённые переменные ачинаються с '_ ...' к ним у пользователя есть доступ, но лучше их не использовать
    # через '__' создаём приватные переменные, доступ есть только внутри классса
    # Инкопсуляция - доступ к переменной есть только внутри класса или проедусмотренный программистом вне класса

    def print_protected_data(self):
        print(self._name, self._balance, self._passport)

    # инкапсуляция метода, доступ внутри класса
    def __print_protected_data(self):
        print(self._name, self._balance, self._passport)


account = BancAccaont('Nik', 100000, 7846467)
# н доступ к методу можно получить через '_ИмяКласса__метод()'
# так же получаем доступ к защтщённым атрибутам
print(account._BancAccaont__print_protected_data())
