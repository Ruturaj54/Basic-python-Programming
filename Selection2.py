def Checkeven(Value):
    Result = 0
    Result = Value % 2
    
    if(Result == 0):
        print("The Number is Even:",Value)
    else:
        print("The Number is Odd:",Value)    

def main():
    No = 0
    print("enter the Number:")
    No = int(input())
    
    Checkeven(No)
    
if __name__=="__main__":
    main()    
    

    