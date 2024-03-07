import numpy as np
def test_lu(studentlu):
  sizes = [(5,5),(10,10),(4,4)]
  for i in range(len(sizes)):
    M = np.random.rand(sizes[i][0],sizes[i][1])
    print(f"Test {i+1}:", end=" ")
    L, U = studentlu(M)
    lowert = np.allclose(L, np.tril(L))
    if not lowert:
      print("\033[31mFailed!\033[0m : L is not lower triangular")
    else:
      uppert = np.allclose(U, np.triu(U))
      if not uppert:
        print("\033[31mFailed!\033[0m : U is not upper triangular")
      else:
        equality = np.allclose(L@U,M)
        if not equality:
          print("\033[31mFailed!\033[0m : L@U != the matrix")
        else:
          print("\033[32mPassed!\033[0m")
    print("---------------")