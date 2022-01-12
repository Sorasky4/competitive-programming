#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<(n); i++)
#define rep2(i,x,n) for(int i=x; i<(n); i++)
int main() {
    int N;
    string S;
    cin >> N >> S;
    vector<int> vW(N+1,0), vE(N+1,0);
    rep(i,N){
        vW[i+1] += vW[i];
        if(S[i] == 'W') vW[i+1]++;
        vE[i+1] += vE[i];
        if(S[i] == 'E') vE[i+1]++;
    }
    int ans = 999999999;
    rep(i,N){
        int now = vW[i] + (vE[N] - vE[i+1]);
        ans = min(now, ans);
    }
    cout << ans << endl;
    return 0;
}