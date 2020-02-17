#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N;
int arr[12];
vector<int> cals;
int main() {
	//입력
	scanf("%d", &N);
	for (int j = 0; j < N; j++) {
		scanf("%d", &arr[j]);
	}
	for (int i = 0; i < 4; i++) {
		int t;
		scanf("%d", &t);
		for (int j = 0; j < t; j++) {
			cals.push_back(i);
		}
	}

	//계산
	int max=-1000000002, min=10000000002, sum;
	do {
		sum = arr[0];
		for (int i = 1; i < N ; i++) {
			if (cals[i-1] == 0) {
				sum += arr[i];
			}else if (cals[i-1] == 1) {
				sum -= arr[i];
			}
			else if (cals[i-1] == 2) {
				sum *= arr[i];
			}
			else if (cals[i-1] == 3) {
				sum /= arr[i];
			}
		}		
		//갱신
		max = max < sum ? sum : max;
		min = min > sum ? sum : min;
	} while (next_permutation(cals.begin(), cals.end()));

	cout << max << "\n" << min;
}