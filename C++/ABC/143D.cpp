#include <bits/stdc++.h>
using namespace std;

int main(){
    int N, i = 0;
    cin >> N;
    vector<int> L(N);
    for(i; i < N; ++i){
        cin >> L[i];
    }
    sort(L.begin(), L.end());
    int ans = 0;
    for(int b = 0; b < N; ++b){
        for(int a = 0; a < b; ++a){
            int ab = L[a]+L[b];
            int r = lower_bound(L.begin(), L.end(), ab) - L.begin();
            int l = b + 1;
            ans += max(0,r-l);
        }
    }
    cout << ans << endl;
    return 0;
}