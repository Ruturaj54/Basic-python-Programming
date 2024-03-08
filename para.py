import multiprocessing
import time

def Square(No):
    Result = 0
    Result = No*No
    return Result

def main():
    
    starttime = time.time()
    Ans = []
    
    print("Enter the values you want to enter:")
    i = int(input())
    
    print("Enter the elements")
    for value in range(i):

        no = int(input())
        Ans.append(no)
        
    out = []
    for p in range(len(Ans)):
        S = Square(Ans[p])
        out.append(S)
        
    print(out)
    endtime = time.time()
    
    print("Required time is ",endtime-starttime)
    
if __name__=="__main__":
    main()
        
        