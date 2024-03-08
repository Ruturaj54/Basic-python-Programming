def fun(no):
    Sum = 0
    
    for i in range (100000):
        Sum = Sum + (no*no)
    return Sum

def main():
    print("Demonstration of serial execution using single core")
    
    Result = []
    
    for no in range(10000):
        Result.append(fun(no))
        
    
    
if __name__=="__main__":
    main()