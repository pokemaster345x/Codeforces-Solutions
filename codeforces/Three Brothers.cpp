#include <bits/stdc++.h>
using namespace std;

int a,b;
int main(){
    cin>>a>>b;
    /*brute force
    if(a==1&&b==2|| a==2 &&b==1){
        cout<<3;
    }else if(a==1 && b==3|| a==3 &&b==1){
        cout<<2;
    }else if(a==2 &&b==3|| a==3 && b==2){
        cout<<1;
    }*/
    //math  form
    cout<<6 - (a+b);
}