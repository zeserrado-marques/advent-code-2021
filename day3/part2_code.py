'''
--- Day 3: Binary Diagnostic ---

Oxygen and CO2 rating

'''

def removeItemsFromList(lista: list, condition):
    delete_counter = 0
    for index in range(len(lista)):
        elemento = lista[index-delete_counter]
        if elemento == condition:
            lista.pop(index-delete_counter)
            delete_counter+=1
    return lista


#fhand = open('input.txt')
fhand = open('test.txt')

num_list = list()

# insert file into an nparray
for line in fhand:
    line = line.rstrip()
    a = [int(i) for i in line]
    #print(a)
    num_list.append(a)


col_size = range(len(a))
row_size = range(len(num_list))

for i in col_size:
    zero_count = 0
    one_count = 0
    for j in row_size:
        current_bit = num_list[j][i]
        if current_bit == 1:
            one_count += 1
        else:
            zero_count += 1
    print(one_count, zero_count)

    # list with numbers to be removed
    if one_count >= zero_count:
        ola = num_list[:]
        for number_index in range(len(num_list)):
            
            number = num_list[number_index]
            current_coluna = number[i]
            if current_coluna == 0:
                ola.pop(i)
                
        break

print(ola)