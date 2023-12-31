# Non-OOP
# Bank version #1
# Single account

account_name = "Joe"
account_balance = 100
account_password = 'soup'

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
        if usr_password != account_password:
            print('Incorrect password.')
        else:
            print(f'Your balance is: {account_balance}')

    elif action == 'd':
        print('Deposit:')
        usr_deposit_amount = input('Please enter amount to deposit: ')
        usr_deposit_amount = int(usr_deposit_amount)

        usr_password = input('Please enter the password: ')

        if usr_deposit_amount < 0:
            print('You can\'t deposit a negative amount')
        elif usr_password != account_password:
            print('Incorrect password.')
        else:
            account_balance += usr_deposit_amount
            print(f'Your new balance is: {account_balance}')

    elif action == 'w':
        print('Withdrawal: ')
        usr_withdraw_amount = input('Please enter the amount to withdraw: ')
        usr_withdraw_amount = int(usr_withdraw_amount)

        usr_password = input('Please enter the password: ')

        if usr_withdraw_amount < 0:
            print('You can\'t withdraw negative amount.')
        elif usr_password != account_password:
            print('Incorrect password.')
        elif usr_withdraw_amount > account_balance:
            print('You can\'t withdraw more than you have in your account')
        else:
            account_balance -= usr_withdraw_amount
            print(f'Your new account balance is {account_balance}')

    elif action == 's':
        print('Show: ')
        print(f'    Name: {account_name}')
        print(f'    Balance: {account_balance}')
        print()

    elif action == 'q':
        break
