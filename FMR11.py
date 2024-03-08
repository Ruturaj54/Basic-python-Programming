import MarvellousFMR

checkeven=lambda No : (No%2==0)    
Increase=lambda No : (No+2)
Add=lambda A,B : (A+B)

def main():

    
    Data=[]
    print("Enter the NUmber in list")
    Size=int(input())
    print("Enter the elements :")
    for i in range(Size):
   
        Value=int(input())
        Data.append(Value)
    output=list(MarvellousFMR.filterx(checkeven,Data))
    print("OUTPUT FROM FILTER",output)
    
    moutput=list(MarvellousFMR.mapx(Increase,output))
    
    print("output from map ",moutput)
    
    result=MarvellousFMR.reducex(Add,moutput)
    print("out from reduce",result)
    

if __name__=="__main__" :
    main()    
    