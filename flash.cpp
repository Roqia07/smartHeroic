#include <bits/stdc++.h>
using namespace std;

int sumtask(int n)
{
return n*(n+1)/2;
}
int main()
{

    int n,k;
    cin>>n>>k;
    int time=240-k;
    int start=0, end =n, mid;
    while(start<end){
        mid=(start+end+1)/2;
        if(sumtask(mid)*5<=time){
            start=mid;}
        else{
            end=mid-1;
        }
        
    }
    cout<<start<<endl;
return 0;
}