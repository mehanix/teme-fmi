from datetime import datetime

def get_native_sort_time(input):
    st_time = datetime.now()
    input.sort()
    end_time = datetime.now()
    return end_time - st_time


def output_is_valid(output):
    for i in range(len(output) - 1):
        if output[i] > output[i+1]:
            return False
    return True

def print_failure(sort_name, msg):
    print(sort_name, " FAILURE ----- Error: ", msg)
    return 0

def print_success(sort_name, sort_time, native_time):
    print(sort_name, " SUCCESS ----- Sort time: ", sort_time, " ----- Native time: ", native_time)


def print_result(sort_name, out, test):
    if len(out) == 1:
        print_failure(sort_name,out[0]) # printeaza eroare returnata de sortare
    else:
        output, sort_time = out # verific daca sortarea e corecta (output = native sort output)
        if output_is_valid(output) == True:
            native_time = get_native_sort_time(test)
            print_success(sort_name,  sort_time, native_time  )
        else:
            print_failure(sort_name, "Incorrect result! :(")



