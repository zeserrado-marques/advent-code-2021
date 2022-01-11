# verificar se o bingo está certo
import numpy as np

def verifyBingo(lst: np.ndarray):
    rows, cols = lst.shape
    for i in range(rows):
        print(f'current row = {lst[i,:]}')
        print(f'current col = {lst[:,i]}')

        if 0 not in lst[i,:]:
            print('BINGO in the row!!!!!!!')
        elif 0 not in lst[:,i]:
            print('BINGO in the column!!!!!')
        else:
            print('no bingo :(')


l1 = np.zeros((5,5), dtype=np.int8)
l2 = np.zeros((5,5), dtype=np.int8)
l3 = np.zeros((5,5), dtype=np.int8)

l1[0,:] = 1
l2[:,2] = 1
l3[3,0:4] = 1


print(l2)

verifyBingo(l2)
