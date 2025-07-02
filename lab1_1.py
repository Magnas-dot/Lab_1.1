#WAP to remove all duplicates from a list and print the unique elements.
import random
list_1=[]
for i in range(10):
    list_1.append(random.randint(1,50))
list_2=set(list_1)
print(list_2)
