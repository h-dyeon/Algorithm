#include <iostream>
#include <algorithm>
using namespace std;
int p[1001]; //카드팩 별 가격 pi
int f[1001]; //x개를 구매할때 최대 가격
int main() {
	int n;
	scanf_s("%d", &n);
	for (int i = 1; i <= n; i++)
		scanf_s("%d", &p[i]);

	f[0] = 0;
	for (int i = 1; i <= n; i++) {
		f[i] = p[i];
		for (int j = 1; j <= i; j++) {
			f[i] = max(f[i], p[j] + f[i - j]);
		}
	}
	cout << f[n];
}