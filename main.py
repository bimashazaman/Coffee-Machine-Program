

# Defining the menu of the coffee machine.
from secrets import choice


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


is_on = True

while is_on:
    choice = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = Menu[choice]
        is_resource_sufficient(drink["ingredients"])
        print("Please insert coins.")


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
