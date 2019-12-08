#include <iostream>
#include <algorithm>
using namespace std;
long long arr[301];
long long dp[301];
int main() {
	int n;
	scanf_s("%lld", &n);
	for (int i = 1; i <= n; i++) scanf_s("%lld", &arr[i]);

	dp[1] = arr[1];
	dp[2] = max(arr[2], arr[1]+arr[2]);
	dp[3]= max(arr[1] + arr[3], arr[2] + arr[3]);
	
	for (int i = 4; i <= n; i++) {
		dp[i] = max(dp[i-2]+arr[i] , dp[i-3]+arr[i-1]+arr[i]);
	}	

	printf("%lli",dp[n] );
	return 0;
}