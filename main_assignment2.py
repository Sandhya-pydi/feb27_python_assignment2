class Supermarket:
    def __init__(self):
        self.inventory = {}
        self.gst_rate = 0.18  # Default GST rate is 18%
        self.cart = []
    
    # Add a new product to the inventory
    def add_product(self, product_name, price, stock):
        self.inventory[product_name] = {'price': price, 'stock': stock}
        print(f"Product {product_name} added successfully.")
    
    # Update the stock of an existing product
    def update_stock(self, product_name, stock):
        if product_name in self.inventory:
            self.inventory[product_name]['stock'] += stock
            print(f"Stock for {product_name} updated successfully.")
        else:
            print(f"Product {product_name} not found.")
    
    # Display the inventory
    def display_inventory(self):
        print("\n--- Supermarket Inventory ---")
        if not self.inventory:
            print("Inventory is empty.")
        for product, details in self.inventory.items():
            print(f"{product} - Price: {details['price']}, Stock: {details['stock']}")
    
    # Add items to the cart
    def add_to_cart(self, product_name, quantity):
        if product_name in self.inventory:
            if self.inventory[product_name]['stock'] >= quantity:
                self.cart.append({'product_name': product_name, 'quantity': quantity})
                self.inventory[product_name]['stock'] -= quantity
                print(f"{quantity} {product_name}(s) added to cart.")
            else:
                print(f"Not enough stock for {product_name}. Only {self.inventory[product_name]['stock']} available.")
        else:
            print(f"Product {product_name} not found.")
    
    # Calculate the total price of items in the cart including GST
    def calculate_total(self):
        total = 0
        for item in self.cart:
            product_name = item['product_name']
            quantity = item['quantity']
            price = self.inventory[product_name]['price']
            total += price * quantity
        
        # Applying GST
        gst_amount = total * self.gst_rate
        total_with_gst = total + gst_amount
        
        return total, gst_amount, total_with_gst
    
    # Generate the receipt for the cart
    def generate_receipt(self):
        if not self.cart:
            print("Your cart is empty.")
            return
        
        print("\n--- Receipt ---")
        print(f"{'Product Name':<20}{'Quantity':<10}{'Price':<10}{'Total Price'}")
        print("-" * 50)
        
        total = 0
        for item in self.cart:
            product_name = item['product_name']
            quantity = item['quantity']
            price = self.inventory[product_name]['price']
            total_price = price * quantity
            total += total_price
            print(f"{product_name:<20}{quantity:<10}{price:<10}{total_price}")
        
        total, gst_amount, total_with_gst = self.calculate_total()
        
        print("-" * 50)
        print(f"{'Subtotal':<40}{total:<10}")
        print(f"{'GST (18%)':<40}{gst_amount:<10}")
        print(f"{'Total (with GST)':<40}{total_with_gst:<10}")
        print("-" * 50)

    # Clear the cart after billing
    def clear_cart(self):
        self.cart.clear()
        print("Cart cleared.")
    
    # Set a custom GST rate
    def set_gst_rate(self, gst_rate):
        if 0 <= gst_rate <= 1:
            self.gst_rate = gst_rate
            print(f"GST rate updated to {gst_rate * 100}%.")
        else:
            print("Invalid GST rate. Please enter a value between 0 and 1.")

def main():
    supermarket = Supermarket()
    
    # Sample Inventory Initialization
    supermarket.add_product("Apple", 50, 100)
    supermarket.add_product("Banana", 30, 50)
    supermarket.add_product("Orange", 60, 75)
    supermarket.add_product("Milk", 40, 200)
    supermarket.add_product("Bread", 20, 150)

    # Main menu for interaction
    while True:
        print("\n--- Supermarket Menu ---")
        print("1. Display Inventory")
        print("2. Add Product to Cart")
        print("3. Calculate Total and GST")
        print("4. Generate Receipt")
        print("5. Update Product Stock")
        print("6. Set GST Rate")
        print("7. Clear Cart")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            supermarket.display_inventory()
        
        elif choice == '2':
            product_name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            supermarket.add_to_cart(product_name, quantity)
        
        elif choice == '3':
            total, gst_amount, total_with_gst = supermarket.calculate_total()
            print(f"\nTotal: {total}")
            print(f"GST Amount: {gst_amount}")
            print(f"Total with GST: {total_with_gst}")
        
        elif choice == '4':
            supermarket.generate_receipt()
        
        elif choice == '5':
            product_name = input("Enter product name: ")
            stock = int(input("Enter stock to add: "))
            supermarket.update_stock(product_name, stock)
        
        elif choice == '6':
            gst_rate = float(input("Enter new GST rate (as decimal, e.g., 0.18 for 18%): "))
            supermarket.set_gst_rate(gst_rate)
        
        elif choice == '7':
            supermarket.clear_cart()
        
        elif choice == '8':
            print("Thank you for visiting!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
