#!/usr/bin/env python
# coding: utf-8
11. Write a python program to find the factorial of a number. 
# In[1]:


import math

def factorial (x):
    return(math.factorial (x))

num = 10
print("Factorial of", num , "is", factorial (num))

12. Write a python program to find whether a number is prime or composite. 
# In[2]:


x=int(input("Enter any number:"))
if(x==0 or x==1):
    print(x,"Number is neither prime nor composite")
elif x>1:
    for i in range(2,x):
        if(x%i==0):
            print(x,"is composite number")
            break
    else:
        print(x,"number is prime number")


# In[3]:


x=int(input("Enter any number:"))
if(x==0 or x==1):
    print(x,"Number is neither prime nor composite")
elif x>1:
    for i in range(2,x):
        if(x%i==0):
            print(x,"is composite number")
            break
    else:
        print(x,"number is prime number")

13. Write a python program to check whether a given string is palindrome or not.
# In[4]:


str1=input("Enter String ")
str1=str1.casefold()

rev_str=reversed(str1)
if (str1)==(rev_str):
    print("The string is palindrome")
else:
    print("The string is not palindrome")

14. Write a Python program to get the third side of right-angled triangle from two given sides. 
# In[5]:


side1=float(input("Enter base: "))
side2=float(input("Enter height: "))

side3=math.sqrt(side1**2 + side2 **2)
print("Hypotenuse =", side3)

15. Write a python program to print the frequency of each of the characters present in a given string 
# In[6]:


str=input("Enter the string")
d=dict( )

for i in str:
    if i in d:
        d[ i ]=d[ i ]+1
    else:
        d[ i ]=1
print(d)


# In[ ]:




