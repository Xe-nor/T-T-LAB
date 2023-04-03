n=int(input("Enter number of elements : "))
print("Enter the elements: ")
l=[]
for i in range(0, n):
    inp=input()
    l.append(inp)
print("List: ", l)
num=int(input(("Enter number: ")))
index=int(input("Enter index: "))
l.insert(index, num)
print("New List: ",l)