/*string�^������
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
/*������̒���
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
/*i�Ԗڂ̕���
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
/*char�^����
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
/*������ϐ�.at(i)�̌^��char
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
/*������̏���������1��������
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
/*���͂���镶����ɉ�����'O'���܂܂�Ă��邩�𐔂���
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
/*�S�p������
#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<(n); i++)
#define rep2(i,x,n) for(int i=x; i<(n); i++)
int main() {
    string s = "����ɂ���";
    cout << s << endl;
    return 0;
}
*/
/*.size()��==���Z�q���g���ꍇ�A�ϐ��Ɋi�[���邩�A"������"s.size()�̂悤��""�̖�����s���K�v
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
/*�󔒂ŋ�؂炸�A�s�P�ʂœ��͂������Ƃ�
#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0; i<(n); i++)
#define rep2(i,x,n) for(int i=x; i<(n); i++)
int main() {
    string s, t;
    getline(cin, s);
    getline(cin, t);

    cout << "��s��" << s << endl;
    cout << "��s��" << t <<endl;
    return 0;
}
*/