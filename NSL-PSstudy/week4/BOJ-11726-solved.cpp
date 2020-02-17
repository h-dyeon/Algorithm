#include <iostream>
using namespace std;
#define max(a,b) (a>b?a:b);
int dp[1001];
int main() {
	int n;
	cin >> n;
	//dp
	dp[1] = 1;
	dp[2] = 2;
	for (int i = 3; i <= n; i++) {
		dp[i] = (dp[i - 1] + dp[i - 2])%10007;
	}
	//답
	cout << dp[n]%10007;
	return 0;
}