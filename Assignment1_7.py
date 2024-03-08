#Write a program which contains one function that accept one number from user and returns
#true if number is divisible by 5 otherwise return false.

def Div(Value):
    
    if(Value % 5):
        print(bool(0))
    else:
        print(bool(1))
    
def main():
    
    No = 0
    print("Enter the number:")
    No = int(input())
    
    Div(No)
    
    
if __name__=="__main__":
    main()