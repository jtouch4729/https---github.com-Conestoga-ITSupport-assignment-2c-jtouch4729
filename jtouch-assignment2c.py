# Header Comment
# Name:                 assignment2c.py
# Author:               Johnny Touch
# Date Created:         July 28, 2025
# Date Last Modified:   , 2025

# Purpose:

# Contant Variables
student_discount = 0.1
hst_tax = 0.13
delivery_charge = 5

# Customer Information Dictionary
customer_info = {
    "first_name": "",
    "last_name": "",
    "address": "",
    "city": "",
    "province": "",
    "postal_code": "",
    "delivery_instructions": "",
    "phone_number": "",
    "delivery": False,
}

# Order Information Dictionary
order_info = {
    "meal_number": 0,
    "meal_name": "",
    "meal_price": 0,
    "meal_quantity": 0,
    "student": False,
    "base_total": 0,
    "discount": 0,
    "subtotal": 0,
    "tax": 0,
    "total": 0,
    "delivery_fee": 0,
    "tip_rate": 0,
    "tip_amount": 0,
}

# Order Tip Dictionary
tip_options = {1: 0.10, 2: 0.15, 3: 0.20}

# Food Menu Dictionary
food_menu = {
    1: {"name": "Chai Tea", "price": 1.99},
    2: {"name": "Mango Lassi", "price": 3.99},
    3: {"name": "Samosa Chaat", "price": 5.99},
    4: {"name": "Baingan Bharta", "price": 9.99},
    5: {"name": "Gobi Matar Masala", "price": 11.99},
    6: {"name": "Paneer Tikka Masala", "price": 13.99},
}


# Input Validation Function
def input_validation(user_input):

    while True:
        value = input(user_input).strip()
        if value:
            return value
        else:
            print("\nPlease provide the required information.")


# Postal Code Input Validation Function
def postal_validation(user_input):
    """Prompts users until they enter a non-empty value"""
    while True:
        value = input(user_input).strip()
        if len(value) == 7:
            return value
        else:
            print("\nPlease provide a postal code that is 7 characters long.")


# Welcome Message Function
def display_welcome_message():
    """Shows a welcome message at the start of the program"""
    print("Welcome to Arnold's Amazing Eats! I'll help process your order.\n")


# Customer Information Function
def get_customer_info():
    """Prompt user for their information and validate their input"""
    print("Let's get started, please provide the following information!")
    customer_info["first_name"] = input_validation("\nFirst name: ")
    customer_info["last_name"] = input_validation("\nLast name: ")
    customer_info["phone_number"] = input_validation("\nPhone number: ")

    while True:
        delivery_choice = input("\nDo you need a delivery? Please enter 'y' or 'n': ")
        if delivery_choice.lower() == "y":
            customer_info["delivery"] = True
            customer_info["address"] = input_validation(
                "\nAddress (including street number, street name, and house or unit number): "
            )
            customer_info["city"] = input_validation("\nCity: ")
            customer_info["province"] = input_validation("\nProvince: ")
            customer_info["postal_code"] = postal_validation("\nPostal code: ")
            customer_info["delivery_instructions"] = input(
                "\nSpecial delivery instructions: "
            )
            break
        elif delivery_choice.lower() == "n":
            customer_info["delivery"] = False
            break
        else:
            print("Please enter 'y' or 'n'")


# Meal Order Function
def get_meal_order():
    """Displays the food menu and prompts user to enter their choice"""
    print("\nArnold's Menu")
    for number, item in food_menu.items():
        print(f"{number}. {item['name']} - ${item['price']:.2f}")
    order_info["meal_number"] = int(
        input(
            "\nWhat would you like to order from the menu today? (Enter a number from the menu): "
        )
    )
    selected_meal = food_menu[order_info["meal_number"]]
    order_info["meal_name"] = selected_meal["name"]
    order_info["meal_price"] = selected_meal["price"]
    order_info["meal_quantity"] = int(input("\nHow many would you like to order? "))


# Confirm Meal Order Function
def confirm_meal_order():
    """Prompts user to confirm their meal choice and quantity"""
    while True:
        meal_confirmation = input(
            f"\nYou would like to order {order_info["meal_quantity"]} x {order_info["meal_name"]}, is this correct? (Enter y or n): "
        )
        if meal_confirmation.lower() == "y":
            return True
        if meal_confirmation.lower() == "n":
            return False
        else:
            print("Please enter 'y' or 'n'")


# Student Status Function
def get_student_status():
    """Confirms if user is a student or not"""
    while True:
        student_confirmation = input(f"\nAre you a student? (Enter y or n): ")
        if student_confirmation.lower() == "y":
            order_info["student"] = True
            break
        elif student_confirmation.lower() == "n":
            order_info["student"] = False
            break
        else:
            print("Please enter 'y' or 'n'")


