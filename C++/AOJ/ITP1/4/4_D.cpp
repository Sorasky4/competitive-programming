#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
using P = pair<int, int>;
#define rep(i,n) for(int i=0; i<(n); i++)
#define precision(x) fixed << setprecision(x)
#define all(x) (x).begin(),(x).end()
#define MAX(x) *max_element(all(x))
#define MIN(x) *min_element(all(x))
#define SUM(x) accumulate(all(x),0LL)
#define SIZE(x) ((ll)(x).size())
#define INF 1000000000000

int gcd(int a,int b){return b?gcd(b,a%b):a;}
const double PI = acos(-1);
int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};

int main() {
    int n, min, max;
    ll sum;
    cin >> n;
    vector<int>a(n,0);
    rep(i,n) cin >> a.at(i);
    min = MIN(a);
    max = MAX(a);
    sum = SUM(a);
    cout << min << " " << max << " " << sum << endl;
}