/*
//���� § ���� �ڵ�
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
	scanf_s("%d", &num); //��Ƚ��
	getchar(); //���ۺ���
	for (int i=0; i < num; i++) { 
		sum += getchar() - 48; //�ѱ��ھ� ����
	}
	printf("%d", sum); 
}