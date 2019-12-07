#include <iostream>
using namespace std;
#include <algorithm>

int main() {
	long long answer[2][10] = { { 1, 1,1,1,1,1,1,1,1,1},{0,} };
	long long modd = 10007;

	int n, b = 0;
	scanf_s("%d", &n);
	for (int k = 1; k < n; k++) { //횟수
		b = !b;
		for (int i = 0; i < 10; i++) { //끝자리수가 0부터 9까지
			answer[b][i] = 0;
			for (int j = 0; j <= i; j++) {
				answer[b][i] = (answer[b][i] + answer[!b][j]) % modd;
			}
		}
	}

	long long sum = 0;
	for (int i = 0; i < 10; i++) {
		sum = (sum + answer[b][i]) % modd;
	}
	cout << sum;

	return 0;
}


//https://www.acmicpc.net/source/4408448
#include <cstdio>
int n,d[15]={1};
int main() {
	int i,j;
	scanf("%d", &n);
	for(i=0; i<=n; i++)
		for(j=1; j<10; j++) 
            d[j]+=d[j-1], d[j]%=10007;
	printf("%d", d[9]);
	return 0;
}