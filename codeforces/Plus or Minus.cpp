#include <iostream>

using namespace std;
int a,b,c,t;
void solve(int a,int b,int c){
    if(a+b==c){
        cout<<"+"<<endl;
    }else{
        cout<<"-"<<endl;
    }
}
int main(){
    cin>>t;
    while(t--){
        cin>>a>>b>>c;
        solve(a,b,c);
    }
    return 0;
}