import os
import threading

def task1():
    print("PID of task1 is :",os.getpid())
    print("thread1 id is:",threading.get_ident())
    
def task2():
    print("pid of task2 is:",os.getpid())
    print("thread2 id is:",threading.get_ident())

def main():
    print("PID Of parent process is :",os.getpid())
    No=5
   
    t1=threading.Thread(target=task1,args=(No,))
    t2=threading.Thread(target=task2,args=(No,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    task1()
    task2()
     
if __name__=="__main__":
    main()
    
      
