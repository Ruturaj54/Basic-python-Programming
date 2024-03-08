#Write a program which contains one function named as Add() which accepts two numbers
#from user and return addition of that two numbers.

def Addition(Value1,Value2):
    
    Result = 0
    Result = Value1 + Value2
    print("Addition of Both Numbers is:",Result)


def main():
    
    No1 = 0
    No2 = 0
    print("Enter the Number 1")
    No1 = int(input())
    
    print("Enter the Numnber 2")
    No2 = int(input())
    
    Addition(No1,No2)
    
    
    
    
    
if __name__=="__main__":
    main()