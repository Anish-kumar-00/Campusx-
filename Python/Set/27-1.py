"""
###Q1: Write a program to find set of common elements in three lists using sets.
Input : ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
Output : [80, 20]
"""

ar1 = set([1, 5, 10, 20, 40, 80])
ar2 = set([6, 7, 20, 80, 100])
ar3 = set([3, 4, 15, 20, 30, 70, 80, 120])
s3=ar1&ar2&ar3
print(s3)