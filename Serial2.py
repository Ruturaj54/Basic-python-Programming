import time

def fun(no):
    Sum = 0
    
    for i in range (100000):
        Sum = Sum + (no*no)
        
    return Sum

def main():
    print("Demonstration of serial execution using single core")
    
    starttime = time.time()
    
    Result = []
    
    for i in range(10000):
        Result.append(fun(i))
        
    endtime = time.time()
    print("time required to execute the program is :",endtime - starttime)
    
if __name__=="__main__":
    main()
        