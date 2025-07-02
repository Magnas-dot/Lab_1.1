##Create a tuple of 10 integers.WAP to display the maximum and minimum numbers from the tuple.
import random
list1=[]
for i in range(10):
    x=random.randint(1,100)
    list1.append(x)
tup=tuple(list1)
print(tup)
maximum=max(tup)
minimum=min(tup)
print("Maximum is:",maximum)
print("Minimum is:",minimum)
