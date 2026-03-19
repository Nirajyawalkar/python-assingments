# <<<<<< lab assignments1>>>>>.
# import numpy as np
#
# # a) Generate a 4x4 identity matrix
# identity_matrix = np.eye(4)
# print("--- 4x4 Identity Matrix ---")
# print(identity_matrix)
#
# # b) Generate two 3x3 matrices with random integers (1 to 9)
# # random.randint(low, high, size)
# matrix_a = np.random.randint(1, 10, size=(3, 3))
# matrix_b = np.random.randint(1, 10, size=(3, 3))
#
# print("\n--- Matrix A (3x3) ---")
# print(matrix_a)
# print("\n--- Matrix B (3x3) ---")
# print(matrix_b)
#
# # Perform Matrix Addition
# add_result = matrix_a + matrix_b
# print("\n--- Matrix Addition (A + B) ---")
# print(add_result)
#
# # Perform Matrix Multiplication (Dot Product)
# mult_result = np.dot(matrix_a, matrix_b)
# # Alternatively, you can use the @ operator: matrix_a @ matrix_b
# print("\n--- Matrix Multiplication (A * B) ---")
# print(mult_result)

#<<<<<< lab assignments2 >>>>>>>>>


# import numpy as np
#
# def get_matrix_input(rows, cols, name):
#     print(f"\nEnter elements for {name} ({rows}x{cols}):")
#     elements = []
#     for i in range(rows):
#         row = list(map(int, input(f"Enter row {i+1} ({cols} values separated by space): ").split()))
#         if len(row) != cols:
#             print(f"Error: You must enter exactly {cols} values.")
#             return None
#         elements.append(row)
#     return np.array(elements)
#
# # 1. Take input for 5x3 matrix
# matrix_5x3 = get_matrix_input(5, 3, "Matrix 1")
#
# # 2. Take input for 3x2 matrix
# matrix_3x2 = get_matrix_input(3, 2, "Matrix 2")
#
# if matrix_5x3 is not None and matrix_3x2 is not None:
#     # 3. Calculate Product Matrix
#     # (5x3) multiplied by (3x2) results in a (5x2) matrix
#     product_matrix = np.dot(matrix_5x3, matrix_3x2)
#
#     # 4. Print results
#     print("\n--- Product Matrix (5x2) ---")
#     print(product_matrix)
# else:
#     print("Failed to generate matrices due to incorrect input.")
