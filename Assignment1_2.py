#2. Write a program which contains one function named as ChkNum() which accept one
#parameter as number. If number is even then it should display “Even number” otherwise
#display “Odd number” on console.

def CheckNum(Value):
    
    if (Value % 2 == 0):
        print("Number is Even:",Value)
    else:
        print("NUmber is Odd:",Value)


def main():
    print("Enter the Number to be checked:")
    No = int(input())
    
    CheckNum(No)
    
    
if __name__=="__main__":
    main()