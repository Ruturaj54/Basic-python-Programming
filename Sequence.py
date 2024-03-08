# Sequence:set of Statements executed in a linear manner

#Function 
def main():
    Ans = 0
    print("Enter thr first number:")
    Value1 = int(input())           #input takes default value as a string
                                     #so we typecaste it to int
    print("Enter the second number:")
    Value2 = int(input())
    
    Ans = Value1 + Value2
    print("Addition is :",Ans)

if __name__=="__main__":    #Starter 
    main()                      