# This file includes our main functions of the chatbot.

from menu import get_menu

class RestaurantChatbot:
    def __init__(self):
        self.menu = get_menu()
        self.order = {}

    def display_menu(self):
        print("Menu:")
        for dish, price in self.menu.items():
            print(f"{dish}: ${price:.2f}")
        print("\n")

    def take_order(self):
        while True:
            dish = input("Enter the name of the dish you want to order (or type 'done' to finish): ")
            if dish.lower() == 'done':
                break
            if dish in self.menu:
                quantity = int(input(f"How many of {dish} would you like? "))
                if dish in self.order:
                    self.order[dish] += quantity
                else:
                    self.order[dish] = quantity
            else:
                print("Sorry, that dish is not on the menu. Please choose a dish from the menu.")

    def calculate_total(self):
        total = 0
        for dish, quantity in self.order.items():
            total += self.menu[dish] * quantity
        return total

    def process_payment(self, total):
        payment = float(input("Enter the amount you are paying: "))
        if payment < total:
            print("Insufficient payment. Please provide at least the total amount.")
        else:
            change = payment - total
            print(f"Thank you for your payment. Your change is: ${change:.2f}")

    def start(self):
        self.display_menu()
        print("Welcome to our restaurant! Please place your order.\n")
        self.take_order()

        if not self.order:
            print("You have not ordered anything.")
            return

        total = self.calculate_total()
        print(f"\nYour total is: ${total:.2f}")
        self.process_payment(total)

def start_chatbot():
    bot = RestaurantChatbot()
    bot.start()

# Uncomment the line below if you want the chatbot to start automatically when this script is run directly
# start_chatbot()
