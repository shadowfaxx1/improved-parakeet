from copyreg import add_extension
from platform import architecture
import time 
import random 
import matplotlib.pyplot as plt 

def selectionSort(ar):

   for i in range(len(ar)):

     
       min = i

       for j in range(i+1, len(ar)):
           if ar[min] > ar[j]:
               min = j

       temp = ar[i]
       ar[i] = ar[min]
       ar[min] = temp
   return ar


