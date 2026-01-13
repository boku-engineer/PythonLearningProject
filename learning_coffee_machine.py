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
    },
}

INITIAL_RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(drink_name, resources):
    """Check if there are enough resources to make the drink."""
    drink = MENU[drink_name]
    for ingredient, amount in drink["ingredients"].items():
        if resources.get(ingredient, 0) < amount:
            return False, f"Sorry, there is not enough {ingredient}."
    return True, ""


def process_coins(quarters, dimes, nickels, pennies):
    """Calculate total value from inserted coins."""
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return round(total, 2)


def check_payment(payment, cost):
    """Check if payment is sufficient and calculate change."""
    if payment < cost:
        return False, 0
    change = round(payment - cost, 2)
    return True, change


def make_coffee(drink_name, resources):
    """Deduct ingredients from resources to make the drink."""
    drink = MENU[drink_name]
    for ingredient, amount in drink["ingredients"].items():
        resources[ingredient] -= amount


def get_report(resources, money):
    """Generate a report of current resources and money."""
    return (
        f"Water: {resources['water']}ml\n"
        f"Milk: {resources['milk']}ml\n"
        f"Coffee: {resources['coffee']}g\n"
        f"Money: ${money:.2f}"
    )


def main():
    """Main coffee machine loop."""
    resources = INITIAL_RESOURCES.copy()
    money = 0.0

    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == "off":
            print("Turning off the coffee machine. Goodbye!")
            break
        elif choice == "report":
            print(get_report(resources, money))
        elif choice in MENU:
            # Check resources
            has_resources, message = check_resources(choice, resources)
            if not has_resources:
                print(message)
                continue

            # Get payment
            print(f"The {choice} costs ${MENU[choice]['cost']:.2f}")
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))

            payment = process_coins(quarters, dimes, nickels, pennies)

            # Check payment
            success, change = check_payment(payment, MENU[choice]["cost"])
            if not success:
                print("Sorry, that's not enough money. Money refunded.")
                continue

            # Make coffee
            make_coffee(choice, resources)
            money += MENU[choice]["cost"]

            if change > 0:
                print(f"Here is ${change:.2f} in change.")

            print(f"Here is your {choice}. Enjoy!")
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
