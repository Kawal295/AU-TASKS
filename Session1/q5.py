p=int(input("Enter principle amount - "))
r=float(input("Enter rate of interest - "))
t=float(input("Enter time(in years) - "))
simpleInterest=(p*r*t)/100
print("Simple Interest = ",simpleInterest)
print("Total value = ",p+simpleInterest)