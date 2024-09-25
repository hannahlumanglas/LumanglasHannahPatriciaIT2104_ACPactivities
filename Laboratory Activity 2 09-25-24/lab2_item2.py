while True:
    purchase_amount = float(input("Enter the total purchase amount: "))
    if purchase_amount > 5000:
        discount_rate = 0.10 
    else:
        discount_rate = 0.05  

    discount = purchase_amount * discount_rate
    final_price = purchase_amount - discount
    
    print(f"Initial Purchase Amount: {purchase_amount:.2f}")
    print(f"Discount: {discount:.2f}")
    print(f"Final Price: {final_price:.2f}")
    
    try_again = input("Do you want to try again? (yes/no): ")
    if try_again!= 'yes':
        break

print("Thank you!")