import random
from treap import *
import numpy as np
import csv
import statistics

N = 1000000
buffer_size_list = [1, 5, 10, 25, 50, 75, 100, 250, 500, 750, 1000, 2500, 5000, 7500, 10000, 25000, 50000, 75000, 100000, 250000, 500000, 750000, 1000000]


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
    return np.random.normal(0, 1, n)

def count_distinct_elements(input_list):
    distinct_elements = set(input_list)
    return len(distinct_elements)

def measure_accuracy(n, m):
    return (1-abs((n-m)/n))*100

def write_to_csv(filename, data):
    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['Buffer Size', 'Med of 10', 'Num Distinct Elements', 'Accuracy']
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
        if t == m - 1:
            return B/p
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


def analyze_stream(stream, tag):
    csv_filename = 'data_stream_analysis_'+tag+'.csv'

    for s in buffer_size_list:
        attempts = []
        for _ in range(10):
            attempts.append(cvm_algorithm(stream, s))
        med = statistics.median(attempts)
        data_to_write = [{'Buffer Size': s, 'Num Distinct Elements': len(set(stream)), 'Med of 10': med, 'Accuracy': measure_accuracy(len(set(stream)), med)}]
        write_to_csv(csv_filename, data_to_write)

A1_STREAM = generate_a1(N)
A2_STREAM = generate_a2(N)
A3_STREAM = generate_a3(N)
A4_STREAM = generate_a4(N)
A5_STREAM = generate_a5(N)
A6_STREAM = generate_a1(10*N)
A7_STREAM = generate_a2(10*N)
A8_STREAM = generate_a3(10*N)
A9_STREAM = generate_a4(10*N)
A10_STREAM = generate_a5(10*N)

analyze_stream(A1_STREAM, "A1")
analyze_stream(A2_STREAM, "A2")
analyze_stream(A3_STREAM, "A3")
analyze_stream(A4_STREAM, "A4")
analyze_stream(A5_STREAM, "A5")
analyze_stream(A6_STREAM, "A6")
analyze_stream(A7_STREAM, "A7")
analyze_stream(A8_STREAM, "A8")
analyze_stream(A9_STREAM, "A9")
analyze_stream(A10_STREAM, "A10")