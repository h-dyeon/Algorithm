#include <iostream>
#include <algorithm>
using namespace std;
long long arr[100001];
long long dp[100001];
int main() {
	int n;
	scanf("%lld", &n);
	for (int i = 1; i <= n; i++) scanf("%lld", &arr[i]);

	long long Max = -100000009;
	for (int i = 1; i <= n; i++) {
		dp[i] = max(arr[i], dp[i-1]+arr[i]);
		Max = max(dp[i], Max);
	}

	printf("%lli",Max );
	return 0;
}