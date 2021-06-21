'''
Problem Statement:
Anagrams Given two strings as input, determine if they are anagrams are not. 
(Ignore the spaces, case and any punctuation or special characters) 
Note: Anagrams are the strings which are made up of the same set of letters. 
For example : Mary and Army are anagrams.

Input Format

First line of the input contains the first string Second line of the input contains the second string

Constraints

Words<100

Output Format

Print Yes if the given strings are anagrams, No otherwise.

Sample Input 0

Tom Marvolo Riddle
I am Lord Voldemort!!!
Sample Output 0

Yes

Sample Input 1

The Morse Code
Here come dots
Sample Output 1

Yes

Sample Input 2

Oh, lame saint 
The Mona Lisa
Sample Output 2

Yes

Sample Input 3

Royal Challengers Bangalore
Rajasthan Royals
Sample Output 3

No'''





import re

def remove_Unwanted_Char(x):
    temp_x = re.sub(r'[?|$|.|!]',r'',x)
    filtered_x = re.sub(r'[^a-zA-Z ]',r'',temp_x.lower())
    return filtered_x.replace(" ", "")

def anagram(x,y):
    xl = sorted(remove_Unwanted_Char(x))
    yl = sorted(remove_Unwanted_Char(y))    
    return "Yes" if xl == yl else "No"
    
x = input()
y = input()

print(anagram(x,y))