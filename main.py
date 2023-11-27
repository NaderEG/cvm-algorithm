import random
import Treap

def generate_list(n, m):
    if n < m:
        raise ValueError("Number of distinct elements cannot be greater than the total number of elements.")

    distinct_elements = list(range(1, m+1))  # Generate m distinct elements
    duplicate_elements = [distinct_elements[random.randint(0, m-1)] for _ in range(n-m)]  # Generate duplicates

    result_list = distinct_elements + duplicate_elements
    random.shuffle(result_list)  # Randomize the list
    return result_list

def count_distinct_elements(input_list):
    distinct_elements = set(input_list)
    return len(distinct_elements)

def cvm_algorithm(stream, s):
    p = 1
    m = len(stream)
    B = {}

    for t in range(m):
        if t == m - 1:
            return len(B)/p
        a = stream[t]
        if a in B.keys():
            del B[a]
        
        u = random.random()
        if u >= p:
            pass
        elif len(B) < s:
            B[a] = u

        else:
            max_pair = max(B.items(), key=lambda x: x[1])
            if u > max_pair[1]:
                p = u
            else:
                del B[max_pair[0]]
                B[a] = u
                p = max_pair[1]


print("Enter the length of the data stream:")
l = int(input())
print("Enter the number of unique elements:")
d = int(input())

stream = generate_list(l, d)
print("Number of Distinct Elements:", d)
print("CVM Algorithm Prediction:", cvm_algorithm(stream, 1000))

