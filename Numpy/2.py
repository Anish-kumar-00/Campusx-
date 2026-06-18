"""###Q-2 Ask user to input two numbers a, b. 
Write a program to generate a random array of
shape (a, b) and print the array and avg of 
the array.
"""
a=3
b=2
import numpy as np  
#l=np.array([np.random.random() for i in range(6)])
l=np.random.random((a,b))*100
print(np.ceil(l))