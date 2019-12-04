#include <iostream>
using namespace std;
int x;//(1<=X<=1000)
int t[1001];

int main() {
	scanf_s("%d", &x);
	int t[1001] = {0, 1,3,5 };
	for (int i = 4; i <= x; i++) {
		t[i] =( t[i - 1] + t[i - 2] * 2)%10007;
	}
	cout << t[x];
	return 0;
}