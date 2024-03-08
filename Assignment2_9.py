# 9. Write a program which accept number from user and return number of digits in that number.
#Input : 5187934 Output : 7

def Digitcount(Value1):
    #i = Value1 % 10
    #print(i)
    #data = list()
    i = str(Value1)
    count = 0 
    count = len(i)
    print(count)
    
    
    
def main():
    
    #No = 0
    print("Enter the number:")
    No = input()
    
    Digitcount(No)
    
if __name__=="__main__":
    main()