# Initialize an empty list
items = []
# Task 1: Write a function that lets the user add items to a list.
def add_item(item_list):
    item = input("Enter an item to add: ")
    item_list.append(item)
    print("Item " + item +" added to the list.")
# Task 2: Include a function to remove items from the list.
def remove_item(item_list):
    item = input("Enter an item to remove: ")
    if item in item_list:
        item_list.remove(item)
        print("Item " + item +"removed from the list.")
    else:
        print("Item " + item + "not found in the list.")
def print_list(item_list):
# Task 3: Add a function that prints out the entire list in a formatted way.
    if item_list:
        print("Current list of items:")
        for index, item in enumerate(item_list, start=1):
            print(f'{index}. {item}')
    else:
        print("The list is currently empty.")


# Loop to keep asking the user for actions until they choose to exit INFINITELY >:)
while True:
    # Added \n to show I can use it but also to give myself some spacing
    print("\nWhat would you like to do?")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Print the list")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        add_item(items)
    elif choice == '2':
        remove_item(items)
    elif choice == '3':
        print_list(items)
    elif choice == '4':
        print("Happy Shopping!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")