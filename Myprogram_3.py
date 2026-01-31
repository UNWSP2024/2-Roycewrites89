#Royce Daniel. 1/30/2026 "Store clerk"
eviltax = 0.07
subtotal = 0.0
for i in range(1, 6):
    price = float(input(f"Enter the price of item {i}: "))
    subtotal += price
sales_tax = subtotal * eviltax
total = subtotal + sales_tax
print("\nReceipt")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales Tax (7%): ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")