class Coffee:

    # initialize coffee with name and price
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:

    # initialize order with empty list of coffees
    def __init__(self):
        self.items = []

    # add coffee to the order
    def add_item(self, coffee):
        self.items.append(coffee)
        print(f"Added {coffee.name} to your order")

    # calculate total price of the order
    def total(self):
        return sum(coffee.price for coffee in self.items)

    # show order summary
    def show_order(self):
        if not self.items:
            print("No items in order.")
            return

        print("\nYour Order:")

        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ₹{item.price}")

        print(f"Total: ₹{self.total()}\n")

    # handle checkout process
    def checkout(self):
        if not self.items:
            print("Your cart is Empty")
            return

        self.show_order()

        confirm = input("Proceed Checkout? (yes/no): ").strip().lower()

        if confirm == 'yes':
            print("Order Confirmed. THANK YOU!")
            self.items.clear()
        else:
            print("Checkout cancelled.")


def main():
    # Menu of available coffees
    menu = [
        Coffee("Espresso", 150),
        Coffee("Latte", 200),
        Coffee("Cappuccino", 180),
        Coffee("Americano", 120),
        Coffee("Mocha", 220),
    ]

    order = Order()

    while True:
        print("\n===== COFFEE MENU =====")
        for i, coffee in enumerate(menu, 1):
            print(f"{i}. {coffee.name} - ₹{coffee.price}")
        print("6. View Order")
        print("7. Checkout")
        print("0. Exit")
        print("========================")

        choice = input("Enter your choice: ").strip()

        if choice == '0':
            print("Goodbye!")
            break
        elif choice in ['1', '2', '3', '4', '5']:
            coffee_index = int(choice) - 1
            qty = input("How many? ").strip()
            try:
                qty = int(qty)
                for _ in range(qty):
                    order.add_item(menu[coffee_index])
            except ValueError:
                print("Invalid quantity. Adding 1.")
                order.add_item(menu[coffee_index])
        elif choice == '6':
            order.show_order()
        elif choice == '7':
            order.checkout()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
