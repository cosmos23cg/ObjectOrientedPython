# Non-OOP
# Bank version #2
# Single account

account_name = ""
account_balance = 0
account_password = ''

def new_account(name: str, balance: int, password: str):
    global account_name, account_balance, account_password
    account_name = name
    account_balance = balance
    account_password = password

def get_balance(password: str):
    global account_name, account_balance, account_password
    if password != account_password:
        print('Incorrect password.')
        return None
    return account_balance

def deposit(usr_deposit: int, password: str):
    global account_name, account_balance, account_password
    if usr_deposit < 0:
        print('You can\'t deposit a negative amount')
        return None

    if password != account_password:
        print('Incorrect password.')
        return None

    account_balance += usr_deposit
    return account_balance

def withdrawal(usr_withdrawal: int, password: str):
    global account_name, account_balance, account_password
    if usr_withdrawal < 0:
        print('You can\'t withdraw negative amount.')
        return None

    if password != account_password:
        print('Incorrect password.')
        return None

    if usr_withdrawal > account_balance:
        print('You can\'t withdraw more than you have in your account')
        return None

    account_balance -= usr_withdrawal
    return account_balance

def show():
    global account_name, account_balance, account_password
    print('Show: ')
    print(f'    Name: {account_name}')
    print(f'    Balance: {account_balance}')
    print()


new_account('Joe', 100, 'soup')

while True:
    print()
    print(
        'Press \'b\' to get a balance.\n'
        'Press \'d\' to make a deposit.\n'
        'Press \'w\' to make a withdrawal.\n'
        'Press \'s\' to show the account.\n'
        'Press \'q\' to quit.\n'
    )

    action = input('What do you want to do? ')
    action.lower()
    action = action[0]
    print()

    if action == 'b':
        print('Get balance:')
        usr_password = input('Please enter the password: ')
        the_balance = get_balance(usr_password)
        if the_balance is not None:
            print(f'Your balance is: {the_balance}')

    elif action == 'd':
        print('Deposit:')
        usr_deposit_amount = input('Please enter amount to deposit: ')
        usr_deposit_amount = int(usr_deposit_amount)

        usr_password = input('Please enter the password: ')

        the_deposit = deposit(usr_deposit_amount, usr_password)
        if the_deposit is not None:
            print(f'Your new balance is: {the_deposit}')

    elif action == 'w':
        print('Withdrawal: ')
        usr_withdraw_amount = input('Please enter the amount to withdraw: ')
        usr_withdraw_amount = int(usr_withdraw_amount)

        usr_password = input('Please enter the password: ')

        the_withdraw = withdrawal(usr_withdraw_amount, usr_password)
        if the_withdraw is not None:
            print(f'Your new balance is: {the_withdraw}')

    elif action == 's':
        show()

    elif action == 'q':
        break
