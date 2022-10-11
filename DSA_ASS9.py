"""
Write a python program to compute following computations on matrix 
1) Addition of two matrices 
2) Subtraction of two matrices
3) Multiplication of two matrices
4) Transpose of a matrix 
"""
def main():
    print("Hello")
    A = []
    B = []
    print("Enter A Matrix")
    r1,c1,A = read_matrix(A)
    display_matrix(r1,c1,A)

    print("Enter B Matrix")
    r2,c2,B = read_matrix(B)
    display_matrix(r2,c2,B)

    print("The Addition of matrix A & B ")
    matrix_addition(A,B,r1,c1,r2,c2)

    print("The Subtraction of matrix A & B ")
    matrix_subtraction(A,B,r1,c1,r2,c2)

    print("The Transpose of A Matrix")
    matrix_transpose(r1,c1,A)

    print("The Transpose of B Matrix")
    matrix_transpose(r2,c2,B)

#For Addition
def matrix_addition(A,B,r1,c1,r2,c2):
    C=[]
    if (r1 == r2 and c1 == c2):
        for i in range (r1):
            L1 =[]
            for j in range (c1):
                x = (A[i][j]+B[i][j])
                L1.append(x)
            C.append(L1)
        display_matrix(r1,c1,C)
    else:
        print("Addition not possible")

#For Substraction
def matrix_subtraction(A,B,r1,c1,r2,c2):
    C=[]
    if (r1 == r2 and c1 == c2):
        for i in range (r1):
            L1 =[]
            for j in range (c1):
                x = (A[i][j]-B[i][j])
                L1.append(x)
            C.append(L1)
        display_matrix(r1,c1,C)
    else:
        print("Subtraction not possible")

#For Transpose
def matrix_transpose(r,c,z):
    for i in range (c):
        for j in range (r):
            print(z[j][i],end =" ")
        print("\n")

# For Input
def read_matrix(z):
    r = int (input("Enter the number of rows : "))
    c = int (input("Enter the number of columns :"))

    for i in range (r):
        L1 = []
        for j in range (c):
            x = int (input("Enter the values : "))
            L1.append(x)
        z.append(L1)
    return r,c,z

# For Display 
def display_matrix(r,c,z):
    for i in range (r):
        for j in range (c):
            print(z[i][j],end= " " )
        print("\n")
         



main()


