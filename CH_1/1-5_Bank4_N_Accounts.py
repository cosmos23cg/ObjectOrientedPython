# Non-OOP
# Bank version #4
# Multiple accounts: use list

account_name_ls = []
account_balance_ls = []
account_password_ls = []

def new_account(name: str, balance: int, password: str):
    global account_name_ls, account_balance_ls, account_password_ls
    account_name_ls.append(name)
    account_balance_ls.append(balance)
    account_password_ls.append(password)

def get_balance(acc_num: int, password:str):
    global account_name_ls, account_balance_ls, account_password_ls
    if password != account_password_ls[acc_num]:
        print('Incorrect password.')
        return None
    return account_balance_ls[acc_num]

def deposit(acc_num: int, usr_deposit: int, password: str):
    global account_name_ls, account_balance_ls, account_password_ls
    if usr_deposit < 0:
        print('You can\'t deposit a negative amount')
        return None

    if password != account_password_ls[acc_num]:
        print('Incorrect password.')
        return None

    account_balance_ls[acc_num] += usr_deposit
    return account_balance_ls[acc_num]

def withdrawal(acc_num: int, usr_withdrawal: int, password: str):
    global account_name_ls, account_balance_ls, account_password_ls
    if usr_withdrawal < 0:
        print('You can\'t withdraw negative amount.')
        return None

    if password != account_password_ls[acc_num]:
        print('Incorrect password.')
        return None

    if usr_withdrawal > account_balance_ls[acc_num]:
        print('You can\'t withdraw more than you have in your account')
        return None

    account_balance_ls[acc_num] -= usr_withdrawal
    return account_balance_ls[acc_num]

def show(acc_num: int):
    global account_name_ls, account_balance_ls, account_password_ls
    print('Show: ')
    print(f'    Name: {account_name_ls[acc_num]}')
    print(f'    Balance: {account_balance_ls[acc_num]}')
    print()


print(f'Joe\'s account is account num {len(account_name_ls)}')
new_account('Joe', 1000, 'joe')

print(f'John\'s account is account number {len(account_name_ls)}')
new_account('John', 20, 'john')

while True:
    print()
    print(
        'Press \'b\' to get a balance.\n'
        'Press \'d\' to make a deposit.\n'
        'Press \'w\' to make a withdrawal.\n'
        'Press \'n\' to create a new account \n'
        'Press \'s\' to show the account.\n'
        'Press \'q\' to quit.\n'
    )

    action = input('What do you want to do? ')
    action.lower()
    action = action[0]
    print()

    if action == 'b':
        print('Get balance:')
        usr_acc = input('Please enter your account number: ')
        usr_acc = int(usr_acc)
        usr_password = input('Please enter the password: ')
        the_balance = get_balance(usr_acc, usr_password)
        if the_balance is not None:
            print(f'Your balance is: {the_balance}')

    elif action == 'd':
        print('Deposit:')
        usr_deposit_amount = input('Please enter amount to deposit: ')
        usr_deposit_amount = int(usr_deposit_amount)
        usr_acc = input('Please enter your account number: ')
        usr_acc = int(usr_acc)
        usr_password = input('Please enter the password: ')
        the_deposit = deposit(usr_acc, usr_deposit_amount, usr_password)
        if the_deposit is not None:
            print(f'Your new balance is: {the_deposit}')

    elif action == 'w':
        print('Withdrawal: ')
        usr_withdraw_amount = input('Please enter the amount to withdraw: ')
        usr_withdraw_amount = int(usr_withdraw_amount)
        usr_acc = input('Please enter your account number: ')
        usr_acc = int(usr_acc)
        usr_password = input('Please enter the password: ')
        the_withdraw = withdrawal(usr_acc, usr_withdraw_amount, usr_password)
        if the_withdraw is not None:
            print(f'Your new balance is: {the_withdraw}')

    elif action == 'n':
        print("New account: ")
        usr_name = input('Please enter your name: ')
        usr_starting_amt = input('How much money to have to start you account with? ')
        usr_starting_amt = int(usr_starting_amt)
        usr_password = input('What password would you like to use for this account? ')
        print(f'Account has been created. Your account number is {len(account_name_ls)}')
        new_account(usr_name, usr_starting_amt, usr_password)

    elif action == 's':
        usr_acc = input('Please enter your account number: ')
        usr_acc = int(usr_acc)
        show(usr_acc)

    elif action == 'q':
        break
