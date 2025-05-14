salary=float(input("Enter salary(in lakhs) - "))
hra=10
da=5
pf=3
if(salary<5):
    tax=0
elif(salary>=5 and salary<10):
    tax=10
elif(salary>=10 and salary<20):
    tax=20
else:
    tax=30            
in_hand_salary=salary-(salary*hra/100)-(salary*da/100)-(salary*pf/100)-(salary*tax/100)
print(in_hand_salary)