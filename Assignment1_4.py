#4.Write a program which display times RRD tech  on screen.

def Display(Value1,pame):
    
    print("Your Output is:")
    for i in range (Value1):
        print(pame)
        
    
    
def main():
    print("Enter the number of time that you want to display the name")
    No = int(input())
    
    print("What to print please enter:")
    name = input()
    
    Display(No,name)
    
    
    
if __name__=="__main__":
    main()
    