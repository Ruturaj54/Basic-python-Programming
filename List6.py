def main():
    print("Enter the number that you wants:")
    length = int(input())
    
    Arr = list()
    
    print("Enter the elements:")
    for i in range(length):
        value = int(input())
        Arr.append(value)
        
    print("Elements in the list are:")
    for i in range(len(Arr)):
        print(Arr[i])
            
if __name__=="__main__":
    main()    