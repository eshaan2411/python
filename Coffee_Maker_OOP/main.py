from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print("\n\t\tWelcome to the COFFEE-MAKER MACHINE\n")

is_on = True
coffee_maker = CoffeeMaker()
my_money = MoneyMachine()
my_menu = Menu()

while is_on:
    options = my_menu.get_items()
    choice = input(f"\nWhat do you wish to have? {options}\nChoice: ")
    
    if choice=="off":
        is_on = False
    
    elif choice.lower()=="report":
        coffee_maker.report()
        my_money.report()

    else:
        drink = my_menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if my_money.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
