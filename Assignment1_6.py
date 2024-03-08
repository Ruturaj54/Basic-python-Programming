#6.Write a program which accept number from user and check whether that number is positive or
#negative or zero.

def Check(Value):
    
    if (Value > 0):
        print("Value is Positive:",Value)
    elif (Value < 0):
        print("Value is Negetive:",Value)
    else:
        print("Value is zero",Value)


def main():
    
    No = 0
    print("Enter the Number")
    No = int(input())
    
    Check(No)
    
    
if __name__=="__main__":
    main()