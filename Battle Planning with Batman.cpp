#include <bits/stdc++.h>
using namespace std;

void compare(int justice[][10],int villains[][10],int r,int c){
    int justWins=0,villainsWins=0,ties=0;
    for (int i=0; i<r;i++){
        for(int j=0; j<c;j++){
            if(justice[i][j]>villains[i][j]){        //compares which array is higher for each element 
                justWins++;
            }
            else if(justice[i][j]<villains[i][j]){
                 villainsWins++;
            }
            else {
                 ties++;
            }
        }
    }
    if(justWins>villainsWins){                      //compares which team has higher total numbers and prints it out
    cout<< "Justice League";
    }
    else if(justWins<villainsWins){
    cout<< "Villains";
    }
    else{
    cout<<"Tie";
    }

}
   
int main(){
int r,c;
cin>> r; //no. of rows
cin>>c; //no. of columns
int justiceLeague[r][10],villains[r][10]; //justice league elements
for (int i=0; i<r;i++){
    for(int j=0; j<c;j++){
        cin>>justiceLeague[i][j];
    }
}
for (int i=0; i<r;i++){ // villains elements
    for(int j=0; j<c;j++){
        cin>>villains[i][j];
    }
}
compare(justiceLeague,villains,r,c); //calling comparison function
 
    return 0;
}