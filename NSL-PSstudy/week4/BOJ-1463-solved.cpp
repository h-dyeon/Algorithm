#include<iostream>
using namespace std;
int x;//(1<=X<=1000000)
int answer[1000002];
int main() {
	scanf("%d", &x);

	answer[1] = 0;
	answer[2] = 1;
	answer[3] = 1;
	for (int i=4; i <= x; i++) {
		answer[i] = answer[i - 1] + 1;
		if (i % 2 == 0 && answer[i / 2] + 1 < answer[i])
			answer[i] = answer[i / 2] + 1;
		if (i % 3 == 0 && answer[i / 3] + 1 < answer[i])
			answer[i] = answer[i / 3] + 1;
	}

	cout << answer[x];
	return 0;
}