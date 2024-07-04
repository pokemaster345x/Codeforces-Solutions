#include <iostream>
 using namespace std;
int main () {
    int n,k,l,c,d,p,nl,np,drink,toasts,limes,s[3],min;
    cin >>n;
    cin >>k;
    cin >>l;
    cin >>c;
    cin >>d;
    cin >>p;
    cin >>nl;
    cin >>np;
    drink=k*l;
    
    s[0]=(drink/nl)/n;
    s[1]=(c*d)/n;
    s[2]=(p/np)/n;
    min=s[0];
    for(int x=0;x<3;x++){
        if(s[x]<min){
            min=s[x];
        }
    }
    cout << min;
    return 0;

}