#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<(n); i++)
#define rep2(i,x,n) for(int i=x; i<(n); i++)
int main() {
   string S;
   cin >> S;
   if(S.substr(0,3) == "yah" && S[3] == S[4]){
       cout << "YES" << endl;
   }else{
       cout << "NO" << endl;
   }
   return 0;
}