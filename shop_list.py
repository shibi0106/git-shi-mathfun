import requests

def fetch_products():
    """Fetch 5 products from FakeStoreAPI."""
    url = "https://fakestoreapi.com/products?limit=5"
    response = requests.get(url)
    products = response.json()
    print("\nAvailable Products:")
    for i, p in enumerate(products, start=1):
        print(f"{i}. {p['title']}")
    return products

def add_item(shopping_list, item):
    """Add an item to the list."""
    shopping_list.append(item)
    print(f"'{item}' added to your shopping list.")

def remove_item(shopping_list, item):
    """Remove an item from the list."""
    if item in shopping_list:
        shopping_list.remove(item)
        print(f" '{item}' removed from your shopping list.")
    else:
        print(f"'{item}' not found in your shopping list.")

def show_list(shopping_list):
    """Show all items in the list."""
    if not shopping_list:
        print("🛒 Your shopping list is empty.")
    else:
        print("\nYour Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")


print("Welcome to Simple Shopping List App!")
shopping_list = []
products = fetch_products()

while True:
    print("\nMenu:")
    print("1. View products")
    print("2. Add ")
    print("3. Remove")
    print("4. View shopping list")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        products = fetch_products()

    elif choice == "2":
        try:
            num = int(input("Enter product number to add: ")) - 1
            if 0 <= num < len(products):
                add_item(shopping_list, products[num]['title'])
            else:
                print("Invalid product number.")
        except ValueError:
            print("Please enter a number.")

    elif choice == "3":
        show_list(shopping_list)
        try:
            num = int(input("Enter item number to remove: ")) - 1
            if 0 <= num < len(shopping_list):
                removed = shopping_list.pop(num)
                print(f"'{removed}' removed from your shopping list.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        show_list(shopping_list)

    elif choice == "5":
        print("See you next time!")
        break

    else:
        print("Please choose between 1 and 5.")
