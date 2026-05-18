cart = []

while True:
    print("\n1. Add Product")
    print("2. Remove Product")
    print("3. Display Cart")
    print("4. Total Items")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        product = input("Enter product name: ")
        cart.append(product)
        print("Product added")

    elif choice == "2":
        product = input("Enter product name to remove: ")

        if product in cart:
            cart.remove(product)
            print("Product removed")
        else:
            print("Product not found")

    elif choice == "3":
        print("\nProducts in Cart:")

        for item in cart:
            print(item)

    elif choice == "4":
        print("Total items:", len(cart))

    elif choice == "5":
        break

    else:
        print("Invalid choice")