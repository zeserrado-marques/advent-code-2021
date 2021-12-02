'''
--- Day 2: Dive! ---

'''

fhand = open('input.txt')

profundo = 0
horizon_length = 0

for line in fhand:
    # trimming the line
    line = line.rstrip()
    line = line.split()
    
    # order and distance to travel
    movement = line[0]
    scale_movement = int(line[1])

    # adds the distance to travel (scale_movement) depending on the order (movement) 
    if movement == 'forward':
        horizon_length += scale_movement
    elif movement == 'up':
        profundo -= scale_movement
    elif movement == 'down':
        profundo += scale_movement
    
    #print(line, profundo)

total = horizon_length * profundo
print(total)
