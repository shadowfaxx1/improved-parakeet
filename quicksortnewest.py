import random
import time
import matplotlib.pyplot as plt

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        
        while low <= high and array[high] >= pivot:
            high = high - 1

        
        while low <= high and array[low] <= pivot:
            low = low + 1

        
        if low <= high:
            array[low], array[high] = array[high], array[low]
           
        else:
           
            break

    array[start], array[high] = array[high], array[start]

    return high


def quicksort(ar,l,h):
    if len(ar)==1:
        return ar
    if(l<h):
        j=partition(ar,l,h)
        quicksort(ar,l,j)
        quicksort(ar,j+1,h)


def mean(a):
    return sum(a) / len(a)

def test():
    g_list_x = []


    find_all_list_y = []

    random_lists = []
    sorted_list_y = []
    worst_list_y = []
    range_num = 2000

    for one_list in range(15):
        random_lists.append([])
        for x in range(range_num):
            random_lists[one_list].append(random.randint(1, 1001))
        range_num += 2000
        g_list_x.append(len(random_lists[one_list]))

    for one_item in range(15):
        sorted_list_y.append(sorted(random_lists[one_item]))

    for one_item in range(15):
        worst_list_y.append(sorted(random_lists[one_item], reverse=True))

    for i in range(50):
        g_list_y = []
        for one_item in range(15):
            ar_pass = random_lists[one_item][:]
            start =time.perf_counter()
            quicksort(ar_pass,0,len(ar_pass)-1)
            elapsed = (time.perf_counter() - start)

            g_list_y.append(elapsed)

        find_all_list_y.append(g_list_y)


    final_avg_list_y = list(map(mean, zip(*find_all_list_y)))

    plt.xlabel('number of N ')
    plt.ylabel('Time Taken')
    plt.plot(g_list_x, final_avg_list_y, label=' Cases')
    plt.grid()c 
    plt.legend()
    plt.show()

if __name__ == '__main__':

    test()
