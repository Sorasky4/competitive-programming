#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
using P = pair<int, int>;
#define rep(i,n) for(int i=0; i<(n); i++)
#define precision(x) fixed << setprecision(x)
#define all(x) (x).begin(),(x).end()
#define MAX(x) *max_element(ALL(x))
#define SIZE(x) ((ll)(x).size())
#define INF 1000000000000

int gcd(int a,int b){return b?gcd(b,a%b):a;}
const double PI = acos(-1);
int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};

int main() {
    double r, s, l;
    cin >> r;
    s = r * r * PI;
    l = 2 * r * PI;
    cout << precision(6) << s << " " << l << endl;
}