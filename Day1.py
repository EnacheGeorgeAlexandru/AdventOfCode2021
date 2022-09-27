file = open('Day1.txt', 'r')
larger_measurments = 0
number_list = []
for number in file:
    number_list.append(int(number))

'part one'
for i in range(1, len(number_list)):
    if number_list[i] > number_list[i-1]:
        larger_measurments += 1
        
print(larger_measurments)
larger_measurments = 0



'part two'
a = 0
for i in range (len(number_list) - 3):
    a = number_list[i] + number_list[i+1] + number_list[i+2]
    b = number_list[i+1] + number_list[i+2] + number_list[i+3]
    if b > a:
        larger_measurments += 1
        
print(larger_measurments)
    
    
    
    
        
        
