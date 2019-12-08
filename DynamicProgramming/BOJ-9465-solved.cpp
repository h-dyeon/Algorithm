#include <iostream>
#include <algorithm>
using namespace std;
int dp[2][100002];
int arr[2][100002];

int main() {

	int T, n;
	scanf_s("%d", &T);
	while (T--) {

		scanf_s("%d", &n);
		//입력
		for (int k = 0; k < 2; k++) {
			int t;
			for (int i = 1; i <= n; i++) {
				scanf_s("%d", &t);
				arr[k][i] = t;
			}
		}
		dp[0][1] = arr[0][1];
		dp[1][1] = arr[1][1];

		//풀이
		for (int i = 2; i <= n; i++) {
			dp[0][i] = max(dp[1][i - 1] , dp[1][i - 2]) + arr[0][i];
			dp[1][i] = max(dp[0][i - 1] , dp[0][i - 2]) + arr[1][i];
		}

		//출력
		int s = max(dp[0][n], dp[1][n]);
		printf("%d\n", s);
		//cout << max(dp[0][n], dp[1][n]) << "\n";
	}
	return 0;
}