



from functools import reduce
#def checkeven(No):
 #   if(No%2==0):
  #      return True
  #  else:
  #      return False
    
checkeven=lambda No : (No%2==0)    
    
#def Increase(No):
#    return No+2;

Increase=lambda No : (No+2)
#def Add(A,B):
 #   return A+B
#Task =name of function
#elements=list of data elements

Add=lambda A,B : (A+B)

def filterx(Task,Elements):
    Result=[]
    for no in Elements:
        if (Task(no)==True):
            Result.append(no)
    return Result

def mapx(Task,Elements):
    Result=[]
    for no in Elements:
        ret=Task(no)
        Result.append(ret)
    return Result

def reducex(Task,Elements):
    Sum=0
    for no in Elements:
        Sum=Task(Sum,no)
        
    return Sum    

        
    
        
def main():

    
    Data=[]
    print("Enter the NUmber in list")
    Size=int(input())
    print("Enter the elements :")
    for i in range(Size):
   
        Value=int(input())
        Data.append(Value)
    output=list(filter(checkeven,Data))
    print("OUTPUT FROM FILTER",output)
    
    moutput=list(map(Increase,output))
    
    print("output from map ",moutput)
    
    result=reduce(Add,moutput)
    print("out from reduce",result)
    

if __name__=="__main__" :
    main()    
    