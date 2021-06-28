'''
You are given a staircase with n steps. This means that you can 
go from bottom to top in n steps. Write a function that counts
the number of ways you can go from bottom to top
Note that you can only take one or two steps at a time.

Sample testcase:
n = 2
Sample Output:
2

Explaination:
1st way - 0 -> 1 -> 2 (One step at a time)
1nd way - 0 -> 2 (Two steps at a time)


Sample testcase 1:
n = 1
Sample Output 1:
1

Explaination:
Only way - 0 -> 1 (One step at a time)

n = 3
0 -> 1 -> 2 -> 3, 0 -> 1 -> 3, 0 -> 2 -> 3

n = 4
0 -> 1 -> 2 -> 3 -> 4
0 -> 1 -> 3 -> 4
0 -> 2 -> 3 -> 4
0 -> 1 -> 2 -> 4
0 -> 2 -> 4



'''

"""def ways(n):
    if n == 0 or n == 1:
        return 1
    else:
        return ways(n-1) + ways(n-2)
"""

def ways(n):
    if n == 0 or n == 1:
        return 1
    table = (n+1)*[0]
    table[0] = table[1] = 1
    for i in range(2,n+1):
        table[i] = table[i-1] + table[i-2]
    
    #print(table)
    return table[n]


n = int(input())
print(ways(n))