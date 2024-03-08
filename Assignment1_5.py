#Write a program which display 10 to 1 on screen.

def Display():
    
    No = list()
    
    No = [10,9,8,7,6,5,4,3,2,1]
    length = len(No)
    
    for i in range(length):
        print(No[i])
        
def main():
    
    print("Inside Main function")
    
    Display()
    
if __name__=="__main__":
    main()
    