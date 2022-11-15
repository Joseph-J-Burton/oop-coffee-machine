from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

running = True
while running:
    # TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino): "
    # Improvement idea: request = input("Hello, what would you like? (espresso $1.50/latte $2.50/cappuccino $3):")
    # or another way of indicating cost of each option
    options = menu.get_items()
    choice = input(f"What would you like? ({options}), 'off' to exit: ")

    # TODO: 2. Turn off the Coffee Machine by entering "off" to the prompt.
    # What would you like? # off ends the loop
    # need to indicate to the user that "off" will exit
    # put code in a loop
    if choice == "off":
        running = False
        break
    # TODO: 3. Print a report of all coffee machine resources
    # report shows the water, milk, coffee, and money values
    # included in CoffeeMaker class
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    # TODO: 4. Check resources sufficient?
    # when a resource is out the message is: "Sorry there is not enough ____."
    # then cycles back to beginning prompt.
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):

            # TODO: 5. Process coins and give change if needed
            # May need to indicate total to user so they know how many coins to enter, "Please insert coins."
            if money_machine.make_payment(drink.cost):
                # here is $0.03 in change.
                # TODO: 6. Check transaction successful?
                # TODO: 7. Make coffee, tell user "Here is your ___. Enjoy!"
                # Here is your latte. Enjoy!
                coffee_maker.make_coffee(drink)
