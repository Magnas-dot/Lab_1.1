#Write a Python program to remove elements from a list that are also present in another list.
l1=[1,2,3,4,5,6,7]
l2=[2,5,4,7,8,9]
##print(l1-l2)
for i in l1:
    if i in l2:
        l1.remove(i)
print("Edited list:",l1)
