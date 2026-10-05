shopping_list = []

while True:
    item = input("Enter an item: ")

    if item.lower() == "done":
        break

    shopping_list.append(item)

print("\nYour shopping list:")

for item in shopping_list:
    print(item)