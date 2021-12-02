'''
--- Day 1: Sonar Sweep ---

count the number of times a depth measurement increases, but with sliding window of size (sw_size) = 3.

'''

fhand = open('input.txt')

# initialize
depths = list()
count = 0
mais_grande_counter = 0
sw_size = 3

for line in fhand:
    count += 1
    current_depth = int(line.rstrip())
    depths.append(current_depth)

    if len(depths) == sw_size + 1:
        # print(depths)
        # print(depths[:sw_size], depths[1:])
        # print(sum(depths[:sw_size]), sum(depths[1:]))
        if sum(depths[:sw_size]) < sum(depths[1:]):
            mais_grande_counter += 1
        depths.pop(0)
    
print(depths)
print(mais_grande_counter)
