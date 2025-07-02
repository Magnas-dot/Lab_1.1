##Write a Python program to merge two dictionaries and sum the values of common keys.
dict1={'a':1,'b':2,'c':2}
dict2={'a':2,'b':4,'d':4}
dict3=dict1.copy()
dict3.update(dict2)
for key in dict1:
    if key in dict2:
        dict3[key]=dict1[key]+dict2[key]
print(dict3)
