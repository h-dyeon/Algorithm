#include <iostream>
using namespace std;
int main() {
	int  T;
	string str;
	cin >> T;
	while (T--) {
		cin >> str;
		string a = str.substr(0, str.find(","));
		string b = str.substr( str.find(",")+1);
		int aa = atoi(a.c_str());
		int bb = atoi(b.c_str());
		cout << aa + bb << "\n";
	}
	return 0;
}
/*
#include <iostream>
int main() {
	int a;
	int c, d;
	scanf("%d", &a);
	for (int i = 0; i < a; i++) {
		scanf("%d,%d", &c, &d);
		printf("%d\n", c + d);
	}
}*/