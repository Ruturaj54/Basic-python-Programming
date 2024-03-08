#10. Write a program which accept number from user and return addition of digits in that number.
#Input : 5187934 Output : 37
def DigitSum(Value):
    Sum = 0
    while(Value != 0):
        
        Sum = Sum + int(Value % 10)
        Value = int(Value/10)
    print(Sum)
        
        
def main():
    
    No = 0
    print("Enter the number:")
    No = int(input())
    
    DigitSum(No)
    
    
if __name__=="__main__":
    main()