
//1~9는 1자리수, 10~99는 2자리수 이런식으로 
// 자리수를 더한다.
#include <iostream>
#include <math.h>
using namespace std;
int main() {
	long long N, answer = 0, k;
	scanf_s("%lld", &N);
	for (k = 1; k < 9; k=k+1) {
		if (N >= pow(10 , k)) {
			answer += k * (pow(10, k) - pow(10, k - 1));
		}
		else {
			break;
		}	
	}
	answer += k * (N - pow(10, k - 1)+1);
	printf("%lli", answer);
}


// N=131일때
// 1~131은 모두 첫째 자리수를 가지고 있다.
// 10~131은 모두 둘째 자리수를 가지고 있다.
// 100~131은 모두 셋째 자리수를 가지고 있다.
#include <iostream>
#include <math.h>
using namespace std;
int main() {
	long long N, answer = 0, k=0;
	scanf_s("%lld", &N);
	while (pow(10, k) <= N) {
		answer += N - pow(10, k) + 1;
		k = k + 1;
	}
	printf("%lli", answer);
}