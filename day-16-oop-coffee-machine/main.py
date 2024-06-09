from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    prompt = f"What would you like? ({menu.get_items()})? "
    command = input(prompt).strip().lower()
    print('')  # Blank line after user input.
    if len(command) < 1:
        continue  # Just prompt them again.
    elif 'off'.startswith(command):
        break  # End program loop.
    elif 'report'.startswith(command):
        coffee_maker.report()
        money_machine.report()
    else:
        item = menu.find_drink(command)
        if item is None:
            print("Sorry that item is not available.")
        else:
            if coffee_maker.is_resource_sufficient(item):
                if money_machine.make_payment(item.cost):
                    coffee_maker.make_coffee(item)

    print('')  # Blank line after command result.
