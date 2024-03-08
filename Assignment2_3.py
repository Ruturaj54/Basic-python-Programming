#3. Write a program which accept one number from user and return its factorial.
#Input : 5 Output : 120
def Factor(Value):
    
    Value = Value + 1
    Result = 1
    
    for i in range(1,Value,1):
        Result = Result * i
        
    print("Factorial is :",Result)    
        
    
def main():
    NO = 0
    print("Enter the number:")
    NO = int(input())
    
    Factor(NO)

if __name__=="__main__":
    main()
    