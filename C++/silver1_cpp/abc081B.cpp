#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<(n); i++)
#define rep2(i,x,n) for(int i=x; i<(n); i++)
int main() {
    int ans=0, N;
    cin >> N;
    vector<int> A(N);
    rep(i,N) cin >> A[i];
    bool div_by_2 = true;
    while(div_by_2){
        rep(i,N){
            if(A[i] % 2 == 1){
                div_by_2 = false;
                break;
            }else{
                A[i] /= 2;
            }
        }
        if(div_by_2){
            ans++;
        }
    }
    cout << ans << endl;
    return 0;
}