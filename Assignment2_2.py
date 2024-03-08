#2. Write a program which accept one number and display below pattern.
#Input : 5
#Output : * * * * *
#* * * * *
#* * * * *
#* * * * *
#* * * * *
def printer(Value):
    data = 0
    data = list()
    
    for i in range(Value):
        data.append("*")
        
    for i in range(Value):
        print(data)
        
    
    
def main():
    
    No = 0
    print("Enter the number:")
    No = int(input())
    
    printer(No)
    
    
if __name__=="__main__":
    main()