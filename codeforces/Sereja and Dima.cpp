#include <bits/stdc++.h>
using namespace std;
#ifdef LOCAL
#include "algo/debug.h"
#else
#define debug(...) 42
#endif
int n,outputs[2]={0,0},x=0,y,z,maxi=0;
int main(){
    cin>>n;
    int s[n];
    y=0;
    z=n-1;
    for(int i=0; i<n;i++){
        cin>>s[i];
    }  
    for(int i=0;i<n;i++){
        maxi=max(s[y],s[z]);
        if(maxi==s[y]){
            y++;
        }else{
            z--;
        }
        outputs[x]+=maxi;
        x=(x+1)%2;

    }
    cout<<outputs[0]<<" "<<outputs[1];
    return 0;
}