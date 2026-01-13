import sys
import os

# Add project root to path so we can import the module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from learning_coffee_machine import (
    MENU,
    check_resources,
    process_coins,
    check_payment,
    make_coffee,
    get_report,
)


class TestMenu:
    def test_menu_has_espresso(self):
        """Menu should have espresso"""
        assert "espresso" in MENU

    def test_menu_has_latte(self):
        """Menu should have latte"""
        assert "latte" in MENU

    def test_menu_has_cappuccino(self):
        """Menu should have cappuccino"""
        assert "cappuccino" in MENU

    def test_espresso_ingredients(self):
        """Espresso should have correct ingredients"""
        assert MENU["espresso"]["ingredients"]["water"] == 50
        assert MENU["espresso"]["ingredients"]["coffee"] == 18
        assert "milk" not in MENU["espresso"]["ingredients"]

    def test_espresso_cost(self):
        """Espresso should cost $1.50"""
        assert MENU["espresso"]["cost"] == 1.5

    def test_latte_ingredients(self):
        """Latte should have correct ingredients"""
        assert MENU["latte"]["ingredients"]["water"] == 200
        assert MENU["latte"]["ingredients"]["coffee"] == 24
        assert MENU["latte"]["ingredients"]["milk"] == 150

    def test_latte_cost(self):
        """Latte should cost $2.50"""
        assert MENU["latte"]["cost"] == 2.5

    def test_cappuccino_ingredients(self):
        """Cappuccino should have correct ingredients"""
        assert MENU["cappuccino"]["ingredients"]["water"] == 250
        assert MENU["cappuccino"]["ingredients"]["coffee"] == 24
        assert MENU["cappuccino"]["ingredients"]["milk"] == 100

    def test_cappuccino_cost(self):
        """Cappuccino should cost $3.00"""
        assert MENU["cappuccino"]["cost"] == 3.0


class TestCheckResources:
    def test_check_resources_sufficient(self):
        """Should return True when resources are sufficient"""
        resources = {"water": 300, "milk": 200, "coffee": 100}
        result, message = check_resources("espresso", resources)
        assert result is True

    def test_check_resources_insufficient_water(self):
        """Should return False when water is insufficient"""
        resources = {"water": 10, "milk": 200, "coffee": 100}
        result, message = check_resources("espresso", resources)
        assert result is False
        assert "water" in message.lower()

    def test_check_resources_insufficient_coffee(self):
        """Should return False when coffee is insufficient"""
        resources = {"water": 300, "milk": 200, "coffee": 5}
        result, message = check_resources("latte", resources)
        assert result is False
        assert "coffee" in message.lower()

    def test_check_resources_insufficient_milk(self):
        """Should return False when milk is insufficient"""
        resources = {"water": 300, "milk": 10, "coffee": 100}
        result, message = check_resources("latte", resources)
        assert result is False
        assert "milk" in message.lower()


class TestProcessCoins:
    def test_process_coins_calculates_total(self):
        """Should calculate total from coin counts"""
        total = process_coins(quarters=4, dimes=0, nickels=0, pennies=0)
        assert total == 1.0

    def test_process_coins_mixed_coins(self):
        """Should calculate total from mixed coins"""
        total = process_coins(quarters=2, dimes=3, nickels=1, pennies=5)
        # 0.50 + 0.30 + 0.05 + 0.05 = 0.90
        assert total == 0.90

    def test_process_coins_zero(self):
        """Should return 0 when no coins inserted"""
        total = process_coins(quarters=0, dimes=0, nickels=0, pennies=0)
        assert total == 0.0


class TestCheckPayment:
    def test_check_payment_exact(self):
        """Should return True with 0 change for exact payment"""
        success, change = check_payment(1.5, 1.5)
        assert success is True
        assert change == 0.0

    def test_check_payment_overpaid(self):
        """Should return True with correct change for overpayment"""
        success, change = check_payment(2.0, 1.5)
        assert success is True
        assert change == 0.5

    def test_check_payment_underpaid(self):
        """Should return False when payment is insufficient"""
        success, change = check_payment(1.0, 1.5)
        assert success is False


class TestMakeCoffee:
    def test_make_coffee_deducts_resources(self):
        """Should deduct correct ingredients from resources"""
        resources = {"water": 300, "milk": 200, "coffee": 100}
        make_coffee("espresso", resources)
        assert resources["water"] == 250  # 300 - 50
        assert resources["coffee"] == 82  # 100 - 18
        assert resources["milk"] == 200  # unchanged for espresso

    def test_make_coffee_deducts_latte_resources(self):
        """Should deduct correct ingredients for latte"""
        resources = {"water": 300, "milk": 200, "coffee": 100}
        make_coffee("latte", resources)
        assert resources["water"] == 100  # 300 - 200
        assert resources["milk"] == 50  # 200 - 150
        assert resources["coffee"] == 76  # 100 - 24


class TestGetReport:
    def test_get_report_format(self):
        """Should return formatted report string"""
        resources = {"water": 300, "milk": 200, "coffee": 100}
        money = 5.0
        report = get_report(resources, money)
        assert "Water: 300ml" in report
        assert "Milk: 200ml" in report
        assert "Coffee: 100g" in report
        assert "Money: $5.00" in report
