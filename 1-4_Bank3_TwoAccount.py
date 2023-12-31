# Non-OOP
# Bank version #3
# Two accounts

account0_name = ""
account0_balance = 0
account0_password = ''
account1_name = ""
account1_balance = 0
account1_password = ''

def new_account(account_num: int, name: str, balance: int, password: str):
    global account0_name, account0_balance, account0_password
    global account1_name, account1_balance, account1_password
    if account_num == 0:
        account0_name = name
        account0_balance = balance
        account0_password = password

    if account_num == 1:
        account1_name = name
        account1_balance = balance
        account1_password = password

def get_balance(account_num: int, password: str):
    global account0_balance, account0_password
    global account1_balance, account1_password
    if account_num == 0:
        if password != account0_password:
            print('Incorrect password.')
            return None
        return account0_balance

    if account_num == 1:
        if password != account1_password:
            print('Incorrect password.')
            return None
        return account1_balance
def deposit(account_num: int, usr_deposit: int, password: str):
    global account0_balance, account0_password
    global account1_balance, account1_password
    if account_num == 0:
        if usr_deposit < 0:
            print('You can\'t deposit a negative amount')
            return None

        if password != account0_password:
            print('Incorrect password.')
            return None

        account0_balance += usr_deposit
        return account0_balance

    if account_num == 1:
        if usr_deposit < 0:
            print('You can\'t deposit a negative amount')
            return None

        if password != account1_password:
            print('Incorrect password.')
            return None

        account1_balance += usr_deposit
        return account1_balance

def withdrawal(account_num: int, usr_withdrawal: int, password: str):
    global account0_balance, account0_password
    global account1_balance, account1_password
    if account_num == 0:
        if usr_withdrawal < 0:
            print('You can\'t withdraw negative amount.')
            return None

        if password != account0_password:
            print('Incorrect password.')
            return None

        if usr_withdrawal > account0_balance:
            print('You can\'t withdraw more than you have in your account')
            return None

        account0_balance -= usr_withdrawal
        return account0_balance

    if account_num == 1:
        if usr_withdrawal < 0:
            print('You can\'t withdraw negative amount.')
            return None

        if password != account1_password:
            print('Incorrect password.')
            return None

        if usr_withdrawal > account1_balance:
            print('You can\'t withdraw more than you have in your account')
            return None

        account1_balance -= usr_withdrawal
        return account1_balance
def show(account_num: int):
    global account0_name, account0_balance
    global account1_name, account1_balance
    if account_num == 0:
        print('Show: ')
        print(f'    Name: {account0_name}')
        print(f'    Balance: {account0_balance}')
        print()

    if account_num == 1:
        print('Show: ')
        print(f'    Name: {account1_name}')
        print(f'    Balance: {account1_balance}')
        print()


account_number = 0
new_account(account_number, 'Joe', 100, 'soup')

while True:
    print()
    print(
        'Press \'b\' to get a balance.\n'
        'Press \'d\' to make a deposit.\n'
        'Press \'w\' to make a withdrawal.\n'
        'Press \'n\' to create a new account.\n'
        'Press \'s\' to show all account.\n'
        'Press \'q\' to quit.\n'
    )

    action = input('What do you want to do? ')
    action.lower()
    action = action[0]
    print()

    if action == 'b':
        print('Get balance:')
        usr_account_num = input('Please enter your account number: ')
        usr_account_num = int(usr_account_num)
        usr_password = input('Please enter the password: ')
        the_balance = get_balance(usr_account_num, usr_password)
        if the_balance is not None:
            print(f'Your balance is: {the_balance}')

    elif action == 'd':
        print('Deposit:')
        usr_account_num = input('Please enter your account number: ')
        usr_account_num = int(usr_account_num)
        usr_deposit_amount = input('Please enter amount to deposit: ')
        usr_deposit_amount = int(usr_deposit_amount)

        usr_password = input('Please enter the password: ')

        the_deposit = deposit(usr_account_num, usr_deposit_amount, usr_password)
        if the_deposit is not None:
            print(f'Your new balance is: {the_deposit}')

    elif action == 'w':
        print('Withdrawal: ')
        usr_account_num = input('Please enter your account number: ')
        usr_account_num = int(usr_account_num)
        usr_withdraw_amount = input('Please enter the amount to withdraw: ')
        usr_withdraw_amount = int(usr_withdraw_amount)

        usr_password = input('Please enter the password: ')

        the_withdraw = withdrawal(usr_account_num, usr_withdraw_amount, usr_password)
        if the_withdraw is not None:
            print(f'Your new balance is: {the_withdraw}')

    elif action == 'n':
        print('New account')
        usr_name = input('Please enter your name. ')
        usr_starting_amt = input('How much money to have to start you account with? ')
        usr_starting_amt = int(usr_starting_amt)
        usr_password = input('What password would you like to use for this account? ')
        account_number += 1
        new_account(account_number, usr_name, usr_starting_amt, usr_password)
        print(f'Your account number is {account_number}')

    elif action == 's':
        usr_account_num = input('Please enter your account number: ')
        usr_account_num = int(usr_account_num)
        show(usr_account_num)

    elif action == 'q':
        break
