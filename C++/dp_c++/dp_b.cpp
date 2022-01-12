#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<(n); i++)
#define rep2(i,x,n) for(int i=x; i<(n); i++)
int main() {
    int N, K, tmp, min_cost;
    cin >> N >> K;
    vector<int> h(N), dp(N, 0);
    rep(i, N) cin >> h[i];
    dp[1] = abs(h[1] - h[0]);
    rep2(i, 2, N){
        min_cost = 999999999;
        rep2(j, 1, min(i, K)+1){
            tmp = dp[i-j] + abs(h[i] - h[i-j]);
            min_cost = min(min_cost, tmp);
        }
        dp[i] = min_cost;
    }
    cout << dp[N-1] << endl;
    return 0;
}