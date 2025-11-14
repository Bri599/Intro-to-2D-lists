#1D list
scores=[20,20,14,15,8]
print(scores)
print(len(scores))
print(scores[0])
print(scores[2])
for i in scores:
    print(i)

#2D list
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(matrix[0])
print("row=",len(matrix))
print("columns=",len(matrix[0]))
print(matrix[1][0])
print("My matrix ")
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j],end=" ")
    print()