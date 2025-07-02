##WAP to count the number of each character in a given string using a dictionary.
name="sangam"
dictn={}
for char in name:
    if char in dictn:
        dictn[char]+=1
    else:
        dictn[char]=1
print(dictn)
