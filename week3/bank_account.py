class BankAccount:
    def __init__(self, name, balance, currency):
        if name == "":
            raise ValueError
        if balance < 0:
            raise ValueError
        if currency == "":
            raise ValueError
        self.__name = str(name)
        self.__balance = balance
        self.__currency = str(currency)
        self.__history = ["Account was created"]

    def holder(self):
        return self.__name


    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.__name, self.__balance, self.__currency)

    def __repr__(self):
        return "{} : {}{}".format(self.__name, self.__balance, self.__currency)

    def __int__(self):
        return int(self.__balance)

    def deposit(self, amount):
        if amount < 0:
            raise ValueError
        self.__balance += amount
        self.update_history("Deposited {}{}".format(amount, self.__currency))

    def update_history(self, text):
        self.__history.append(text)

    def balance(self):
        self.update_history("Balance check -> {}{}".format(self.__balance, self.__currency))
        return int(self.__balance)

    def withdraw(self, amount):
        if self.__balance < amount:
            return False
        else:
            self.__balance = self.__balance - amount
            self.update_history('{}{} was withdrawed'.format(amount, self.__currency))
            return True

    def history(self):
        return self.__history

    def transfer_to(self, account, amount):
        if isinstance(account, BankAccount):
            if self.__balance > amount:
                self.update_history("Transfer to {} for {}{}".format(account.__name, amount, self.__currency))
                return True
            else:
                return False
        else:
            return False
