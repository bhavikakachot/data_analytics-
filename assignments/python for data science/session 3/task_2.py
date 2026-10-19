def total_cart_amount(prices):
    # map(float, prices) converts all strings to floats automatically
    # sum() then adds them all together
    total_bill = sum(map(float, prices))
    return total_bill

# Sample Flipkart-style cart list
flipkart_cart = ['199.99', '49', '350.75']

# Call the function
final_amount = total_cart_amount(flipkart_cart)

# Print the result
print("Flipkart Cart Total: ₹", final_amount)
