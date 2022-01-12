/*stringŒ^•¶Žš—ñ
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
/*•¶Žš—ñ‚Ì’·‚³
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
/*i”Ô–Ú‚Ì•¶Žš
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
/*charŒ^•¶Žš
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
/*•¶Žš—ñ•Ï”.at(i)‚ÌŒ^‚Íchar
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
/*•¶Žš—ñ‚Ì‘‚«Š·‚¦‚Í1•¶Žš‚¸‚Â
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
/*“ü—Í‚³‚ê‚é•¶Žš—ñ‚É‰½•¶Žš'O'‚ªŠÜ‚Ü‚ê‚Ä‚¢‚é‚©‚ð”‚¦‚é
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
/*‘SŠp•¶Žš—ñ
#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<(n); i++)
#define rep2(i,x,n) for(int i=x; i<(n); i++)
int main() {
    string s = "‚±‚ñ‚É‚¿‚Í";
    cout << s << endl;
    return 0;
}
*/
/*.size()‚â==‰‰ŽZŽq‚ðŽg‚¤ê‡A•Ï”‚ÉŠi”[‚·‚é‚©A"•¶Žš—ñ"s.size()‚Ì‚æ‚¤‚É""‚Ì––”ö‚És‚ª•K—v
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
/*‹ó”’‚Å‹æØ‚ç‚¸As’PˆÊ‚Å“ü—Í‚µ‚½‚¢‚Æ‚«
#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<(n); i++)
#define rep2(i,x,n) for(int i=x; i<(n); i++)
int main() {
    string s, t;
    getline(cin, s);
    getline(cin, t);

    cout << "ˆês–Ú" << s << endl;
    cout << "“ñs–Ú" << t <<endl;
    return 0;
}
*/