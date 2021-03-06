/*string型文字列
#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<(n); i++)
#define rep2(i,x,n) for(int i=x; i<(n); i++)
int main()
{
    string str1, str2;
    cin >> str1;
    str2 = ", world!";
    cout << str1 << str2 << endl;
    return 0;
}
*/
/*文字列の長さ
#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<(n); i++)
#define rep2(i,x,n) for(int i=x; i<(n); i++)
int main()
{
    string str = "Hello";
    cout << str.size() << endl;
    return 0;
}
*/
/*i番目の文字
#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<(n); i++)
#define rep2(i,x,n) for(int i=x; i<(n); i++)
int main()
{
    string str = "hello";
    cout << str.at(0) << endl;
    cout << str.at(4) << endl;
    return 0;
}
*/
/*char型文字
#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<(n); i++)
#define rep2(i,x,n) for(int i=x; i<(n); i++)
int main()
{
    char c = 'a';
    cout << c << endl;
    return 0;
}
*/
/*文字列変数.at(i)の型はchar
#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<(n); i++)
#define rep2(i,x,n) for(int i=x; i<(n); i++)
int main() {
    string str = "Hello";
    char c = str.at(0);
    cout << c << endl;
    return 0;
}
*/
/*文字列の書き換えは1文字ずつ
#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<(n); i++)
#define rep2(i,x,n) for(int i=x; i<(n); i++)
int main() {
    string str = "Hello";
    str.at(0) = 'M';
    cout << str << endl;
    return 0;
}
*/
/*入力される文字列に何文字'O'が含まれているかを数える
#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<(n); i++)
#define rep2(i,x,n) for(int i=x; i<(n); i++)
int main() {
    string str;
    cin >> str;
    int count = 0;
    rep(i,str.size()){
        if(str.at(i) == 'O'){
            count++;
        }
    }
    cout << count << endl;
    return 0;
}
*/
/*全角文字列
#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<(n); i++)
#define rep2(i,x,n) for(int i=x; i<(n); i++)
int main() {
    string s = "こんにちは";
    cout << s << endl;
    return 0;
}
*/
/*.size()や==演算子を使う場合、変数に格納するか、"文字列"s.size()のように""の末尾にsが必要
#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<(n); i++)
#define rep2(i,x,n) for(int i=x; i<(n); i++)
int main() {
    string str = "Hello";
    cout << str.size() << endl;
    cout << "Hello"s.size() << endl;
//    cout << "Hello".size() << endl;
    return 0;
}
*/
/*空白で区切らず、行単位で入力したいとき
#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<(n); i++)
#define rep2(i,x,n) for(int i=x; i<(n); i++)
int main() {
    string s, t;
    getline(cin, s);
    getline(cin, t);

    cout << "一行目" << s << endl;
    cout << "二行目" << t <<endl;
    return 0;
}
*/