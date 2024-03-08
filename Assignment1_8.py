#8. Write a program which accept number from user and print that number of “*” on screen.
#Input : 5 Output : * * * * *
def Starprinter(Value):
    data = "*"
    for i in range(Value):
        print(data,end=" ")
def main():
    
    No = 5
    print("Enter the value for number of times star to printed")
    No = int(input())
    
    Starprinter(No)
    
if __name__=="__main__":
    main()