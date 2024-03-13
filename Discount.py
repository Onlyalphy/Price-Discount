def calculate_discount(price, discount_percent):
    price = 2500
    discount_percent = 20
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
#Calculating function with actual parameters
final_price = calculate_discount(2500, 20)
print(final_price)
