'part one'

file = open('Day2.txt', 'r')
horizontal_position = 0
depth = 0
for line in file:
    command = line.split()
    if command[0] == 'up':
        depth -= int(command[1])
    if command[0] == 'down':
        depth += int(command[1])
    if command[0] == 'forward':
        horizontal_position += int(command[1])

print(horizontal_position * depth)

'part two'
file = open('Day2.txt', 'r')
horizontal_position = 0
depth = 0
aim = 0
for line in file:
    command = line.split()
    if command[0] == 'up':
        aim -= int(command[1])
    if command[0] == 'down':
        aim += int(command[1])
    if command[0] == 'forward':
        horizontal_position += int(command[1])
        depth += aim * int(command[1])

print(horizontal_position * depth)



    
        
    
    