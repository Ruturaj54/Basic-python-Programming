def fun(no):
    Sum = 0
    
    for i in range (100000):
        Sum = Sum + (no*no)
    return Sum

def main():
    print("Demonstration of serial execution using single core")
    
    ret = fun(10)
    
    print(ret)
    
    
if __name__=="__main__":
    main()