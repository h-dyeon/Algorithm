#include <iostream>
using namespace std;
int main() {
	int x;
	scanf_s("%d", &x);

	for (int i = 0;i < 2*x-1;i++) {
		for (int j = 0;j < 2*x;j++) {
			if(i<x)
				if(j>i && j<2*x-i-1) printf(" ");
				else printf("*");
			else 
				if(j > 2*x-2-i&& j < i+1) printf(" ");
				else printf("*");
		}
		printf("\n");
	}
}