import multiprocessing
import time
def square(no):
    return no * no

def main():
    Arr = [10,20,30,40]
    Result = []
    
    starttime = time.time()
    
    p = multiprocessing.Pool()
    Result = p.map(square,Arr)
    p.close() #closes the pool content
    p.join()  #this method tells that all core conclude
                #the work then go ahead
    print(Result)
    
    endtime = time.time()
    
    print("Required time is:",endtime-starttime)
    
    
if __name__=="__main__":
    main()