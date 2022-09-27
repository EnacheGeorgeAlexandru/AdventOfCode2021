with open("Day4.txt") as file:
    lines = file.readlines()
    vector = lines[0].split(',')
    lines = [line.split() for line in lines]
    
boards = []
for i in range (1,len(lines)):
    if lines[i]:
        boards.append(lines[i])
        
min_moves_nr = len(vector)
max_moves_nr = 0
for i in range (0,len(boards),5):
    matrix = []
    moves_nr = 0
    board_score = 0
    board_sum = 0
    matrix = boards[i:i+5]
    for i in range(5):
        for j in range(5):
            board_sum += int(matrix[i][j])
    bingo_line = 0
    bingo_column = 0
    for number in vector:
        moves_nr += 1
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == number:
                    board_sum -= int(matrix[i][j])
                    bingo_line = 1
                    bingo_column = 1
                    matrix [i][j] = ' '
                    for a in range(5):
                        if matrix[i][a] != ' ':
                            bingo_line = 0
                    for b in range(5):
                        if matrix[b][j] != ' ':
                            bingo_column = 0
        if bingo_line == 1 or bingo_column == 1:
            board_score = int(number) * board_sum
            break 
    if moves_nr < min_moves_nr:
        min_moves_nr = moves_nr
        winning_score = board_score
    if moves_nr > max_moves_nr:
        max_moves_nr = moves_nr
        losing_score = board_score
        

print(winning_score,losing_score)          
    

        

