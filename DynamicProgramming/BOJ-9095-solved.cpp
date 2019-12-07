#include <iostream>
using namespace std;
int answer[12];
int main() {
	int T;
	scanf_s("%d", &T);
	answer[1] = 1;
	answer[2] = 2;
	answer[3] = 4;
	while (T--) {
		int n;
		scanf_s("%d", &n);
		for (int i = 4; i <= n; i++) {
			answer[i] =  answer[i - 1]+ answer[i - 2]+  answer[i - 3];
		}
		cout << answer[n] << "\n";
	}
	return 0;
}