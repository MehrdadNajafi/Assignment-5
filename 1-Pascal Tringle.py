n = int(input('pls enter the number of row: '))

list = [[1 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(1,i):
        list[i][j] = list[i-1][j] + list[i-1][j-1]

for i in range(n):
    for j in range(i+1):
        print(list[i][j],end=' ')
    print()