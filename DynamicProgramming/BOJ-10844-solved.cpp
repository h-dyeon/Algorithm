#include <iostream>
using namespace std;
#include <algorithm>

int main() {
	long long answer[101][10] = { {},{0,1,1,1,1,1,1,1,1,1} };
	long long modd = 1000000000;
	int n;
	scanf_s("%d", &n);

	for (int i = 2; i <= n; i++) {
		for (int j = 0; j < 10; j++) {
			if (j == 0) {
				answer[i][j] = answer[i - 1][j+1] % modd;
			}				
			else if (j == 9) {
				answer[i][j] = answer[i - 1][j-1] % modd;
			}
			else {
				answer[i][j] = (answer[i - 1][j-1]+ answer[i - 1][j+1])%modd;
			}
		}
	}

	long long sum = 0;
	for (int i = 0; i < 10; i++) {
		sum = (sum + answer[n][i]) % modd;
	}
	cout << sum << "\n";
	
	return 0;
}



//https://www.acmicpc.net/source/4408282
//필요없는 부분은 굳이 저장을 하지 않아도 됨
#include <cstdio>
#define R 1000000000
int n,s,k=1,d[2][11];
int main() {
	int i,j;
	for(j=1; j<=9; j++) d[k][j] = 1;
	scanf("%d", &n);
	for(i=2; i<=n; i++) {
		k = !k;
		for(j=0; j<10; j++) d[k][j] = (d[!k][j-1] + d[!k][j+1]) % R;
	}
	for(j=0; j<10; j++) s = (s+d[k][j]) % R;
	printf("%d", s);
	return 0;
}