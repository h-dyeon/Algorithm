#include <iostream>
using namespace std;
typedef long long ll;
#define max(a,b) (a>b?a:b);
ll arr[301];
ll dp[301];
int main() {
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
		scanf("%lld", &arr[i]);
	
	dp[1] = arr[1];
	dp[2] = max(arr[1]+arr[2],arr[2]);
	dp[3] = max(arr[1] + arr[3], arr[2] + arr[3]);
	for (int i = 3; i <= n; i++) 
		dp[i] = max(dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i]);
	//답
	printf("%lli", dp[n]);
	return 0;
}