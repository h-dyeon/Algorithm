/*
//�����ڵ�
#include <stdio.h>
#include <stdlib.h>

int main()
{
	char ch=NULL;
	while (ch != EOF)
	{
		ch = getchar();
		if (ch == EOF)
			continue;
		putchar(ch);
	}
	return 0;
}*/


/*
//���� �ڵ�
#include <cstdio>
using namespace std;
int main() {
	char str[101];
	while (fgets(str, 101, stdin) != NULL) {
		printf("%s", str);
	}
	return 0;
}*/

//Ʋ�� �ڵ�
#include<iostream>
using namespace std;
int main() {
	string str;
	cin >> str;
	while (cin.eof() != NULL) {
		cout << str;
		cin >> str;
	}
}