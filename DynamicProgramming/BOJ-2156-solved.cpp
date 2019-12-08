#include <iostream>
#include <algorithm>
using namespace std;
long long arr[10001];
long long dp[3][10001]; 
//  . . X : 0
//  . X O : 1
//  X O O : 2

int main() {
	int n;
	scanf_s("%d", &n);
	for (int i = 1; i <= n; i++) {
		scanf_s("%lld", &arr[i]);
	}
	dp[0][1] = 0;
	dp[1][1] = arr[1];
	dp[2][1] = arr[1];

	for (int i = 2; i <= n; i++) {
		dp[0][i] = max(dp[0][i - 1] , dp[1][i - 1]); 
		dp[0][i] = max(dp[0][i] , dp[2][i - 1] );
		dp[1][i] = dp[0][i - 1] + arr[i];
		dp[2][i] = dp[1][i - 1] + arr[i];
	}

	long long s = max(dp[0][n], dp[1][n]);
	s=max(s, dp[2][n]);
	printf("%lli",s);

	return 0;
}