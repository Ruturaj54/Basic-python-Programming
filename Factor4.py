No = 0
print("Enter the number whoes factors you want")

No = int(input())

for no in range(1,No,1):
    if(No % no == 0):
        print("The factors are",no)
        