#include <iostream>
using namespace std;

int main() {
	long long answer[2] = { 0,1 };
	int n = 0;
	scanf_s("%d", &n);

	for (int i = 1; i < n; i++) {
		long long ans = answer[1];
		answer[1] = answer[0];
		answer[0] = answer[0] + ans;
	}

	cout << answer[0] + answer[1];
	return 0;
}

// https://www.acmicpc.net/source/16165942
// 규칙을 알고 피보나치수로 간단하게 줄임
#include <stdio.h>
int main(){
	long long  a[91], n;
	scanf("%lld",&n);
	a[1]=1;
	a[2]=1;
	for(int i=3;i<=n;i++) a[i]=a[i-1]+a[i-2];
	printf("%lld", a[n]);
} 