
def vector_size_check(*vector_variables):
    result = [ True if len(vector_variables[i]) == len(vector_variables[i + 1]) else False for i in range(0, len(vector_variables) - 1)]
    return  False not in result 
"""
    for i in range(0, len(vector_variables) - 1) :
        if len(vector_variables[i]) != len(vector_variables[i+1]) :
          return False
        return True
"""

def vector_addition(*vector_variables):
    ans = []
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
    else:
        for a in zip(*vector_variables):
            ans.append(sum(a))
        return ans


def vector_subtraction(*vector_variables):
    ans = []
    mid = 0
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError
    else:
        for i in zip(*vector_variables):
            for j in i:
                mid -= j
            ans.append(mid + 2 * i[0])
            mid = 0
    return ans


def scalar_vector_product(alpha, vector_variable):
    ans = []
    for char in vector_variable:
      ans.append(alpha * char)
    return ans


def matrix_size_check(*matrix_variables):
    lens = []
    for i in matrix_variables:
        for j in i:
            lens.append(j)
    if len(lens) / len(matrix_variables) != len(matrix_variables[0]):
        return False
    else:
        return True


def is_matrix_equal(*matrix_variables):
    for i in range(0,len(matrix_variables) - 1):
        if matrix_variables[i] != matrix_variables[i + 1]:
            return False
        else:
            return True

def matrix_addition(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    else:
        pre_result = []
        result = []
        for i in zip(*matrix_variables):
            for k in zip(*i):
                pre_result.append(sum(k))
            result.append(pre_result)
            pre_result = []    
    return result


def matrix_subtraction(*matrix_variables):
    mid = []
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError
    else:
        for i in zip(*matrix_variables):
            mid += vector_subtraction(*i)
        ans = [mid[i:i+len(matrix_variables[0][0])] for i in range(0, len(mid), len(matrix_variables[0][0]))]
        return ans


def matrix_transpose(matrix_variable):
    mid = []
    for vec in zip(*matrix_variable):
        for i in vec:
            mid.append(i)
    result = [mid[i:i+len(matrix_variable)] for i in range(0, len(mid), len(matrix_variable))]
    return result


def scalar_matrix_product(alpha, matrix_variable):
    mid = []
    for vec in matrix_variable:
        mid += scalar_vector_product(alpha, vec)
    ans = [mid[i:i+len(matrix_variable[0])] for i in range(0, len(mid), len(matrix_variable[0]))]
    return ans


def is_product_availability_matrix(matrix_a, matrix_b):
    if len(matrix_a[0]) == len(matrix_b):
      return True
    else:
      return False


def matrix_product(matrix_a, matrix_b):
    mid = []
    pre_result = []
    result = []
    if is_product_availability_matrix(matrix_a, matrix_b) == False:
        raise ArithmeticError
    else:
        for garo in matrix_a:
            for sero in zip(*matrix_b):
                for x, y in zip(garo, sero):
                    mid.append(x * y)
                pre_result.append(sum(mid))
                mid = []
            result.append(pre_result)
            pre_result = []
        return result