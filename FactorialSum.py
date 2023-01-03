'''
Factorial Sum

Read two numbers M and N indefinitely. Calculate and write the sum of their factorial. Be carefull, because the result can have more than 15 digits.

Input
The input file contains many test cases. Each test case contains two integer numbers M (0 ≤ M ≤ 20) and N (0 ≤ N ≤ 20). The end of file is determined by eof.

Output
For each test case in the input your program must print a single line, containing a number that is the sum of the both factorial (M and N).

Input Sample
4 4
0 0
0 2

Output Sample
48
2
3
'''

def FacSum(m,n):

    if m==0:
        m = 1
    else:
        for i in range(m-1):
            m = m*(i+1)
    if n==0:
        n = 1
    else:
        for i in range(n-1):
            n = n*(i+1)

    return n+m

try:
    while True:
        M,N =  (int(i) for i in input().split())
        print(FacSum(M,N))
except:
    pass
