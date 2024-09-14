#include <iostream>
#include <algorithm>
 using namespace std;
 int main(){
    int n,as[3];
    cin >>n;
    for(int i=0;i<n;i++){
        cin>>as[0]>>as[1]>>as[2];
        sort(as,as+3);
        if (as[0]+as[1]==as[2]){
            cout<< "YES"<<endl;
        }else{
            cout << "NO"<<endl;
        }
    }
    return 0;
 }