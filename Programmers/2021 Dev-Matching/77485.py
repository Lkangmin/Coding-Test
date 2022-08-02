def solution(rows, columns, queries):
    answer = []
    matrix = [[columns*i+j for j in range(1, columns+1)] for i in range(rows)]
    
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        min_v = matrix[x1][y1]
        fir = matrix[x1][y1]
        
        for x in range(x1, x2):
            if min_v > matrix[x+1][y1]:
                min_v = matrix[x+1][y1]
            matrix[x][y1] = matrix[x+1][y1]

        for y in range(y1, y2):
            if min_v > matrix[x2][y+1]:
                min_v = matrix[x2][y+1]
            matrix[x2][y] = matrix[x2][y+1]
                
        for x in range(x2, x1, -1):
            if min_v > matrix[x-1][y2]:
                min_v = matrix[x-1][y2]
            matrix[x][y2] = matrix[x-1][y2]

            
        for y in range(y2, y1+1, -1):
            if min_v > matrix[x1][y-1]:
                min_v = matrix[x1][y-1]
            matrix[x1][y] = matrix[x1][y-1]

        matrix[x1][y1+1] = fir
        answer.append(min_v)

    return answer