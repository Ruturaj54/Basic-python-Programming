#4.Write a program which accept one number form user and return addition of its factors.
#Input : 12 Output : 16 (1+2+3+4+6)

def Factors(Value):
    
    data = list()
    
    Result = 0
    for i in range(1,Value,1):
        if(Value % i == 0):
            data.append(i)
            Result = Result + i
    print("Factors are:",data)
    print("Sum is:",Result)
    
def main():
    NO = 0
    print("Enter the number:")
    NO = int(input())
    
    Factors(NO)

if __name__=="__main__":
    main()
    