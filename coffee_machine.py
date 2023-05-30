# TODO: 1. Print report of all coffee machine resources
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
}


# TODO: 2. Check resources sufficient to make drink order.
def check_resources(coffee_type):
    """Checks the amount of resources for the coffee the user wants."""
    if MENU[coffee_type]['ingredients']['water'] <= resources['water']:
        if coffee_type != 'espresso' and MENU[coffee_type]['ingredients']['coffee'] <= resources['coffee']:
            if MENU[coffee_type]['ingredients']['milk'] <= resources['milk']:
                resources['water'] -= MENU[coffee_type]['ingredients']['water']
                resources['milk'] -= MENU[coffee_type]['ingredients']['milk']
                resources['coffee'] -= MENU[coffee_type]['ingredients']['coffee']
                print("There is enough resource in machine.")
                return 1
            else:
                print("Sorry there is not enough milk")

        elif coffee_type == 'espresso' and MENU[coffee_type]['ingredients']['coffee'] <= resources['coffee']:
            resources['water'] -= MENU[coffee_type]['ingredients']['water']
            resources['coffee'] -= MENU[coffee_type]['ingredients']['coffee']
            print("There is enough resource in machine.")
            return 1

        else:
            print("Sorry there is not enough coffee milk")
    else:
        print("Sorry there is not enough water")


# TODO: 3. Check money.
def check_money(coffee_type, safe):
    """" Compares the price of coffee with the money entered by the user.
        Safe -> Represents money in the safe
    """
    quarters = int(input('how many quarters?: '))
    dimes = int(input('how many dimes?: '))
    nickles = int(input('how many nickles?: '))
    pennies = int(input('how many pennies?: '))
    users_money = float(pennies * 0.01 + dimes * 0.10 + nickles * 0.05 + quarters * 0.25)
    if users_money >= MENU[coffee_type]['cost']:
        in_change = users_money - MENU[coffee_type]['cost']
        safe = safe + MENU[coffee_type]['cost']
        print(f"Here is ${in_change} in change.")
        print(f"Here is your {coffee_type} ☕ Enjoy!")
        return safe
    else:
        resources['water'] += MENU[coffee_type]['ingredients']['water']
        resources['coffee'] += MENU[coffee_type]['ingredients']['coffee']

        if coffee_type != 'espresso':
            resources['milk'] += MENU[coffee_type]['ingredients']['milk']

        print("Sorry that's not enough money. Money refunded.")

        return safe


# TODO: 4. Other Operations.
machine_off = False
money = 0
while not machine_off:
    selection = input("What would you like? (espresso/latte/cappuccino): ")

    if selection == 'off':
        machine_off = True

    elif selection == 'report':
        for i in resources:
            print(f"{i} : {resources[i]}")
        print(f"Money : ${money}")

    elif selection == 'espresso' or selection == 'latte' or selection == 'cappuccino':
        if check_resources(selection) == 1:
            print('Please insert coins.')
            money = check_money(selection, money)

        else:
            machine_off = True

    else:
        print('Invalid Input')
        machine_off = True
