/*
//내가 짠 맞은 코드
#include<iostream>
using namespace std;
int main() {
	int num, sum = 0;
	cin >> num;
	getchar();

	char str[101];
	fgets(str, 101, stdin);

	for (int i = 0; i < num; i++) {
		sum = sum + str[i] - 48;
	}
	cout << sum;
}*/

#include<cstdio>
int main() {
	int sum=0, num;
	scanf_s("%d", &num); //총횟수
	getchar(); //버퍼비우기
	for (int i=0; i < num; i++) { 
		sum += getchar() - 48; //한글자씩 읽음
	}
	printf("%d", sum); 
}