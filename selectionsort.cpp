#include<bits/stdc++.h>
using namespace std;

#include<time.h>


void selection_sort(int ar[], int n){
   int i ,j;
  
   int min ;
   int temp;

   for(i=0;i<n;i++){
        min = i;
        for(j=i+1;j<n;j++)
        if(ar[min]>ar[j])
            min=j;
      temp =ar[min];
      ar[min]=ar[i];
      ar[i]=temp;

   }
}

void bubble_sort(int ar[],int n )
{
    int i ,j;
  
   int temp;
   for(i=0;i<n-1;i++)
   {
     for(j=0;j<n-i-1;j++)
     {
       if(ar[j]>ar[j+1])

      {
         temp=ar[j];
       ar[j]=ar[j+1];
        ar[j+1]=temp;
      }

     }
   }

}

void kaif(int ar[], int n ){

   int i ,j;
  
   int temp;
   for(i=1;i<n;i++)
   {
       for(j=i;j>0;j--)
       {
           if(ar[i]>ar[j])
           {
               temp=ar[i];
               ar[i]=ar[j];
               ar[j]=ar[i];

           }

       }


  
}
void insertion_sort(int ar [], int n )
{
     int i ,j;
      int k ;
      for(i=1;i<n;i++)
      {
          k=ar[i];
           j=i-1;
           while(j>=0 && ar[j] >k )
           {
               ar[j+1]=ar[j];
               j=j-1;

           }
         ar[j+1]=k;

      }

}

int main(){ 

  int ar[5]={5,3,2,1,6};
  int n=sizeof(ar)/sizeof(ar[0]);

  insertion_sort(ar,n);
  for(int i=0;i<n;i++)
  cout<<ar[i];


 
}