import art

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
    "money": 2.5
}

def coffee_report():
    for resource in resources:
        print(resources[resource])

def is_sufficient_resource(choice):
    for resource in MENU[choice]["ingredients"]:
        if resources[resource] < MENU[choice]["ingredients"][resource]:
            print(f"Sorry, there is not enough {resource}")
            return False
    return True

def process_coins():
    total = int(input("How many quarters?\n")) * 0.25
    total += int(input("How many nickles?\n")) * 0.10
    total += int(input("How many dimes?\n")) * 0.05
    total += int(input("How many pennies?\n")) * 0.01
    return total

def is_transaction_successful(choice):
    total = process_coins()
    if total > float(MENU[choice]["cost"]):
        change = round(total - float(MENU[choice]["cost"]), 2)
        if resources["money"] > change and change > 0:
            print(f"Successful Transaction! Your change is ${change}")
            resources["money"] -= change
            resources["money"] += total
        elif resources["money"] < change and change > 0:
            print("Successful Transaction! Insufficient Change! No Change given!")
            resources["money"] += total
        else:
            print("Successful Transaction!")
            resources["money"] += total
        return True
    else:
        return False

def make_drink(choice):
    for resource in MENU[choice]["ingredients"]:
        resources[resource] -= MENU[choice]["ingredients"][resource]
    print(f"Here is your {choice.capitalize()}, Enjoy!")

def coffee_machine():
    is_running = True
    print(art.logo)
    while is_running:
        choice = input("What would you like?\n").lower()
        # Is it a valid choice?
        if choice == "report":
            coffee_report()
        elif choice == "off":
            is_running = False
        elif choice in MENU.keys():
            print(MENU[choice]["cost"])
            if not is_sufficient_resource(choice):
                return
            else:
                if is_transaction_successful(choice):
                    make_drink(choice)
        else:
            print("Not a valid choice!")

coffee_machine()