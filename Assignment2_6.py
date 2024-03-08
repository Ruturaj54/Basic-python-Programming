#6. Write a program which accept one number and display below pattern.
#Input : 5
#Output : * * * * *
#* * * *
#* * *
#* *
#*
def starprint(Value):
    
    Result = list()
    Ans = list()
    
    for i in range(0,Value,1):
        Result.append("*")
    
    print(Result)
    
    Count = 0
    while(Count <= len(Result)+1):
        a = Result.pop(1)
        print(Result)
        Count = Count + 1
 
             
def main():
    
    No = 0
    print("Enter the number:")
    No = int(input())
    
    starprint(No)
    
if __name__=="__main__":
    main()