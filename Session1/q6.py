heads=int(input("Enter heads - "))
legs=int(input("Enter  legs - "))
flag=False
j=0
for i in range(heads+1):
    j=heads-i
    if(legs==((4*i)+(2*j))):
        print("Dogs - ",i)
        print("Chicken - ",j)
        flag=True
        break
if(flag==False):
    print("not possible")    