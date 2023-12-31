# Account class


class Account:
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password

    def get_balance(self, password):
        if password != self.password:
            print('Incorrect password.')
            return None
        return self.balance

    def deposit(self, usr_deposit, password):
        if usr_deposit < 0:
            print('You can\'t deposit a negative amount')
            return None
        if password != self.password:
            print('Incorrect password.')
            return None
        self.balance += usr_deposit
        return self.balance

    def withdrawal(self, usr_withdrawal, password):
        if usr_withdrawal < 0:
            print('You can\'t withdraw negative amount.')
            return None
        if password != self.password:
            print('Incorrect password.')
            return None
        self.balance -= usr_withdrawal
        return self.balance

    def show(self):
        print('Show: ')
        print(f'    Name: {self.name}')
        print(f'    Balance: {self.balance}')
        print()
