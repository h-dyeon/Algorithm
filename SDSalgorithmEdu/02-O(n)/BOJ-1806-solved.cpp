#include <iostream>
using namespace std;
int N, S;
int answer = 999999;
long long arr[100001];
int main() {
	scanf("%d %d", &N, &S); 

		for (int i = 0; i < N; i++) {
			scanf("%lld", &arr[i]);
		}
		int left = 0, right = 0;
		long long sum = arr[0];
		while (left <= right && right < N) {
			if (sum < S) {
				right++;
				sum += arr[right];
			}
			else {
				if (answer > right - left + 1)
					answer = right - left + 1;
				sum -= arr[left];
				left++;
			}
		}
		if (answer == 999999)
			cout << 0;
		else
			cout << answer<<endl;	
}