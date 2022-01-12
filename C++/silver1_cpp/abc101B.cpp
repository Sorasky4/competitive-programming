#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<(n); i++)
#define rep2(i,x,n) for(int i=x; i<(n); i++)
int main() {
   string N;
   int S = 0;
   cin >> N;
   rep(i,N.size()){
       S += N[i] - '0';
   }
   if(stoi(N) % S == 0){
       cout << "Yes" << endl;
   }else{
       cout << "No" << endl;
   }
   return 0;
}