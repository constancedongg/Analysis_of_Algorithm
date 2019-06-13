

'''
Bloom filter consists of: 
1. an array B of n bits, initially all are set to 0.
2. k independent random hash functions h1, ... , hk witih range {0,1, ..., n-1}

Supports: insert(x), lookup(x)
'''

# map S into Bloom filter with n bits via hashing functions h1, h2, ..., hk with ranges [0, n-1]
# h stands for an array of dictionaries, i.e., h =[h1 , h2 , ... , hk]
def SetupBloomFilter(S, h , n):

    # Initialize B to all zeros
    B = [0 for i in range(n)]
    for i in range(len(S)):

        for k in range(len(h)):
            B[h[k][S[i]]] = 1
    return B


def lookup(B , x , h):
    for k in range(len(h)):
        if B[h[k][x]] == 0:
            return False
    return True

S = [6, 7, 8]
h = [{6:0 , 7:3 , 8:5 , 9 : 5} , {6:3, 7:4 , 8:5 , 9: 0} , {6:2 , 7: 3 , 8:5 , 9:4}]
n = 6
B = SetupBloomFilter(S,h,n)
print(B)
print(lookup(B,9,h))  # false positive, 9 is not in S, but all B[hi[9]] == 1, return True

h = [{6:0 , 7:3 , 8:5 , 9 : 1} , {6:3, 7:4 , 8:5 , 9: 0} , {6:2 , 7: 3 , 8:5 , 9:4}]
B = SetupBloomFilter(S,h,n)
print(lookup(B,9,h))  # B[h1[9]] = 0, since [6 , 7, 8] all don't map to value 1 in B, return False, 