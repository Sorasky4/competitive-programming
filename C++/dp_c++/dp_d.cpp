#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using P = pair<int, int>;
#define rep(i,n) for(int i=0; i<(n); i++)
#define rep2(i,x,n) for(int i=x; i<(n); i++)
int main() {
    int n, W;
    cin >> n >> W;
    vector<ll> w(n),v(n);
    vector<vector<ll>> dp(n+1, vector<ll>(W+1,0));
    rep(i,n) cin >> w.at(i) >> v.at(i);
    rep(i,n){
        rep(j,W+1){
            if(j < w.at(i)) dp.at(i+1).at(j) = dp.at(i).at(j);
            else dp.at(i+1).at(j) = max(dp.at(i).at(j), dp.at(i).at(j-w.at(i))+v.at(i));
        }
    }
    cout << dp.at(n).at(W) << endl;
}