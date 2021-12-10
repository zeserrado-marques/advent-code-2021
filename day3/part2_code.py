'''
--- Day 3: Binary Diagnostic ---

Oxygen and CO2 rating

'''

def getOnesAndZeros(num_list: list, column):
    zero_count = 0
    one_count = 0
    for j in range(len(num_list)):
        current_bit = num_list[j][column]
        if current_bit == 1:
            one_count += 1
        else:
            zero_count += 1
    return one_count, zero_count

def bitToRemove(is_oxygen: bool, current_bit):
    '''if the criteria is oxygen, we want to keep the current bit, which is the most common.
        it's the other way around for carbon
    '''
    if current_bit == 1:
        if is_oxygen:
            return 0
        else:
            return current_bit
    elif current_bit == 0:
        if is_oxygen:
            return 1
        else:
            return current_bit
    else:
        print('not a binary number. quiting macro')
        quit()


def ratingGetter(num_list: list, i: int, is_oxygen: bool):
    '''
        where the magic happens
    '''
    ola = num_list.copy()
    
    one_count, zero_count = getOnesAndZeros(ola, i)
    print(one_count, zero_count)

    # list with numbers to be removed
    if one_count >= zero_count:
        most_common_bit = 1
        bit_to_remove = bitToRemove(is_oxygen, most_common_bit)
        for number in num_list:
            current_column = number[i]
            if current_column == bit_to_remove:
                # it's better to remove the first ocurrence of the element, instead of using pop() for the index of the element
                ola.remove(number)
    else:
        most_common_bit = 0
        bit_to_remove = bitToRemove(is_oxygen, most_common_bit)
        for number in num_list:
            current_column = number[i]
            if current_column == bit_to_remove:
                ola.remove(number)
    # verifies if we have one number. if not, we run the function again
    if len(ola) == 1:
        return ola[0]
    else:
        return ratingGetter(ola, i+1, is_oxygen)
    

fhand = open('input.txt')
#fhand = open('test.txt')

num_list = list()

# insert file into a list. this will be a list of lists
for line in fhand:
    line = line.rstrip()
    a = [int(i) for i in line]
    #print(a)
    num_list.append(a)


col_size = range(len(a))
#row_size = range(len(num_list))
ola = num_list.copy()

oxygen = ratingGetter(num_list, 0, True)
carbon = ratingGetter(num_list, 0, False)
oxygen = ''.join([str(elm) for elm in oxygen])
carbon = ''.join([str(elm) for elm in carbon])

total = int(oxygen, 2) * int(carbon, 2)
print(oxygen, carbon)
print(total)
quit()

for i in col_size:
    one_count, zero_count = getOnesAndZeros(ola, i)
    print(one_count, zero_count)

    # list with numbers to be removed
    if one_count >= zero_count:
        most_common_bit = 1
        bit_to_remove = bitToRemove(True, most_common_bit)
        print(bit_to_remove)
        for number in num_list:
            current_column = number[i]
            if current_column == bit_to_remove:
                # it's better to remove the first ocurrence of the element, instead of using pop() for the index of the element
                ola.remove(number)
    else:
        for number in num_list:
            current_column = number[i]
            if current_column == 1:
                ola.remove(number)
    if len(ola) == 1:
        break
    break

print(ola)
