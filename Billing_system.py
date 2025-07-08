try:
    customer_name : input("Enter your name: ")
    product_qnty = int(input("Enter the quantity of products: "))
    price = float(input("Enter total amount: "))

    if product_qnty >= 3 and price >=5000:
        discount = 0.10
    elif price < 5000:
        discount = 0.5
    else:
        discount = 0.0

    discount_amount = price *discount
    final_price = price - discount_amount

    print(f"Products quntity you bought is = {product_qnty}")
    print(f"Products Price is = {price}")
    print(f"Dicount applied ={discount*100}")
    print(f"Discount Price is = {discount_amount}")
    print(f'Final Bill is :{final_price}')

except ValueError:
    print("there is an erroe in system")

