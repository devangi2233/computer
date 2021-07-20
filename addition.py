m1 =[[2, 5],[4, 7]]
m2 = [[4, 7], [6, 2]]

result = [[0, 0], [0,0]]

for i in range(len(m1)):
    for j in range(len(m1[0])):
        result[i][j] = m1[i][j] + m2[i][j]
    
for r in result:
    print(r)
