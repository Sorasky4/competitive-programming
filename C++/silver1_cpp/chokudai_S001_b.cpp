#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<(n); i++)
#define rep2(i,x,n) for(int i=x; i<(n); i++)
int main() {
    int N;
    cin >> N;
    vector<int> a(N);
    rep(i,N){
        cin >> a[i];
    }
    int sum = 0;
    rep(i,N){
        sum += a[i];
    }
    cout << sum << endl;
    return 0;
}