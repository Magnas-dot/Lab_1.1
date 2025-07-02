#Write a program to input key-value pairs from the user and store them in a dictionary. Allow the user to search for a key and display its value.
n=int(input("Enter how many key-values (items) to input:"))
dictn={}
for i in range(n):
      key=input("Enter key:")
      value=input("enter value:")
      dictn[key]=value
key_s=input("Enter keys to search:")
for j in dictn:
      if (j==key_s):
         print("value:",dictn[j])
         break
else:
    print("keys not found:")
      
      
            
