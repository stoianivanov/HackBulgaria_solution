class Bill:
    def __init__(self, amount):
        if amount <= 0:
            raise ValueError
        if not isinstance(amount, int):
            raise TypeError
        self.amount = amount

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return self.amount

    def __repr__(self):
        return "A {}$ bill".format(self.amount)


class BillBatch:
    def __init__(self, amount):
        self.amount = amount

    def __len__(self):
        return len(self.amount)

    def __getitem__(self, index):
        if index <= len(self.amount):
            return self.amount[index]
        else:
            raise TypeError

    def total(self):
        total = 0
        for i in range(0, len(self)):
            total += int(self.amount[i])
        return total


class CashDesk:
    def __init__(self, desk={}, total=0):
        if not isinstance(desk, dict) or not isinstance(total, int):
            raise TypeError
        if total < 0:
            raise ValueError
        self.desk = desk
        self.total = total

    def add_money(self, money):
        key = "{}$ bills".format(int(money))
        self.total += int(money)
        if key in self.desk:
            self.desk[key] = self.desk[key] + 1
        else:
            self.desk[key] = 1

    def take_money(self, money):
        if isinstance(money, Bill):
            self.add_money(money)
        elif isinstance(money, BillBatch):
            for i in money:
                self.add_money(i)

    def total(self):
        return self.total

    def inspect(self):
        print("We have a total of {} $ in the desk".format(self.total))
        print("We have the following count of bills, sorted in ascending order:")
        for bill in self.desk:
            print (bill + " - ")
            print (self.desk[bill])
