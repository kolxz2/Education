class BankAccount:

    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    @property
    def my_balance(self):
        return self.__balance

    @my_balance.setter
    def my_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Вы ввели не число ")
        self.__balance = value

    @my_balance.deleter
    def my_balance(self):
        del self.__balance

    ''':cvar
    my_balance = property()
    my_balance = my_balance.getter(get_balance)
    my_balance = my_balance.setter(set_balance)
    my_balance = my_balance.deleter(del_instance)
    '''

    '''
    balance = property(fget=get_balance(), fset=set_balance(), fdel=delete_balance())
    '''