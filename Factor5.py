def Checkfactors(Value):
    
    
    for no in range(1,Value,1):
        if(Value % no == 0):
            print("Value is factors",no)
            
def main():
    No = 0
    
    print("Enter the value")
    No = int(input())
    
    Checkfactors(No)
    
if __name__=="__main__":
    main()    
    