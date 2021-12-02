'''
--- Day 2: Dive! ---

'''

# beginning file opening protocol of read bits and get an handle of said bits.
fhand = open('input.txt')

profundo = 0
horizon_length = 0
aim = 0

for line in fhand:
    # parsing the instructions...  bzzt
    line = line.rstrip()
    line = line.split()

    # order and distance to travel... bzzt
    movement = line[0]
    scale_movement = int(line[1])

    # moving ship.. humm.. submarine in X-axis (horizon_length) and in the other axis which is Y (profundo)... bzzt
    if movement == 'forward':
        horizon_length += scale_movement
        profundo = profundo + (scale_movement * aim)

    # TAKE AIM TO KILL THE ENEMY!!! ups, I meant, take aim to then move submarine (maybe is yellow) in Y... and bzzt also
    elif movement == 'up':
        aim -= scale_movement
    elif movement == 'down':
        aim += scale_movement

total = horizon_length * profundo
print(total)