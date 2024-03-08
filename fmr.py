from functools import reduce
def checkeven(No):
    if(No%2==0):
        return True
    else:
        return False
    
def Increase(No):
    return No+2;

def Add(A,B):
    return A+B
def main():
    
    Data=[10,20,13,40,43,13]
    print(Data)
    output=list(filter(checkeven,Data))
    print(output)
    moutput=list(map(Increase,output))
    print(moutput)
    result=reduce(Add,moutput)
    print(result)
    
if __name__=="__main__":
    main()
