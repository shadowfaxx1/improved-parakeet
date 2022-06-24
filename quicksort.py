
def print(ar):
    for i in range(ar):
        print(i)


def swap(ar,i,j):
     temp=ar[i]
     ar[i]=ar[j]
     ar[j]=ar[i]


def partition(ar,l,h):
    
    i=l
    j=h
    piv=ar[(l+h)//2]
    print(piv)
    while(i<h):
        while(ar[i]>=piv):
            i=i+1
        while(ar[j]<=piv):
            j=j-1
        if(i<j):
            swap(ar,i,j)
           
    swap(ar,l,j)
    return j 




def quicksort(ar,l,h):
    if(l<h):
        j=partition(ar,l,h)
        quicksort(ar,l,j)
        quicksort(ar,j+1,h)





n=int(input())
ar=list(map(int,input().split()[:n]))
l=0
h=n-1
quicksort(ar,l,h)
print(ar)

