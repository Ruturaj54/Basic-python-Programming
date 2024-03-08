# lambda function

def Add(A,B):
     return A+B
 

AddX =lambda A,B : (A + B) 
 
def checkeven(No):
    return No%2==0

checkevenx=lambda No : (No%2==0)


def Increase(No):
    return No+2 

Increasex=lambda No : (No+2)


def main():
    ret=Add(10,11)
    print(ret)
    ret=checkeven(10)
    print(ret)
    ret=Increase(10)
    print(ret)

if __name__=="__main__":
     main()
        