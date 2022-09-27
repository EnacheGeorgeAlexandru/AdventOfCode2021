with open("Day5.txt") as file:
    lines = file.readlines()
    lines = [line.split() for line in lines]

matrix = []
for i in range (1000):
    matrix.append([])
    for j in range (1000):
        matrix[i].append(0)
        
for line in lines:
    index = lines.index(line)
    start = line[0].split(',')
    stop = line[2].split(',')
    # as the input is given as coordinates in the xoy plane, in the 4th quadrant
    # but as positive integers, start[0] will not be refering to lines in the 
    # matrix, but to columns. start[1] will be refering to lines.
    for i in start:
        start[start.index(i)] = int(i)
    for i in stop:
        stop[stop.index(i)] = int(i)
    # equal column coordinate, so it plots vertical lines
    if start[0] == stop[0]:
        min_ = min(start[1],stop[1])
        max_ = max(start[1],stop[1])
        for i in range(min_ , max_+1):
            matrix[i][start[0]] += 1
    # equal line coordinate, so it plots horizontal lines
    if start[1] == stop[1]:
        min_ = min(start[0],stop[0])
        max_ = max(start[0],stop[0])
        for i in range(min_ , max_+1):
            matrix[start[1]][i] += 1
          
    #part2
    if abs(start[0] - stop[0]) == abs(start[1] - stop[1]):
        #diagonal line to the south-east:
        if start[1] < stop[1] and start[0] < stop[0]:
            j = start[0]
            for i in range(start[1],stop[1]+1):
                matrix[i][j] += 1
                j += 1
        #diagonal line to the south-west:
        if start[1] < stop[1] and start[0] > stop[0]:
            j = start[0]
            for i in range(start[1],stop[1]+1):
                matrix[i][j] += 1
                j -= 1
        #diagonal line to the north-east:
        if start[1] > stop[1] and start[0] < stop[0]:
            j = start[0]
            for i in range(start[1], stop[1] - 1, -1):
                matrix[i][j] += 1
                j += 1
        #diagonal line to the north-west:
        if start[1] > stop[1] and start[0] > stop[0]:
            j = start[0]
            for i in range(start[1], stop[1] - 1, -1):
                matrix[i][j] += 1
                j -= 1
        
count = 0
for line in matrix:
    for col in line:
        if col > 1:
            count += 1
print(count)
    
    
    

    