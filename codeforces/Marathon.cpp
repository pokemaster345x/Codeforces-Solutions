#include <bits/stdc++.h>
using namespace std;
int as[4],t,aux;
int main(){

    cin>>t;
    for(int i=0;i<t;i++){
        aux=0;
        cin>>as[0]>>as[1]>>as[2]>>as[3];
        for(int x=0;x<4;x++){
            if(as[0]<as[x]){
                aux++;
            }
        }
        cout<<aux<<endl;
    }
    return 0;

}