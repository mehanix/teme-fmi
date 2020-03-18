from datetime import datetime
import math
import random
def time_elapsed(start_time, sort_time):
    return sort_time - start_time

#### BUBBLE SORT ####

def bubble_sort(input):
    ## verific conditii ##
    if len(input) > 9999:
        return ["input size too large (too many numbers)"]


    ## iau timp start ##
    start_time = datetime.now()
    ## sortare ##
    ok = 0
    while ok == 0:
        ok = 1
        for i in range(len(input)-1):
            if input[i] > input[i+1]:
                input[i],input[i+1] = input[i+1],input[i]
                ok = 0
    sort_time = datetime.now()
    return input,time_elapsed(start_time,sort_time)

#### END BUBBLE SORT ####




#### COUNT SORT ####

def count_sort(input):

    ## gasit capat exterior #
    if input == ['']:
        return [''],0

    max_nr = max(input)
    ## verificari ##
    if max_nr > 500000:
       return ["numbers too large to sort with count sort (max nr: "+str(max_nr)+")"]

    ## algo sortare ##

    ## iau timp start ##
    start_time = datetime.now()

    v = [0 for x in range(max_nr+1)]

    for x in input:
        v[x]+=1
    ## recompunere vector ##
    output = [0 for x in input]

    index = 0
    for i in range(len(v)):
        for _ in range(v[i]):
            output[index] = i
            index+=1
    #print(output)

    end_time = datetime.now()
    return output,time_elapsed(start_time,end_time)


#### END COUNT SORT ####




#### MERGE SORT ####

def merge(left,right):
    new = [ 0 for x in range(len(left)+len(right)) ]
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new[k] = left[i]
            i += 1
        else:
            new[k] = right[j]
            j += 1
        k+=1

    while i < len(left):
        new[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        new[k] = right[j]
        j += 1
        k += 1
    return new



def merge_sort(input):
    if len(input) == 1:
        return input

    mid = len(input)//2
    left = merge_sort(input[:mid])
    right = merge_sort(input[mid:])
    return merge(left, right)




def merge_sort_wrapper(input):
    ## wrapper merge sort, pentru verificari inainte de rularea algoritmului efectiv, pt ca e fct recursiva ##
    if input == ['']:
        return [''], 0

    start_time = datetime.now()
    output =  merge_sort(input)
    end_time = datetime.now()

    return output, time_elapsed(start_time,end_time)

#### END MERGE SORT ###






#### RADIX SORT ####

def count_sort_radix(input,digit,base):
    output = [0] * (len(input))  # vector output (aici reconstruiesc vectorul)
    count = [0] * (base)

    for nr in input:
          
        index = (nr // base**digit ) % base  # scot cifra exp din fiecare nr
        count[index] += 1 # o numar
    #pt fiecare cifra, calculez pozitia in vectorul nou
    for i in range(1, base):
        count[i] += count[i - 1]
    #print(count[:8])
    # construiesc output-ul, mergand descrescator
    for i in range(len(input) - 1, -1, -1):
        # scot cifra
        index = (input[i] // base**digit) % base
     
        # plasez numarul in vectorul nou pe pozitia determinata de count
        output[count[index] - 1] = input[i]
           # scad count-ul
        count[index % base] -= 1
    #print(output)
    return output



def radix_sort(input, base):
    if input == ['']:
        return [''], 0
    start_time = datetime.now()

    max_nr = max(input) # nr pt aflat nr maxim de cifre
    output = input
    digits = int(math.floor(math.log(max_nr,base)+1))

    for i in range(digits):
        output = count_sort_radix(output, i, base)

    end_time = datetime.now()
    return output, time_elapsed(start_time,end_time)

#### END RADIX SORT ####










##### QUICK SORT ####

# quicksort are nevoie de vector global pt sorting in-place
input_q = []
calls = 0

def quick_sort_wrapper(input): 
    # wrapper quick sort, pt verificari conditii
    #  inainte de intrat in fct recursiva
    if input == ['']:
        return [''], 0

    global input_q
    input_q = input
    #print(input)
    n = len(input_q)
    start_time = datetime.now()
    input_q = quick_sort(input)
    end_time = datetime.now()

    return input_q, time_elapsed(start_time,end_time)



def quick_sort(input_q:list):
    if len(input_q) <= 1:
        return input_q
    pivot = input_q[-1]
    '''    #mediana din 3
    center = len(input_q) // 2 # iau elem din mijloc

    # pun start, center, end la locurile lor
    median_of_3 = [input_q[0], input_q[center], input_q[-1]]

    median_of_3.sort()
    input_q[0] = median_of_3[0]
    input_q[center] = median_of_3[1]
    input_q[2] = median_of_3[2]
    pivot = median_of_3[1]'''
    small = [i for i in input_q if i < pivot]
    eq = [i for i in input_q if i == pivot]
    big = [i for i in input_q if i > pivot]
    return quick_sort(small) + eq + quick_sort(big)

#### END QUICK SORT ####
