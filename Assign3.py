#Write aprogram that accepts n number form user and store into list
#return addition of all numbers and all elements from that list
def main():
    Data=[]
    print("Enter the number of elements you want to add:")
    Size=int(input())
    
    print("Enter the numbers:")
    for i in range (Size):
        Value=int(input())
        Data.append(Value)   
        
    print("list of input numbers:",Data) 
    
    
    Add=0
    for i in range (Size):
       Add=Data[i]+Add
       
    print("Addition is :",Add)       
    

if __name__=="__main__":
    main()    