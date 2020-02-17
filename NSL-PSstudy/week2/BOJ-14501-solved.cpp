#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N;
int T[16], P[16];
int main() {
	//입력
	scanf("%d", &N);
	for (int j = 0; j < N; j++) {
		scanf("%d %d", &T[j],&P[j]);
	}
	
	//nC1, nC2, nC3, nC4 ... 검사
	int max = -1000000002;
	for (int i = 0; i < N; i++) {
		
		vector<int> idx;
		for (int j = 0; j < N; j++) {
			if (j > i)idx.push_back(0);
			else idx.push_back(1);
		}
		sort(idx.begin(), idx.end());

		do {
			int sum = 0;
			int check[16] = { 0, };
			check[N] = 1;
			for (int k = 0; k < N; k++) {
				if (idx[k] == 1) {

					//상담이 가능한지
					bool status = true;
					for (int m = k; m < k + T[k]; m++) {
						if (check[m] == 1) {
							status = false;
							break;
						}
					}

					//상담이 가능할때
					if (status) {
						for (int m = k; m < k + T[k]; m++) {
							check[m] = 1;
						}
						sum += P[k];
					}
				}
			}
			max = max < sum ? sum : max;
		} while (next_permutation(idx.begin(), idx.end()));
	}

	cout << max ;
}