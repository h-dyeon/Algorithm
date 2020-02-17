#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N;
int S[21][21];
int main() {
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			scanf("%d", &S[i][j]);
		}
	}

	//N개 중에 N/2개의 원소를 뽑아낸다.
	vector<int> idx;	
	for (int i = 0; i < N / 2; i++) {
		idx.push_back(1);
		idx.push_back(0);
	}
	sort(idx.begin(), idx.end());


	int min = 9999999999;
	do {
		int val = 0;
		for (int i = 0; i < N; i++) {
			for (int j = i; j < N; j++) {
				if (i != j) {
					if (idx[i] == 1 && idx[j] == 1) {
						val = val - S[i][j] - S[j][i];
					}
					if (idx[i] == 0 && idx[j] == 0) {
						val = val + S[i][j] + S[j][i];
					}
				}				
			}
		}
		//갱신
		min = min > abs(val) ? abs(val) : min;
	} while (next_permutation(idx.begin(), idx.end()));

	cout << min;
	return 0;
}