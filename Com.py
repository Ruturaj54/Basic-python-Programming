import sys

def main():
    print("Command line argument Demonstration:")
    
    Value1 = int(sys.argv[1])
    Value2 = int(sys.argv[2])
    
    Ans = Value1 + Value2
    
    print("length is:",len(sys.argv))
    
    print("Addition is :",Ans)
    
if __name__=="__main__":
    main()    
    
# python Com.py 10 11
# OP = ADDITION 21
#LENGTH = 3  [com.py,Value1,Value2]