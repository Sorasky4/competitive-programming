#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<(n); i++)
#define rep2(i,x,n) for(int i=x; i<(n); i++)
int main() {
    int ans=0,n,k;
    cin >> n >> k;
    vector<int> l(n);
    rep(i,n) cin >> l[i];
    sort(l.begin(),l.end());
    reverse(l.begin(),l.end());
    rep(i,k) ans += l[i];
    cout << ans << endl;
    return 0;
}