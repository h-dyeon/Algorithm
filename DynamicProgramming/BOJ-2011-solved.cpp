#include <iostream>
#include <string>
using namespace std;
long long mod = 1000000;
long long dp[2];//0:맨 뒤 알파벳이 1자리수 (A,B,C..)인 경우의 수, 
				//1:맨 뒤 알파벳이 2자리수(Z,Y,X..)인 경우의 수
bool isAlphabet(int ten, int one) {
	int val= (ten - 48) * 10 + one - 48;
	if (val >= 10 && val <= 26)
		return true;
	return false;
}
bool isAlphabet(int one) {
	if (one - 48 == 0)
		return false; //0
	return true; // 1~9
}
int main(void) {
	string str;
	cin >> str;
	int length = str.length();

	if (!isAlphabet(str[0])){
		cout << 0; return 0;
	}
	dp[0] = 1, dp[1] = 0;

	for (int i = 1; i < str.length(); i++) {
		if (dp[0] == 0 && dp[1] == 0) {
			cout << 0;	return 0;
		}
		else {
			long long dp0 = dp[0];
			long long dp1 = dp[1];
			dp[0] = isAlphabet(str[i]) ? (dp0 + dp1)%mod : 0;
			dp[1] = isAlphabet(str[i - 1], str[i]) ? dp0 : 0;
		}
	}
	printf("%lld", (dp[0]+dp[1])%mod);
}
