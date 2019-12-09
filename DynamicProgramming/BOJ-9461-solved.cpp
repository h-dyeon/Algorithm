#include <iostream>
#include <algorithm>
long long dp[101] = { 0,1,1,1,2,2,3,4,5,7,9 };
using namespace std;
int main() {
	int t;
	scanf_s("%d",&t);
	for (int i = 11; i < 101; i++) {
		dp[i] = dp[i - 1] + dp[i - 5];
	}
	while (t--) {
		int n;
		scanf_s("%d", &n);
		printf("%lli\n", dp[n]);
	}
	return 0;
}