/*#include<iostream>
using namespace std;
int main() {
	string str;
	cin >> str;
	int num = str.size() / 10;
	for(int i=0;i<num;i++)
	{
		cout << str.substr(0, 10) << "\n";
		str = str.substr(10);
	}
	cout << str << "\n";
	return 0;
}*/
#include<iostream>
using namespace std;

int main() {
	string S;
	cin >> S;
	for (int i = 0; i < S.length(); i += 10)
		cout << S.substr(i, 10) << endl;
	return 0;
}