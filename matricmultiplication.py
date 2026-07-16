# matrix multiplication for 3 * 3 matrix
import numpy as np
import pandas as pd
def matrixmultiplication(a11, a12, a13, a21, a22, a23, a31, a32, a33, b11, b12, b13, b21, b22, b23,b31,b32,b33):
    matrix_1 = np.array([[a11,a12 ,a13], [a21, a22, a23], [a31,a32,a33]])
    matrix_2 = np.array([[b11, b12, b13], [b21, b22, b23], [b31, b32, b33]])
    result = np.matmul(matrix_1, matrix_2)
# print(result)            no clean  look while directly print result so using pandas to have a proper format
    df = pd.DataFrame(result, columns=['Column 1', 'Column 2','Column 3'], index=['Row 1', 'Row 2','Row 3'])
    print(df)


def main():
    print("enter value for first matrix: ")
    a11 = int(input("enter the value: "))
    a12 = int(input("enter the value: "))
    a13 = int(input("enter the value: "))
    a21 = int(input("enter the value: "))
    a22 = int(input("enter the value: "))
    a23 = int(input("enter the value: "))
    a31 = int(input("enter the value: "))
    a32 = int(input("enter the value: "))
    a33 = int(input("enter the value: "))
    print("enter value for second matrix: ")
    b11 = int(input("\n enter the value: "))
    b12 = int(input("enter the value: "))
    b13 = int(input("enter the value: "))
    b21 = int(input("enter the value: "))
    b22 = int(input("enter the value: "))
    b23 = int(input("enter the value: "))
    b31 = int(input("enter the value: "))
    b32 = int(input("enter the value: "))
    b33 = int(input("enter the value: "))
    matrixmultiplication(a11,a12, a13, a21, a22, a23, a31, a32, a33, b11, b12, b13, b21, b22, b23,b31,b32,b33)
main()