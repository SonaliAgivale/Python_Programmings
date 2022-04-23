print("*****Power Of Two******")
no=int(input("Enter the no: "))
if (no == 1):
    print("It is power of 2.");
else:  
        while (no > 1):
                remainder = no % 2
                if (remainder != 0):
                    break;
                no /= 2
        if (no == 1):
                print("It is a power of 2")
        else:
                print("It is not a power of 2")
