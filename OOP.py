class Arthimeatic:
    def __init__(self,A,B):
        print("Inside constructor")
        self.No1=A
        self.No2=B
        
    def Addition(self):
        Ans=0
        Ans=self.No1+self.No2
        return Ans
    
    def substraction(self):
        Ans=0
        Ans=self.No1-self.No2    
        return Ans
        
def main():
    
    
    Value1=int(input("Enter the first Number:"))
    Value2=int(input("Enter the second Number:"))
    
    
    obj1=Arthimeatic(Value1,Value2)
    ret=obj1.Addition()
    ret1=obj1.substraction()
    
    print("addition:",ret)
    print("Substraction:",ret1)
    
    
    
    
if __name__=="__main__":
    main()
        