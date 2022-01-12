#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
using P = pair<int, int>;
#define rep(i,n) for(int i=0; i<(n); i++)
#define precision(x) fixed << setprecision(x)
#define all(x) (x).begin(),(x).end()
#define MAX(x) *max_element(ALL(x))
#define MIN(x) *min_element(all(x))
#define SUM(x) accumulate(all(x),0LL)
#define SIZE(x) ((ll)(x).size())
#define INF 1000000000000

int gcd(int a,int b){return b?gcd(b,a%b):a;}
const double PI = acos(-1);
int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};

int main() {
    int n, i=0, x;
    cin >> n;
    while(++i <= n){
        x = i;
        if(x % 3 == 0){
            cout << " " << i;
            continue;
        }
        while(x){
            if(x % 10 == 3){
                cout << " " << i;
                break;
            }
            x /= 10;
        }
    }
    cout << endl;
}