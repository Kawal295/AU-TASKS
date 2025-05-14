while(1):
    print("1. cm to ft")
    print("2. km to miles")
    print("3. USD to INR")
    print("4. exit")
    print()
    choice=int(input("Enter choice - "))
    if(choice==1):
        cm=float(input("Enter cm - "))
        ft=cm/30.48
        print("ft -",ft)
        print()
    elif(choice==2):
        km=float(input("Enter km - "))
        miles=km*0.62137119
        print("miles -",miles) 
        print()
    elif(choice==3):
        USD=float(input("Enter USD - "))
        INR=USD*85.28
        print("INR -",INR)
        print()
    elif(choice==4):
        break
    else:
        print("RETRY") 
        print()
        continue         