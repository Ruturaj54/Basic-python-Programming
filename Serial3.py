import multiprocessing
import time

def fun(no):
    Sum = 0
    
    for i in range(100000):
        Sum = Sum +(no*no)
    return Sum

def main():
    print("Demostration of multiprocess or parallel execution")

    starttime = time.time()
    p = multiprocessing.Pool()
    
    Result = []
    Result = p.map(fun,range(10000))
    p.close()
    p.join()
    
    endtime = time.time()
    print("Time required to execute the application is:",endtime - starttime)
    
if __name__=="__main__":
    main()