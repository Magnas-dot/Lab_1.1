#Given a list of names, write a program to count how many times each name appears using a dictionary
li=('sangam','paudel','maxey','joey','hendrison','sangam')
dictn={}
for char in li:
    if char in dictn:
        dictn[char]+=1
    else:
        dictn[char]=1
print(dictn)
   
