def account(initial_balance):
    balance = initial_balance

    def withdraw(amount):
        if dispatch['balance'] > amount:
            dispatch['balance'] = dispatch['balance'] - amount
            return dispatch['balance']
        else:
            return 'Insufficient Funds'

    def deposit(amount):
        dispatch['balance'] = dispatch['balance'] + amount
        return dispatch['balance']

    dispatch = {
        'withdraw': withdraw,
        'deposit': deposit,
        'balance': balance
    }
    return dispatch


def withdraw(account, amount):
    return account['withdraw'](amount)


def deposit(account, amount):
    return account['deposit'](amount)


def check_balance(account):
    return account['balance']


a = account(20)
print(deposit(a, 5))
print(withdraw(a, 17))
print(check_balance(a))
