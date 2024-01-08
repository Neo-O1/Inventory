# inventory_management.py

class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity

    def view_inventory(self):
        print("Current Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity} units")

    def search_item(self, item):
        if item in self.inventory:
            print(f"{item} found in the inventory. Quantity: {self.inventory[item]} units")
        else:
            print(f"{item} not found in the inventory.")

def main():
    inventory = Inventory()

    while True:
        print("\nOptions:")
        print("1. Add item to inventory")
        print("2. View current inventory")
        print("3. Search for an item")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            item = input("Enter the item name: ")
            quantity = int(input("Enter the quantity: "))
            inventory.add_item(item, quantity)

        elif choice == "2":
            inventory.view_inventory()

        elif choice == "3":
            item = input("Enter the item name to search: ")
            inventory.search_item(item)

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
