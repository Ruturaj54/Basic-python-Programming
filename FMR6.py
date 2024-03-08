import functools
#def checkeven(No):
 #   if(No%2==0):
  #      return True
  #  else:
#      return False
    

    
#def Increase(No):
#    return No+2;


#def Add(A,B):
 #   return A+B


def main():

    
    Data=[]
    print("Enter the NUmber in list")
    Size=int(input())
    print("Enter the elements :")
    for i in range(Size):
   
        Value=int(input())
        Data.append(Value)
        
    output=list(filter((lambda No : (No%2==0)),Data))
    print("OUTPUT FROM FILTER",output)
    
    moutput=list(map((lambda No : (No+2)),output))
    
    print("output from map ",moutput)
    
    result=functools.reduce((lambda A,B : (A+B)),moutput)
    print("out from reduce",result)
    

if __name__=="__main__" :
    main()    
    