# Tip Function
def get_tip_choice():
    """Displays the tip options and prompts user to make a choice"""
    print("\nHow much would you like to tip?")
    for key, rate in tip_options.items():
        print(f"{key}. {int(rate * 100)}%")
    tip_choice = int(input("\nEnter a number from the tip options: "))
    order_info["tip_rate"] = tip_options[tip_choice]


# Calculations Function
def calculate_totals():
    """Calculates the total cost that the user is required to pay"""
    # Base Total and Discount
    order_info["base_total"] = order_info["meal_quantity"] * order_info["meal_price"]
    if order_info["student"]:
        order_info["discount"] = order_info["base_total"] * student_discount
        order_info["subtotal"] = order_info["base_total"] - order_info["discount"]
    else:
        order_info["discount"] = 0
        order_info["subtotal"] = order_info["base_total"]

    # Delivery Fee
    if customer_info["delivery"]:
        if order_info["subtotal"] >= 30:
            order_info["delivery_fee"] = 0
        else:
            order_info["delivery_fee"] = delivery_charge
    else:
        order_info["delivery_fee"] = 0

    # Tip
    if customer_info["delivery"]:
        order_info["tip_amount"] = order_info["subtotal"] * order_info["tip_rate"]
    else:
        order_info["tip_amount"] = 0

    # Tax
    order_info["tax"] = order_info["subtotal"] * hst_tax

    # Total
    order_info["total"] = (
        order_info["subtotal"]
        + order_info["tax"]
        + order_info["delivery_fee"]
        + order_info["tip_amount"]
    )


# Order Receipt Function
def print_receipt():
    """Print a receipt summarizing the order"""
    print("")
    print(f"{'Receipt':-^70}")
    print("")
    print("")

    # Print Customer Information
    print(customer_info["first_name"], customer_info["last_name"])
    if customer_info["delivery"]:
        print(customer_info["address"])
        print(
            customer_info["city"],
            customer_info["province"],
            customer_info["postal_code"],
        )
        print(customer_info["delivery_instructions"])
    else:
        # Print Phone Number
        print(customer_info["phone_number"])

    # Print Order Headers
    print("")
    print(
        f"{"Order":<20} {"":4} {"Item Amt":8} {"":8} {"Item Price":>10} {"":6} {"Total":>8}"
    )
    print(f"{"":-<20} {"":4} {"":->8} {"":8} {"":->10} {"":6} {"":->8}")

    # Print Order Details
    print(
        f"{order_info["meal_name"]:<20} {"":4} {order_info["meal_quantity"]:8d} {"":8} {f"${order_info["meal_price"]:.2f}":>10} {"":6} {f"${order_info["base_total"]:.2f}":>8}"
    )
    print("")

    # Print Student Discount
    if order_info["student"]:
        print(
            f"{"10% student savings":<20} {"":40} {f"-${order_info["discount"]:.2f}":>8}"
        )

    # Print Subtotal
    print(f"{"Sub Total":>54} {"":6} {f"${order_info["subtotal"]:.2f}":>8}")

    # Print Delivery
    if customer_info["delivery"]:

        # Print Delivery Waived
        if order_info["delivery_fee"] == 0:
            print(
                f"{"Delivery (Waived)":<20} {"":40} {f"${order_info["delivery_fee"]:.2f}":>8}"
            )
        else:

            #  Print Delivery Fee
            print(f"{"Delivery":<20} {"":40} {f"${order_info["delivery_fee"]:.2f}":>8}")

        # Print Tip Amount
        print(
            f"{f'Tips ({int(order_info['tip_rate'] * 100)}%)':>54} {'':6} {f'${order_info['tip_amount']:.2f}':>8}"
        )

    # Print Tax and Total
    print(f"{"Tax (13%)":>54} {"":6} {f"${order_info["tax"]:.2f}":>8}")
    print(f"{"":>61} {"":->8}")
    print("")
    print(f"{"TOTAL":>54} {"":6} {f"${order_info["total"]:.2f}":>8}")


# Logical Flow

# Welcome Message Function Call
display_welcome_message()

# Customer Information Function Call
get_customer_info()

# Meal Order Function Call and Confirm Meal Order Function Call
while True:
    get_meal_order()
    if confirm_meal_order():
        break

# Student Status Function Call
get_student_status()

# Student Status Function Call
if customer_info["delivery"]:
    get_tip_choice()

# Calculations Function Call
calculate_totals()

# Order Receipt Function Call
print_receipt()
