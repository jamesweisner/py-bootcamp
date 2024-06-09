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

money = 0.0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Prompt user to insert coins. Returns amount inserted.
def insert_coins():
    balance = 0
    coins = {
        'quarters': 0.25,
        'dimes': 0.10,
        'nickels': 0.05,
        'pennies': 0.01,
    }
    print('Please insert coins.\n')
    for name, value in coins.items():
        try:
            count = int(input(f'  How many {name}? '))
            assert count > 0
            balance += count * value
        except ValueError:
            print("    That's a weird number... Looks like zero to me!")
        except AssertionError:
            print("    Oh, so you don't have any {name}. Too bad.")
    print('')
    return balance


# Record the sale of an item. Modify money & resources.
def log_sale(item):
    global money, resources
    money += MENU[item]['cost']
    for name, amount in MENU[item]['ingredients'].items():
        resources[name] -= amount


# Attempt to purchase a coffee item.
def purchase(item):
    for name, amount in MENU[item]['ingredients'].items():
        if resources[name] < amount:
            print(f"Sorry, there is not enough {name}.")
            return
    balance = insert_coins()
    balance -= MENU[item]['cost']
    if balance < 0:
        print("Sorry that's not enough money. Money refunded.")
        return
    print(f'Here is your {item}. Enjoy!')
    if balance > 0:
        print(f'Here is ${balance:.2f} in change.')
    log_sale(item)


# Main program loop.
prompt = f"What would you like? ({'/'.join(MENU.keys())}): "
while True:
    command = input(prompt).strip().lower()
    print('')  # Empty line after user input.
    if len(command) < 1:
        print('Please type a command.')
    elif 'off'.startswith(command):
        break  # End program loop.
    elif 'report'.startswith(command):
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money:.2f}")
    else:
        found = False
        for item in MENU.keys():
            if item.startswith(command):
                purchase(item)
                found = True
                break
        if not found:
            print('Unrecognized command.')
    print('')  # Empty line after command result.

print('Bye!\n')
