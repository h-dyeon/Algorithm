#include <iostream>
using namespace std;
int T, K;
int Tnum[50];
int IsTrue[1001];
int main() {
	for (int i = 0; i < 50; i++) {
		Tnum[i] = i * (i + 1) / 2;
	}
	for (int i = 1; i < 50; i++) {
		for (int j = 1; j < 50; j++) {
			for (int k = 1; k < 50; k++) {
				if (Tnum[i] + Tnum[j] + Tnum[k] < 1001) {
					IsTrue[Tnum[i] + Tnum[j] + Tnum[k]] = 1;
					//cout << Tnum[i] + Tnum[j] + Tnum[k] << endl;
				}
			}
		}
	}
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		scanf("%d", &K);
		printf("%d\n", IsTrue[K]);	
	}
	return 0;
}