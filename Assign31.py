

def main():
    
    Data=[]
    print("Enter the elements you want to substract:")
    Size=int(input())
    print("Enter the elements:")
    for i in range (Size):
        Value=int(input())
        Data.append(Value)
        
    print("LIST IS:",Data)
    
    Sub=0
        
    for i in range (Size):
        Sub = Data[i] - Sub
    
    print("ADITION IS :",Sub)
         

if __name__=="__main__":
    main()
    