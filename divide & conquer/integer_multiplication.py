
'''
If directly solve by mulitplication, O(n^2)
Better way: x = x_H * 10^(n/2) + x_L , y = y_H * 10^(n/2) + y_L
Instead of calculating 4 terms, compute (x_H + X_L) * (y_H + y_L) - x_H * y_H - x_L * y_ L for x_H * y_L + x_L * y_H
in total, multiply 3 times
T(n) = 3 * T(n/2) + cn, a = 3 , b = 2 , k = 1 ,
Time complexity: O(n^log2(3))

'''
# input x and y are two strings, suppose x and y have the same length
def integer_multiplication(x , y):
    n1 = len(x)
    n1_half = n1 // 2
    x_h = x[ : n1_half]
    x_l = x[n1_half : ]
    y_h = y[ : n1_half]
    y_l = y[n1_half : ]
    if n1 > 1 :
        tmp1 = integer_multiplication(x_h , y_h)
        tmp3 = integer_multiplication(x_l , y_l)
        tmp2 = integer_multiplication(x_h + x_l , y_h + y_l) - tmp1 - tmp3
        return tmp1 * 10 ** n1 + tmp2 * 10 ** (n1_half) + tmp3
    else:
        return int(x) * int(y) 

print(integer_multiplication('123','456'))
