import time
def square(no):
    return no*no

def main():
    Arr = [10,20,30,40]
    Result = []
    
    starttime = time.time()
    
    for value in Arr:
        Ans = square(value)
        Result.append(Ans)
    
    print(Result)
    
    endtime = time.time()
    
    print("Time requried is:",endtime - starttime)
    
if __name__=="__main__":
    main()