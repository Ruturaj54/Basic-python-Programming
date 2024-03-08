
def main():
    
    No = 0
    print("Enter the Number")
    No = int(input())
    
    Result = No % 2
    
    if(Result==0):
        print("The Number is Even:",No)
    else:
        print("The number is Odd:",No)    
        
    
    
    
if __name__=="__main__":
    main()    