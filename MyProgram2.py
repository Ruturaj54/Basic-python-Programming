def CalculateArea(Value1):
    PI = 3.14
    Ans = 0.0
    Ans = PI * Value1 * Value1
    return Ans
    
def main():
    
   
    RADIUS = 0.0
    Area = 0
    print("Enter the Radius of circle:")
    RADIUS = int(input())
    
    Area = CalculateArea(RADIUS)
    
    print("Area of circle is:",Area)
    
    
    
    
if __name__=="__main__":
    main()