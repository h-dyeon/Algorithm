#include <iostream>
#include <algorithm>
using namespace std;
int arr[10001];
int dp[10001];

int main() {
	int n, answer=0;
	scanf_s("%d", &n);
	for (int i = 1; i <= n; i++) {
		scanf_s("%d", &arr[i]);
		dp[i] = 1;
		for (int j = 1; j < n; j++) {
			if (arr[i] > arr[j])
				dp[i] =max(dp[i], dp[j] + 1);
		}
		answer = answer < dp[i] ? dp[i] : answer;
	}
	printf("%d", answer);
	return 0;
}