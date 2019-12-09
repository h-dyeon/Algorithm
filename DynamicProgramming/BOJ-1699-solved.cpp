#include <iostream>
#include <algorithm>
using namespace std;
int dps[100001];
int main() {
	int n;
	scanf_s("%d", &n);

	dps[1] = 1;
	dps[2] = 2;
	dps[3] = 3;
	for (int i = 4; i <= n; i++) {
		dps[i] = i; //초기화
		for (int j = 1; j * j <= i; j++) {
			dps[i] = min(dps[i], 1 + dps[i - (j * j)]);
		}
	}

	printf("%d", dps[n]);
	return 0;
}
