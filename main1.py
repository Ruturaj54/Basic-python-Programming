def Addition(No1,No2):
    result = 0
    result = No1 + No2
    return result

def main():
    Value1 = int(input("Enter the value:"))
    Value2 = int(input("Enter the value:"))
    
    ans = 0
    ans = Addition(Value1,Value2)
    
    print("Addition is : ",ans)
    