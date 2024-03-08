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

Add=lambda A,B : (A+B)

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
    