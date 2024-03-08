#5.Write a program which accept one number for user and check whether number is prime or not.
#Input : 5 Output : It is Prime Number
def primecheck(Value):
    #Value = Value + 1
    for i in range(2,Value,1):
        if(Value % i == 0):
            flag = 1
        else:
            flag = 0
    if(flag == 0):
        print("Prime number..")
    else:
        print("Not a prime number")
        
def main():
    No = 0
    print("Enter the number :")
    No = int(input())
    
    primecheck(No)
    
if __name__=="__main__":
    main()