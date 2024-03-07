import numpy as np


def row_echelon(A):
    """ Return Row Echelon Form of matrix A """    
    # if matrix A has no columns or rows,    
    # # it is already in REF, so we return itself 
    r, c = A.shape
    if r == 0 or c == 0:
        return A

    # we search for non-zero element in the first column
    for i in range(len(A)):
        if A[i, 0] != 0:
            break
    else:
        # if all elements in the first column is zero,
        # we perform REF on matrix from second column
        B = row_echelon(A[:, 1:])
        # and then add the first zero-column back
        return np.hstack([A[:, :1], B])

    # if non-zero element happens not in the first row,    # we switch rows
    if i > 0:
        ith_row = A[i].copy()
        A[i] = A[0]
        A[0] = ith_row

    # we divide first row by first element in it    
    A[0] = A[0] / A[0, 0]
    
    # we subtract all subsequent rows with first row (it has 1 now as first element)
    # multiplied by the corresponding element in the first column    
    A[1:] -= A[0] * A[1:, 0:1]

    # we perform REF on matrix from second row, from second column  
    B = row_echelon(A[1:, 1:])

    # we add first row and first (zero) column, and return
    return np.vstack([A[:1], np.hstack([A[1:, :1], B])])





n = int(input())
inp = np.zeros((n, n+1), dtype= float)

for i in range(n):
    l = input()
    inp[i] = np.array([int(k) for k in l.split()])




I = np.identity(n, dtype = float)
A = inp[:, :n].copy()
b = inp[:, n:].copy()


m = row_echelon(np.hstack([A, I]))
m = np.rot90(np.rot90(m))
B = np.zeros((m.shape[0], m.shape[1]))


B[:, :n] = m[:, n:]
B[:, n:] = m[:, :n]

Br = row_echelon(B)
B = np.rot90(np.rot90(Br[:, n:]))
if np.array_equal(Br[:, :n], I):
    print(np.array2string(np.sort(np.reshape(np.round(B @ b).astype(np.int32), (n)))))
    print(np.array2string(np.round(B, 2)))
else:
    print('no unique solution')