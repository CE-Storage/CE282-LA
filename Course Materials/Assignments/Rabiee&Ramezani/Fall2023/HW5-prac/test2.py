import numpy as np
def test_QR(student_qr,scipy_qr,unify_signs):
  sizes = [(5,8),(4,4),(10,10),(16,20)]
  for i in range(4):
    M = np.random.rand(sizes[i][0],sizes[i][1])
    a = unify_signs(student_qr(M))
    b = unify_signs(scipy_qr(M))
    if np.isclose(a[0].all(),b[0].all()) and np.isclose(a[1].all(),b[1].all()):
      print(f"Test{i+1}: \033[32mPassed!\033[0m")
    else:
      print(f"Test{i+1}: \033[31mFailed!\033[0m")