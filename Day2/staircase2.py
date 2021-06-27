'''
You are given a staircase with n steps. This means that you can 
go from bottom to top in n steps. Write a function that counts
the number of ways you can go from bottom to top
Note that you can take one or three or five steps at a time.

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
    if n == 0:
        return 1
    no_ways = 0
    allowed_steps = [1,3,5]
    for step in allowed_steps:
        if n-step >= 0:
            no_ways += ways(n-step)
    
    return no_ways
"""

def ways(n):
    if n == 0:
        return 1
    allowed_steps = [1,3,5]
    table = (n+1)*[0]
    table[0] = 1

    for i in range(1,n+1):
        no_ways = 0
        for step in allowed_steps:
            if i-step >= 0:
                no_ways += table[i-step]
        table[i] = no_ways
     
    #print(table)
    return table[n]


n = int(input())
print(ways(n))