#include <bits/stdc++.h>
using namespace std;

bool search(int n,float arr[], float target){    // searches for the target
    bool found=false;
    for(int i=0;i<n;i++)
    {
        if(arr[i]==target) {
           cout<<i<<" "; //prints the indecies of the target is it is repeated in the array
          found= true;
        }
    }
    return found;
}

int main()
{
    int n; //no of elements
    cin>>n;
    float arr[n]; 
    for(int i=0; i<n;i++){
        cin>>arr[i]; //takes array elements
    }
    float target;
    cin>>target; //takes search target
    bool out = search(n,arr,target); //calls the search function
    if(out==false){  
        cout<<"-1";   //prints if the target isn't found
    }
   return 0; 
}
