import random 
import matplotlib.pyplot as plt 
import time 

def test_selection_Sort():
    worst_list=[]
    best_list=[]
    avg_list=[]

    g_graph_x=[]
    g_graph_y=[]
    random_list=[]

    r=2000

    for list_s in range(10):
        random_list.append([])
        for i in range(r):
            random_list[list_s].append(random.randint(1,1001))
        r=r+2000



if __name__ == '__main__': 
    test_selection_Sort()
