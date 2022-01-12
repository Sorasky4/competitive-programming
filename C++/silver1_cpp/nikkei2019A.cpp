#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<(n); i++)
#define rep2(i,x,n) for(int i=x; i<(n); i++)
int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    rep(i,N) cin >> A[i];

    vector<long long> v(N+1, 0);
    rep(i,N) v[i+1] += v[i] + A[i];

    rep2(k,1,N+1){
        long long max_total = 0;
        for(int i=0; i+k<=N; i++){
            long long now = v[i+k] - v[i];
            max_total = max(max_total, now);
        }
        cout << max_total << endl;
    }
    return 0;
}