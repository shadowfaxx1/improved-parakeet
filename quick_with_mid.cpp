#include<bits/stdc++.h>

using namespace std;


int partition(int ar[],int l,int h){
      
    int mid =(l+h)/2;
   
     int piv=ar[l];
     int i,j;
     i=l;
     j=h;
  

     while(i<j){
         do{
             i++;
         }while(ar[i]<=piv);
         do{
             j--;

         }while(ar[j]>piv);

         if(i<j)
         {
            
       int temp=ar[i];
       ar[i]=ar[j];
       ar[j]=temp;
         }
     }
     int t=piv;
     piv=ar[j];
     ar[j]=t;
     return j ;

}
void quicksort(int ar [] ,int l ,int h)
{
     
    
    if(l<h)
    {
        int p=partition(ar,l,h);
        quicksort(ar,l,p);
        quicksort(ar,p+1,h);

    }
}


int main () 
{   int n=6; 
    int ar[n]={4,13,11,2,3,9};
    quicksort(ar,0,n);
    for(int i =0;i<n;i++)
    cout<<" "<< ar[i];

}