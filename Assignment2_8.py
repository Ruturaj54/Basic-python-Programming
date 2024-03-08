#8. Write a program which accept one number and display below pattern.
#Input : 5
#Output : 1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

def printer(Value):
    data = list()
    Value = Value + 1
    
    for i in range(1,Value,1):
        data.append(i)
        print(data)
    
        
   
        
    
def main():
    No = 0
    print("Enter the number:")
    No = int(input())
    
    printer(No)
    
    
    

if __name__=="__main__":
    main()