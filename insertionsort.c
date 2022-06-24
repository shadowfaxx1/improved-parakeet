#include<stdio.h>
#include<stdlib.h>


int main(){

    int ar[5]={4,2,5,1,3};
        int i ,j;

     for(i=0;i<5;i++)
     {   
         int k =ar[i];
          j=i-1;

          while(j>=0&&ar[j]>k)
          {
             
             ar[j+1]=ar[j];
             j--;
             

          } 
            
              ar[j+1]=k;


         } 


     
     for(i=0;i<5;i++)
     printf("%d",ar[i]);

}