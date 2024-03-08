Set1 = {11,78.89,"Hello",True}
print(Set1)

#print(Set1[1])

for Value in Set1:  #for each loop
    print(Value)   
    
Set2 = {11,78,89,11,78}
print(Set2)

Set2.add(101)
print(Set2)

Set2.remove(101)
print(Set2)

print("Enter the value you want to search in set")
No = int(input())

for Value in Set2:
    if(No == Value):
        print("Elements is present")
        break
    