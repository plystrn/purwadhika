from tabulate import tabulate

products = {
    "001": {"name": "Black T-Shirt", "category": "Tops", "price": 199000, "quantity": 10},
    "002": {"name": "White T-Shirt", "category": "Tops", "price": 199000, "quantity": 15},
    "003": {"name": "Black Jacket", "category": "Outer", "price": 249000, "quantity": 20},
    "004": {"name": "Red Jacket", "category": "Outer", "price": 249000, "quantity": 8},
    "005": {"name": "Slim Fit Jeans", "category": "Pants", "price": 599000, "quantity": 12},
    "006": {"name": "Ripped Jeans", "category": "Pants", "price": 549000, "quantity": 5}
    }
cart = []

# Print initial products
def print_initial_products():
    print("Initial Products in the Marketplace:")
    product_list = [[pid, details['name'], details['category'], details['price'], details['quantity']] for pid, details in products.items()]
    print(tabulate(product_list, headers=['ID', 'Name', 'Category', 'Price', 'Quantity'], tablefmt='grid'))

# Main Menu
def main_menu():
    while True:
        print("\nWelcome to the Clothing Store!")
        print("1. Seller Menu")
        print("2. Buyer Menu")  
        print("3. Exit Program")
        choice = input("Enter your choice of menu: ")
        if choice == "1":
            seller_menu()
        elif choice == "2":
            buyer_menu()
        elif choice == "3":
            print("Thank you for visiting the Clothing Store. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Seller Menu
def seller_menu():
    while True:
        print("\nSeller Dashboard")
        print("1. Input product for sale")
        print("2. Show list of products being sold")
        print("3. Edit product")
        print("4. Delete product")
        print("5. Return to main menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_product()
        elif choice == "2":
            print("\nWould you like to sort the products? (y/n)")
            while True:
                sort_choice = input().lower()
                sort_by = 'id'
                if sort_choice == 'y':
                    while True:
                        print("Sort by: 1. Name 2. Price")
                        sort_option = input()
                        if sort_option == '1':
                            sort_by = 'name'
                            break
                        elif sort_option == '2':
                            sort_by = 'price'
                            break
                        else:
                            print("Invalid choice. Please enter a number between 1 and 2.")
                    break
                elif sort_choice == 'n':
                    break
                else:
                    print("Invalid choice. Please enter correct input! (y/n)")
            show_products(sort_by)
        elif choice == "3":
            edit_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Buyer Menu
def buyer_menu():
    while True:
        print("\nBuyer Dashboard")
        print("1. Display list of products")
        print("2. Buy products (add to cart)")
        print("3. Search products by name")
        print("4. Search products by category")
        print("5. See cart details")
        print("6. Checkout")
        print("7. Return to main menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nWould you like to sort the products? (y/n)")
            while True:
                sort_choice = input().lower()
                sort_by = 'id'
                if sort_choice == 'y':
                    while True:
                        print("Sort by: 1. Name 2. Price")
                        sort_option = input()
                        if sort_option == '1':
                            sort_by = 'name'
                            break
                        elif sort_option == '2':
                            sort_by = 'price'
                            break
                        else:
                            print("Invalid choice. Please enter a number between 1 and 2.")
                    break
                elif sort_choice == 'n':
                    break
                else:
                    print("Invalid choice. Please enter correct input! (y/n)")
            show_products(sort_by)
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            search_products()
        elif choice == "4":
            search_products_by_category()
        elif choice == "5":
            show_cart()
        elif choice == "6":
            checkout()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

# Add Product in seller menu
def add_product():
    show_products()
    # Validate Product ID
    while True:
        product_id = input("Enter product ID: ").strip()
        if product_id:
            if product_id in products:
                print("Error: Product ID already exists. Please use a different ID.")
            else:
                break
        else:
            print("Product ID cannot be empty.")

    # Validate Product Name
    while True:
        product_name = input("Enter product name: ").strip()
        if product_name:
            break
        else:
            print("Product name cannot be empty.")

    # Validate Product Category
    while True:
        product_category = input("Enter product category: ").strip()
        if product_category:
            break
        else:
            print("Product category cannot be empty.")

    # Validate Product Price
    while True:
        product_price = input("Enter product price: ").strip()
        if product_price.replace('.', '', 1).isdigit() and float(product_price) > 0:
            product_price = float(product_price)
            break
        else:
            print("Invalid price. Please enter a positive number.")

    # Validate Product Quantity
    while True:
        product_quantity = input("Enter product quantity: ").strip()
        if product_quantity.isdigit() and int(product_quantity) > 0:
            product_quantity = int(product_quantity)
            break
        else:
            print("Invalid quantity. Please enter a positive integer.")

    # Add product to dictionary
    products[product_id] = {
        "name": product_name, 
        "category": product_category, 
        "price": product_price, 
        "quantity": product_quantity
    }
    print("Product added successfully.")


# Display the list of products
def show_products(sort_by='id'):
    if not products:
        print("No products available.")
        return
    
    # Decide the sorting key based on the input
    if sort_by == 'name':
        sort_key = lambda item: item[1]['name']
    elif sort_by == 'price':
        sort_key = lambda item: item[1]['price']
    else:  # Default sort by 'id'
        sort_key = lambda item: item[0]

    # Sorting the products based on the chosen key
    sorted_products = sorted(products.items(), key=sort_key)

    product_list = [[pid, details['name'], details['category'], details['price'], details['quantity']] for pid, details in sorted_products]
    print(tabulate(product_list, headers=['ID', 'Name', 'Category', 'Price', 'Quantity'], tablefmt='grid'))

# Edit Product in seller menu
def edit_product():
    show_products()
    while True:
        product_id = input("Enter product ID to edit: ").strip()
        if product_id in products:
            # Validate Product Name
            while True:
                new_name = input("Enter new product name: ").strip()
                if new_name:
                    break
                else:
                    print("Product name cannot be empty.")

            # Validate Product Category
            while True:
                new_category = input("Enter new product category: ").strip()
                if new_category:
                    break
                else:
                    print("Product category cannot be empty.")

            # Validate Product Price
            while True:
                new_price = input("Enter new product price: ").strip()
                if new_price.replace('.', '', 1).isdigit() and float(new_price) > 0:
                    new_price = float(new_price)
                    break
                else:
                    print("Invalid price. Please enter a positive number.")

            # Validate Product Quantity
            while True:
                new_quantity = input("Enter new quantity: ").strip()
                if new_quantity.isdigit() and int(new_quantity) > 0:
                    new_quantity = int(new_quantity)
                    break
                else:
                    print("Invalid quantity. Please enter a positive integer.")

            # Update product details
            products[product_id] = {
                "name": new_name,
                "category": new_category,
                "price": new_price,
                "quantity": new_quantity
            }
            print("Product updated successfully.")
            break
        else:
            print("Product not found.")



# Delete Product in seller menu
def delete_product():
    show_products()
    while True:
        product_id = input("Enter product ID to delete: ")
        if product_id in products:
            del products[product_id]
            print("Product deleted successfully.")
            break
        else:
            print("Product not found.")

# Add to cart in buyer menu
def add_to_cart():
    show_products()
    while True:
        product_id = input("Enter product ID to add to cart: ").strip()
        if product_id in products:
            while True:
                quantity_to_add = input("Enter quantity to add: ").strip()
                if quantity_to_add.isdigit() and int(quantity_to_add) > 0:
                    quantity_to_add = int(quantity_to_add)
                    if quantity_to_add <= products[product_id]['quantity']:
                        # Check if the product is already in the cart
                        found_in_cart = False
                        for item in cart:
                            if item['id'] == product_id:
                                item['quantity'] += quantity_to_add
                                products[product_id]['quantity'] -= quantity_to_add  
                                found_in_cart = True
                                break
                        if not found_in_cart:
                            cart.append({
                                'id': product_id,
                                'name': products[product_id]['name'],
                                'price': products[product_id]['price'],
                                'quantity': quantity_to_add
                            })
                            products[product_id]['quantity'] -= quantity_to_add  
                        print(f"Added {quantity_to_add} units of {products[product_id]['name']} to your cart.")
                        break
                    else:
                        print("Not enough stock available. Try a smaller quantity.")
                else:
                    print("Invalid quantity. Please enter a positive integer.")
            break
        else:
            print("Product not found.")


# Search products in buyer menu
def search_products():
    search_term = input("Enter product name to search: ").strip()
    found_products = []
    for product_id, details in products.items():
        if search_term.lower() in details['name'].lower():
            found_products.append([product_id, details['name'], details['category'], details['price'], details['quantity']])
    
    if found_products:
        print(tabulate(found_products, headers=['ID', 'Name', 'Category', 'Price', 'Quantity'], tablefmt='grid'))
    else:
        print("No products found.")

# Search products by category
def search_products_by_category():
    category = input("Enter category to search: ").strip()
    found_products = []
    for product_id, details in products.items():
        if category.lower() == details['category'].lower():
            found_products.append([product_id, details['name'], details['category'], details['price'], details['quantity']])
    
    if found_products:
        print(tabulate(found_products, headers=['ID', 'Name', 'Category', 'Price', 'Quantity'], tablefmt='grid'))
    else:
        print("No products found.")


# Show Cart in buyer menu
def show_cart():
    if not cart:
        print("Your cart is empty.")
        return
    
    cart_items = []
    total_cart_price = 0
    for item in cart:
        total_price = item['price'] * item['quantity']
        total_cart_price += total_price  
        cart_items.append([item['name'], item['price'], item['quantity'], total_price])

    print(tabulate(cart_items, headers=['Product', 'Unit Price', 'Quantity', 'Total Price'], tablefmt='grid'))
    print(f"Total Cart Price: {total_cart_price:.2f}")

# Checkout in buyer menu
def checkout():
    if not cart:
        print("Your cart is empty.")
        return
    
    total = sum(item['price'] * item['quantity'] for item in cart)  
    print(f"Total amount to pay: {total:.2f}")

    while True:
        cash_input = input("Enter the amount of cash you are paying: ")
        if cash_input.replace('.', '', 1).isdigit():
            cash_provided = float(cash_input)
            if cash_provided < total:
                needed = total - cash_provided
                print(f"Not enough cash. You need to add {needed:.2f} more.")
            else:
                if cash_provided > total:
                    change = cash_provided - total
                    print(f"Here's your change: {change:.2f}")
                for item in cart:  
                    products[item['id']]['quantity'] -= item['quantity']
                cart.clear()
                print("Checkout successful. Thank you for your purchase!")
                break
        else:
            print("Invalid input. Please enter a valid amount.")



if __name__ == "__main__":
    print_initial_products()
    main_menu()
