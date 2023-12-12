import random
from treap import *
import numpy as np
import csv
import statistics

N = 1000000

def generate_values(m, n):
    ratio = (n / m) ** (1 / (m - 1))
    result = [round((ratio ** i) * (i + 1)) for i in range(m)]
    return result

def generate_list(n, m):
    if n < m:
        raise ValueError("Number of distinct elements cannot be greater than the total number of elements.")

    distinct_elements = list(range(1, m+1))  # Generate m distinct elements
    duplicate_elements = [distinct_elements[random.randint(0, m-1)] for _ in range(n-m)]  # Generate duplicates

    result_list = distinct_elements + duplicate_elements
    random.shuffle(result_list)  # Randomize the list
    return result_list

def generate_a1(n):
    return [random.randint(1000000, 9999999) for _ in range(n)]

def generate_a2(n):
    return [(i % 50000) for i in range(n)]

def generate_a3(n):
    return [i for i in range(n)]

def generate_a4(n):
    return [50003 if i % 2 != 0 else i for i in range(n)]

def generate_a5(n):
    num_distinct = int(0.01*n)+1
    distinct_integers = list(range(1, num_distinct))
    non_distinct_integers = [random.randint(1, num_distinct-1) for _ in range(n-num_distinct)]
    final_list = distinct_integers + non_distinct_integers
    random.shuffle(final_list)
    return final_list

def generate_a6(n):
    unique_percentage = 0.001
    repeated_value = 42

    integer_list = [repeated_value] * n
    unique_indices = random.sample(range(n), k=int(n * unique_percentage))
    integer_list = [random.randint(1, 1000000) if i in unique_indices else repeated_value for i in range(n)]
    return integer_list

def count_distinct_elements(input_list):
    distinct_elements = set(input_list)
    return len(distinct_elements)

def measure_accuracy(n, m):
    return (1-abs((n-m)/n))*100

def write_to_csv(filename, data):
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['Buffer Size', 'Lowest Attempt', 'Highest Attempt','Med of 10', 'Num Distinct Elements', 'Accuracy', 'Lowest Accuracy', 'Highest Accuracy']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Check if the file is empty, and write the header only if needed
        if csvfile.tell() == 0:
            writer.writeheader()

        for row in data:
            writer.writerow(row)

def cvm_algorithm(stream, s):
    p = 1
    m = len(stream)
    B = 0
    root = None

    for t in range(m):
        a = stream[t]
        if search(root, a):
            root = deleteNode(root, a)
            B-=1
        
        u = random.random()
        if u >= p:
            pass
        elif B < s:
            root = insert(root, a, u)
            B+=1

        else:
            max_u = root.priority
            if u > root.priority:
                p = u
            else:
                root = deleteNode(root, root.key)
                root = insert(root, a, u)
                p = max_u
    return B/p

def analyze_stream(buffer_list, stream, tag):
    csv_filename = 'data_stream_analysis_'+tag+'.csv'

    for s in buffer_list:
        attempts = []
        for _ in range(10):
            attempts.append(cvm_algorithm(stream, s))
            attempts.sort()
        med = statistics.median(attempts)
        data_to_write = [{'Buffer Size': s, 'Num Distinct Elements': len(set(stream)), 'Lowest Attempt': attempts[0], 'Highest Attempt': attempts[-1], 'Med of 10': med, 'Accuracy': measure_accuracy(len(set(stream)), med), "Lowest Accuracy":measure_accuracy(len(set(stream)), attempts[0]), "Highest Accuracy":measure_accuracy(len(set(stream)), attempts[-1])}]
        write_to_csv(csv_filename, data_to_write)

#buffer_list_1M = [i*10+1 for i in range(1000)]
#buffer_list_10M = generate_values(50, N//1000)
#A1_STREAM = generate_a1(N)
#A2_STREAM = generate_a2(N)
#A3_STREAM = generate_a3(N)
#A4_STREAM = generate_a4(N)
#A5_STREAM = generate_a5(N)
#A6_STREAM = generate_a6(N)

#analyze_stream(buffer_list_1M, A1_STREAM, "A1_linear_buffer")
#analyze_stream(buffer_list_1M, A6_STREAM, "A6_linear_buffer")
#analyze_stream(buffer_list_10M, A2_STREAM, "B2")
#analyze_stream(buffer_list_10M, A3_STREAM, "B3")
#analyze_stream(buffer_list_10M, A4_STREAM, "B4")
#analyze_stream(buffer_list_10M, A5_STREAM, "B5")

print(generate_values(10, 500))
