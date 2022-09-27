#part one

number_of_digits = 12
ones = 0
zeroes = 0
gamma = 0
epsilon = 0
for n in range(number_of_digits):
    file = open('Day3.txt', 'r')
    for number in file:
        string_base2 = str(number)
        if int(string_base2[n]) == 1:
            ones += 1
        else:
            zeroes += 1
    if ones > zeroes:
        gamma += 2 ** (number_of_digits - n - 1)
    else:
        epsilon += 2 ** (number_of_digits - n - 1)
    ones = 0
    zeroes = 0

print(gamma * epsilon)

#part two      
def oxygen_generator_rating(mylist,n):
    def most_common_digit(mylist,position):
        ones = 0
        zeroes = 0
        for number in mylist:
            string_base2 = str(number)
            if int(string_base2[position]) == 1:
                ones += 1
            else:
                zeroes += 1
        if ones >= zeroes:
            return 1
        else:
            return 0
    if len(mylist) == 0:
        file = open('Day3.txt', 'r')
        for number in file:
            mylist.append(number)
   
    if len(mylist) == 1 or n == 12:
        return mylist
    else:
        man_list = []
        for number in mylist:
            string_base2 = str(number)
            if int(string_base2[n]) == most_common_digit(mylist,n):
                man_list.append(number)
        mylist.clear()
        mylist = man_list
        return oxygen_generator_rating(mylist, n+1)
    
def co2_scrubber_rating(mylist2,n):
    def least_common_digit(mylist,position):
        ones = 0
        zeroes = 0
        for number in mylist:
            string_base2 = str(number)
            if int(string_base2[n]) == 1:
                ones += 1
            else:
                zeroes += 1
        if ones >= zeroes:
            return 0
        else:
            return 1
    if len(mylist2) == 0:
        file = open('Day3.txt', 'r')
        for number in file:
                mylist2.append(number)

    if len(mylist2) == 1 or n == 12:
        return mylist2
    else:
        man_list2 = []
        for number in mylist2:
            string_base2 = str(number)
            if int(string_base2[n]) == least_common_digit(mylist2,n):
                man_list2.append(number)
        mylist2.clear()
        mylist2 = man_list2
        return co2_scrubber_rating(mylist2, n+1)
        
        
#print(int(oxygen_generator_rating(mylist=[],n = 0)[0],2))
#print(int(co2_scrubber_rating(mylist2=[], n=0)[0],2))  
print(int(oxygen_generator_rating(mylist=[],n = 0)[0],2) * int(co2_scrubber_rating(mylist2=[], n=0)[0],2) )
        
    
        

    
    
    
    