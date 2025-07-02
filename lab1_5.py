##Create a set of prime numbers less than 50. Write a program to check
##whether a given number exists in the set or not.
prime=[]
for i in range(1,51):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
            
    if(count==2):
            prime.append(i)
p_search=int(input("enter number to search:"))
if p_search in prime:
        print("found") 
else:
        print(f"{p_search} not found in the given list") 


