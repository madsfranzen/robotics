def hello_world():
    print("Hello Python\n")


hello_world()


def sum_list(list):
    sum = 0
    for num in list:
        sum += num
    return sum


list = [1, 2, 3, 4, 5]

print(sum_list(list))


class Bank_Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount

    def check_balance(self):
        print(self.balance)


account1 = Bank_Account()
account1.deposit(15000)
account1.check_balance()
account1.withdraw(20000)
account1.check_balance()
