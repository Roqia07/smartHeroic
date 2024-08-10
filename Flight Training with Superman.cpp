#include <bits/stdc++.h>
using namespace std;

int main() {
     int noFlights;
    cin>>noFlights;

    int heights[noFlights];
    for (int i=0; i<noFlights;i++){
        cin>>heights[i];
    }  
    int maxno=heights[0];
    for (int i=1; i<noFlights;i++){
        maxno=max(heights[i],maxno);
    }

    cout<<maxno;
    return 0;
}