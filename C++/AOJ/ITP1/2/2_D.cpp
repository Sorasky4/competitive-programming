#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
using P = pair<int, int>;
#define rep(i,n) for(int i=0; i<(n); i++)
#define all(x) (x).begin(),(x).end()
#define MAX(x) *max_element(ALL(x))
#define SIZE(x) ((ll)(x).size())
#define INF 1000000000000

int gcd(int a,int b){return b?gcd(b,a%b):a;}
int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};

int main() {
    int W, H, x, y, r;
    string ans = "Yes";
    cin >> W >> H >> x >> y >> r;
    if (x - r < 0 || W < x + r || y - r < 0 || H < y + r) ans = "No";
    cout << ans << endl;
}