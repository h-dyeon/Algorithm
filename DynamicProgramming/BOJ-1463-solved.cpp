//내코드
#include<iostream>
using namespace std;
int x;//(1<=X<=1000000)
int answer[1000002];
int main() {
	scanf_s("%d", &x);

	answer[1] = 0;
	answer[2] = 1;
	answer[3] = 1;
	for (int i=4; i <= x; i++) {
		answer[i] = answer[i - 1] + 1;
		if (i % 2 == 0 && answer[i / 2] + 1 < answer[i])
			answer[i] = answer[i / 2] + 1;
		if (i % 3 == 0 && answer[i / 3] + 1 < answer[i])
			answer[i] = answer[i / 3] + 1;
	}

	cout << answer[x];
	return 0;
}

//참고 코드 ==> https://www.acmicpc.net/source/16250222
//재귀함수 사용, 
/*
#include <cstdio>
using namespace std;
int i;
int solve(int num) {
	if (num < 2) return 0;
	int a1 = solve(num / 3) + num % 3 + 1;
	int a2 = solve(num / 2) + num % 2 + 1;

	return a1 < a2 ? a1 : a2;
}
int main() {
	int num;
	scanf("%d", &num);
	printf("%d", solve(num));
}*/