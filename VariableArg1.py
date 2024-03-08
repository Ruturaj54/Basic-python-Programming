def Display(*Values):
    for i in range(len(Values)):
        print(Values[i])
        
def main():
    Display(10,20,30,40)
    Display(30,50,60)
    
if __name__=="__main__":
    main()