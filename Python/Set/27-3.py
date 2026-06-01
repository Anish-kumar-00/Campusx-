2.0.1 Q3: Write a program to Check if a given string is binary string of or not.
A string is said to be binary if it’s consists of only two unique characters.
Take string input from user.
Input: str = "01010101010"
Output: Yes
Input: str = "1222211"
Output: Yes
Input: str = "Campusx"
Output: No

str="01010101010"
#input("Enter a string:-")
uniue_str=set(str)
x=len(str)
print(x)
if x==2:
    print("Yes Binary string")
else:
    print("No ")