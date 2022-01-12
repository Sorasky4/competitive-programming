#include <bits/stdc++.h>
using namespace std;

int main() {
  string p;
  int N, A;
  int ans = A, x;
  cin >> N >> A;
  for(int i=0; i < N; i++){
  cin >> p >> x;
  if(p == "+"){
      ans += x;
  }else if(p == "-"){
      ans -= x;
  }else if(p == "*"){
      ans *= x;
  }else{
      if(x == 0){
          cout << "error" << endl;
          break;
      }else{
          ans /= x;
      }
  }
  cout << i+1 << ":" << ans << endl;
  }
}