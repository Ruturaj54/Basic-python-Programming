#10. Write a program which accept name from user and display length of its name.
#Input : Marvellous Output : 10
def length(string):
    print("Length of string is:",len(string))
    
def main():
    
    print("Enter any name:")
    name = input()
    
    length(name)
    
if __name__=="__main__":
    main()