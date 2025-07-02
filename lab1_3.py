##Write a Python function that accepts a list and returns a new list with only the even numbers from the original list.
l=[]
for i in range(10):
    x=int(input("Enter Number:"))
    l.append(x)
even_list=[]
for num in l:
    if(num%2==0):
        even_list.append(num)
print("Even Numbers:",even_list)
