#9. Write a program which display first 10 even numbers on screen.
#Output : 2 4 6 8 10 12 14 16 18 20
def Evenprinter(Value):
    if (Value > 0):
        Value = Value * 2 + 1
    Arr = list()
    for i in range(1,Value,1):
        if(i % 2 == 0):
            Arr.append(i)
    print(Arr)
        

def main():
    print("Enter the first 10 or any number to display even number")
    No = int(input())
    
    Evenprinter(No)
    
if __name__=="__main__":
    main()