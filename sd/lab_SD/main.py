from pathlib import Path
from printing import print_result
from sorting_algorithms import bubble_sort, merge_sort_wrapper, count_sort, quick_sort_wrapper, radix_sort
import random 
import sys
def read_tests(path):
    tst = Path(path).read_text().split('\n')

    for t in range(len(tst)):
        try:
           tst[t] = [int(x) for x in tst[t].split(' ')]
        except:
            tst[t] = ['']

    return tst


def read_test_data(path):
    tst = Path(path).read_text().split('\n')

    for t in range(len(tst)):
        try:
            tst[t] = [int(x) for x in tst[t].split(' ')]
        except:
            tst[t] = ['']

    return tst


#### Initializare ####

test_data = read_test_data("tests.txt")
test_count = test_data[0][0]
for i in range(1,test_count+1):
    n = test_data[i][0]
    v_max = test_data[i][1]
    test = [0] * n
    for j in range(n):
        test[j] = random.randrange(v_max+1)
    print("TEST ", i, "============================================================= NR_ELEM:",n,"=====" )
    test_count+=1
    out = []

    ## bubble sort ##
    test_copy = test.copy()
    out = bubble_sort(test_copy)
    test_copy = test.copy()
    print_result("Bubble Sort", out, test_copy)

    ## count sort ##
    test_copy = test.copy()
    out = count_sort(test_copy)
    print_result("Count Sort",out,test.copy())

    ## merge sort ##
    test_copy = test.copy()
    out = merge_sort_wrapper(test_copy)
    print_result("Merge Sort", out, test.copy())

    ## radix sort ##
    test_copy = test.copy()
    out = radix_sort(test_copy,256)
    print_result("Radix Sort",out,test.copy())

    ## "quick" sort ##
    test_copy = test.copy()
    out = quick_sort_wrapper(test_copy)
    print_result("Quick Sort",out, test.copy())

    print() #spacing
