// 점화식으로 짠 코드
// for문에서 변수의 범위와 초기값을 반드시 확인할 것
// 나머지 계산을 할때는 순서를 잘 고려해야 한다!
#include <iostream>
#include <algorithm>
using namespace std;
long long dp[2][201]; 
long long r = 1000000000;
int main() {
	int n, k;
	scanf_s("%d %d", &n, &k);
	int b = 0;

	for (int i = 0; i <= n; i++)
		dp[b][i] = 1;

	//dp[k][n] = dp[k-1][n-1] + dp[k-1][n-2] + ... + dp[k-1][0]
	for (int i = 2; i <= k; i++) {
		b = !b;
		for (int nn = 0; nn <= n; nn++) {
			dp[b][nn] = 0;
			for (int pp = 0; pp <= nn; pp++) {
				dp[b][nn] += dp[!b][pp];
			}
			dp[b][nn] %= r;
		}
	}
	cout<< dp[b][n];
}


//중복조합이라 오버플로우에 시간까지 오래걸리는 코드
/*
#include <iostream>
#include <algorithm>
long long dp[201] ;
using namespace std;
long long fact(long long num) {
	if (dp[num] != 0)
		return dp[num];
	else
		return num * fact(num - 1);
}
int main() {
	int n,k;
	long long r = 1000000000;
	scanf_s("%d %d",&n,&k);

	//(n+k-1)!/(n)!(k-1)!
	long long answer = fact(n + k - 1) / fact(n) * fact(k-1);
	answer = answer % r;
	
	cout << answer;	
}*/

