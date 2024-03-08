import multiprocessing
import os

def task1(Value):
    print("executing the first task")
    print("pid of running process is task1 :",os.getpid())
    for i in  range(Value):
        print("task2:",i)
    
def task2(Value):
    print("executing the 2nd task")
    print("PID of running process is task2 :",os.getpid())
    for i in  range(Value):
        print("task2:",i)

    
def task3():
    print("Executing taask three")
    print("No of cores is:",os.cpu_count())
   
def main():

    print("Demostration of multiprocessing")
    
    print("pid of running process is",os.getpid())
    
    No=5
    p1=multiprocessing.Process(target=task1,args=(No,))
    p2=multiprocessing.Process(target=task2,args=(No,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    task1()
    task2()
    task3()

if __name__=="__main__": 
    main()
