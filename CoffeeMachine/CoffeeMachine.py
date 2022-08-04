MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def process_choice(choice: str):
    if choice.lower() in MENU.keys():
        check_ingredients(choice)
    elif choice.lower() == 'report':
        print_report()
        pass
    elif choice.lower() == 'off':
        quit()
    else:
        print('Invalid drink selection')
        return


def make_drink(choice: str):
    for i, v in MENU.get(choice.lower()).get('ingredients').items():
        resources[i] = resources.get(i) - v
    print("Here is your {0}, enjoy! ☕".format(choice))
    return


def coin_input(n: int, bev_type: str) -> float:
    if bev_type == 'Q':
        val = 0.25
    elif bev_type == 'D':
        val = 0.10
    elif bev_type == 'N':
        val = 0.05
    elif bev_type == 'P':
        val = 0.01
    else:
        val = 0
    total = int(n) * val
    return total


def add_money(price: float):
    resources['money'] = resources['money']+price
    return


def process_payment(choice: str):
    price = MENU.get(choice.lower()).get('cost')

    # handle quarters and check for full payment
    val_q = coin_input(input("How many quarters?"), 'Q')
    bal = price - val_q
    if bal == 0:
        print("Thanks for exact change!")
        add_money(price)
        make_drink(choice)
        return
    elif bal < 0:
        print("Your change is ${0:.2f}".format(abs(bal)))
        add_money(price)
        make_drink(choice)
        return

    print("Balance: ${0:.2f}".format(bal))

    # handle dimes and check for full payment
    val_d = coin_input(input("How many dimes?"),'D')
    bal -= val_d
    if bal == 0:
        print("Thanks for exact change!")
        add_money(price)
        make_drink(choice)
        return
    elif bal < 0:
        print("Your change is ${0:.2f}".format(abs(bal)))
        add_money(price)
        make_drink(choice)
        return

    print("Balance: ${0:.2f}".format(bal))

    # handle nickels and check for full payment
    val_n = coin_input(input("How many nickels?"), 'N')
    bal -= val_n
    if bal == 0:
        print("Thanks for exact change!")
        add_money(price)
        make_drink(choice)
        return
    elif bal < 0:
        print("Your change is ${0:.2f}".format(abs(bal)))
        add_money(price)
        make_drink(choice)
        return

    print("Balance: ${0:.2f}".format(bal))

    # handle pennies and check for full payment
    val_p = coin_input(input("How many pennies?"), 'P')
    bal -= val_p
    if bal == 0:
        print("Thanks for exact change!")
        add_money(price)
        make_drink(choice)
        return
    elif bal < 0:
        print("Your change is ${0:.2f}".format(abs(bal)))
        add_money(price)
        make_drink(choice)
        return
    else:
        print("Insufficient funds. You have been refunded your money.")
        return


def check_ingredients(choice: str):
    for i, v in MENU.get(choice.lower()).get('ingredients').items():
        if resources.get(i) >= v:
            continue
        else:
            print("Insufficient quantity of {0} found for {1}. Please contact supplier.".format(i, choice))
            return()

    process_payment(choice)


def print_report():
    for k, v in resources.items():
        if k == 'money':
            print('{0:<15}${1:.2f}'.format(k,v))
            next
        if k == 'water' or k == 'milk':
            print('{0:<15}{1:.0f}ml'.format(k, v))
            next

        if k == 'coffee':
            print('{0:<15}{1:.0f}g'.format(k, v))
            next


def menu():
    choice = input('\nEspresso - ${0:.2f}\nLatte - ${1:.2f}\nCappuccino - ${2:.2f}\nSelect a beverage: '.format(MENU.get('espresso').get('cost'),MENU.get('latte').get('cost'),MENU.get('cappuccino').get('cost')))
    process_choice(choice)


if __name__ == "__main__":
    while True:
        menu()
