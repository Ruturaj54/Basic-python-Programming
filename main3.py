def Addition(No1,No2):
    Result = 0
    Result = No1 + No2
    return Result

def main():
    Value1 = int(input("Enter the Number:"))
    Value2 = int(input("Enter the Number:"))
    
    Ans = 0
    Ans = Addition(Value1,Value2)
    
    print("Addition is :",Ans)
    
main()    