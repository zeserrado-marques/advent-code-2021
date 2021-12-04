'''
--- Day 3: Binary Diagnostic ---

'''
import numpy as np

fhand = open('input.txt')
#fhand = open('test.txt')

test = np.array([])

# insert file into an nparray
for line in fhand:
    line = line.rstrip()
    a = [int(i) for i in line]

    # create nparray by joining new rows at the end 
    if len(test) == 0:
        test = np.array(a)
    else:
        test = np.vstack((test,a))
    
# rows become columns and vice-versa
test = np.stack(test, axis=-1)

gamma_rate = str()
epsilon_rate = str()

# count the bits for the gamma and epsilon rate calculation
for column in test:
    one_count = 0
    zero_count = 0
    for bit in column:
        if bit == 0:
            zero_count +=1
        else:
            one_count += 1
    if one_count > zero_count:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

# convert binary into decimal and multiply
gamma_decimal = int(gamma_rate, 2)
epsilon_decimal = int(epsilon_rate, 2)
total = gamma_decimal * epsilon_decimal

# print gamma and epsilon in binarey and decimal
print(gamma_rate, epsilon_rate)
print(gamma_decimal, epsilon_decimal)
print(total)

# it took me too fucking long to figure this out. Man, I need to get better
