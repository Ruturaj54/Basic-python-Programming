import Arithmetic

def main():
    No = 0
    No1 = 0
    No2 = 0
    
    print("Enter the First Numbers:")
    No1 = int(input())
    
    print("Enter the Second Number:")
    No2 = int(input())
    
    
    print("what operation to be performed [Enter Selected No]:")
    print("1.Addition")
    print("2.Substration")
    print("3.Multiplication")
    print("4.Division")
    
    No = int(input())
    
    if (No == 1):
        Arithmetic.Add(No1,No2)
    elif(No == 2):
        Arithmetic.Sub(No1,No2)
    elif(No == 3):
        Arithmetic.Mul(No1,No2)
    elif(No == 4):
        Arithmetic.Div(No1,No2)
    else:
        print("Enter valid Number....")
    
    
    
    
if __name__=="__main__":
    main()