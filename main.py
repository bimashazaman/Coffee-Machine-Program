

# Defining the menu with ingredients of the coffee machine.
Menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.5,
    },

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 3.0,
    },
}

profit = 0

# Defining the resources available to the machine.
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""

    print("Please insert coins.")

   # This is asking the user to input the number of quarters, dimes, nickles, and pennies.
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01

    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    # This is a conditional statement that is checking if the money received is greater than or equal
    # to the cost of the drink. If it is, then it will calculate the change and print it. It will also
    # add the cost of the drink to the profit.
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    # This is a for loop that is iterating through the dictionary `order_ingredients`. It is
    # subtracting the value of the key `item` from the value of the key `item` in the dictionary
    # `resources`.
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
   # This is asking the user to input what they would like to drink. It is also converting the input
   # to lowercase.
    choice = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()
    
    # This is a conditional statement that will break the loop if the user inputs "off"
    if choice == "off":
        print("The machine is now off.")
        is_on = False
        
   # This is printing the resources and profit.
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
        
   # This is a conditional statement that is checking if the user has inputted a drink that is in the
   # menu. If it is, then it will check if the resources are sufficient. If they are, then it will ask
   # for the money. If the money is sufficient, then it will print the change and the drink.
    else:
        drink = Menu[choice]
        is_resource_sufficient(drink["ingredients"])
        payment = process_coins()
        if is_transaction_successful(payment, drink["cost"]):
            make_coffee(choice, drink["ingredients"])
            
            

            # ---------------second Approach--------------

            #     # This is a conditional statement that will break the loop if the user inputs "off"
            #     choice = input("What would you like? (expresso/latte/cappuccino): ").lower()

            #     # This is a conditional statement that will break the loop if the user inputs "off"
            #     if choice == "off":
            #         is_on = False

            #    # Printing the resources and profit.
            #     elif choice == "report":
            #         print(f"Water: {resources['water']}ml")
            #         print(f"Milk: {resources['milk']}ml")
            #         print(f"Coffee: {resources['coffee']}g")
            #         print(f"Money: ${profit}")

            #     elif choice == "expresso" or choice == "latte" or choice == "cappuccino":
            #        # Assigning the value of the key `choice` to the variable `drink`.
            #         drink = Menu[choice]
            #         print(f"You have chosen {choice}")

            #         # Checking if the resources are sufficient.
            #         is_enough_ingredients = True
            #        # This is a for loop that is iterating through the dictionary `drink["ingredients"]`.
            #         for item in drink["ingredients"]:
            #             if drink["ingredients"][item] > resources[item]:
            #                 print(f"Sorry there is not enough {item}")
            #                 is_enough_ingredients = False

            #         # If the resources are sufficient, then the program will ask for the money.
            #         if is_enough_ingredients:
            #             print("Please insert coins.")
            #            # This is asking the user to input the number of quarters, dimes, nickles, and pennies.
            #             quarters = int(input("How many quarters?: "))
            #             dimes = int(input("How many dimes?: "))
            #             nickles = int(input("How many nickles?: "))
            #             pennies = int(input("How many pennies?: "))
            #             # This is calculating the total amount of money that the user has inputted.
            #             total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

            #             # If the money is sufficient, then the program will print the change and the drink.
            #             if total >= drink["cost"]:
            #                 change = round(total - drink["cost"], 2)
            #                 print(f"Here is ${change} in change.")
            #                 print(f"Here is your {choice} ☕️. Enjoy!")
            #                 profit += drink["cost"]

            #                 # Updating the resources.
            #                 for item in drink["ingredients"]:
            #                     resources[item] -= drink["ingredients"][item]
            #             else:
            #                 print("Sorry that's not enough money. Money refunded.")
