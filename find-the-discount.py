# Calculate the final price after a discount.

price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

discounted_price = price * (1 - discount / 100)

print(f"The discounted price is: {discounted_price:.2f}")