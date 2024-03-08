def main():
    print("Enter the Size of list:")
    size = int(input())
    
    data = list()
    
    print("Enter the elements")
    for i in range(size):
        value = int(input())
        data.append(value)
        
    print("Elements are:")
    for i in range(len(data)):
        print(data[i])
        
if __name__=="__main__":
    main()            