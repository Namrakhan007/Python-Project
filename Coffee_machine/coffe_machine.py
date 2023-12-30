MENU = {
    "espresso": {
        "ingredients": {
            "water": 50  ,
            "coffee": 18 ,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200 ,
            "milk": 150 ,
            "coffee": 24 ,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250 ,
            "milk": 100 ,
            "coffee": 24 ,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


# Check resources sufficient
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        is_enough = True
        if order_ingredients[item] >= resources[item]:
            is_enough = False
            print(f"SORRY!The resources aren't enough for your ordered {choice}")
        return is_enough


# Process coins
def coins():
    print("Insert the coins...")
    total = int(input("quarters: $")) * 0.25
    total += int(input("dimes: $")) * 0.10
    total += int(input("nickles: $")) * 0.5
    total += int(input("pennies: $")) * 0.1
    return total


#  Check transaction successful?
def is_transaction(money_received, amount):
    if money_received >= amount:
        changes = (round(money_received - amount, 2))
        print(f"THANK YOU! Here's your change {changes}")
        global profit
        profit += money_received
        return True
    else:
        print("SORRY! that's not enough money. Money refunded")
        return False


# Make coffee
def make_coffee(order, order_ingredients):
    """deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your {order}☕️  Enjoy! 😄")
    print(resources)


# What would you like? (espresso/latte/cappuccino)
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino)☕️ .....")
    #  Turn off the Coffee Machine by entering 'off' to the prompt.
    if choice == "off":
        is_on = False
    #  Print report......
    elif choice == "report":
        print(f"water : {resources['water']}ml")
        print(f"milk : {resources['milk']}ml")
        print(f"coffee : {resources['coffee']}ml")
        print(f"money : {profit}")
    else:
        drink = MENU[choice]
        print(drink)

        # Calling all the functions.
        if is_resource_sufficient(drink['ingredients']):
            payment = coins()
            if is_transaction(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
