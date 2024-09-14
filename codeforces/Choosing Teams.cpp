#include <iostream>
using namespace std;
int n,k,cont=0;

int main(){
    cin>>n>>k;
    int aux;
    for(int i=0;i<n;i++){
        cin>>aux;
        if(aux+k<=5){
            cont+=1;
        }
    }
    cout<<cont/3<<endl;
}