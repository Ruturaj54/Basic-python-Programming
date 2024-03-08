def ADDITION(No1,No2):
    ans=0
    ans=No1+No2
    return ans

def Substraction(No1,No2):
    ans=0
    ans=No1-No2
    return ans

def main():
    
    Value1=int(input("Enter the first Number:"))
    Value2=int(input("Enter the second Number:"))
    
    ret=ADDITION(Value1,Value2)
    print("Addition is :",ret)
    
    ret=Substraction(Value1,Value2)
    print("Substraction is :",ret)
    
    
if __name__=="__main__":
    main()
        
        