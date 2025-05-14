cost_price=float(input("Enter cost price - "))
selling_price=float(input("Enter selling price - "))
if(cost_price>selling_price):
    print("It's a loss - ",cost_price-selling_price)
elif(selling_price>cost_price):
    print("It's a profit - ",selling_price-cost_price)
else:
    print("No profit no loss")        