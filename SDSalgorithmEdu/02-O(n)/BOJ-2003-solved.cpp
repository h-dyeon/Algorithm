#include <iostream>
using namespace std;
int N, M, answer;
int arr[10001];
int main() {
	scanf("%d %d", &N, &M);
	for (int i = 1; i <= N; i++) {
		scanf("%d", &arr[i]);
		arr[i] = arr[i] + arr[i - 1];
	}
	for (int i = 0; i <= N; i++) {
		for (int j = i; j <= N; j++) {
			if (arr[j]-arr[i] == M)
				answer++;
		}
	}

	cout << answer;
	return 0;
}