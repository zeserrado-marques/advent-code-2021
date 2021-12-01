'''
--- Day 1: Sonar Sweep ---

count the number of times a depth measurement increases

'''

fhand = open('input.txt')

# initialize
depths = list()
count = 0
mais_grande_counter = 0

for line in fhand:
    count += 1
    depth_value = int(line.rstrip())
    depths.append(depth_value)

    if len(depths) == 2:
        #print(depths)
        if depths[0] < depths[1]:
            mais_grande_counter += 1
            #print('ouga bouga')
        depths.pop(0)

print(mais_grande_counter)
