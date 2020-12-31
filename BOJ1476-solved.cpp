#include <iostream>
using namespace std;

int main() {

	int E, S, M, year;
	scanf_s("%d %d %d", &E, &S, &M);	

	year = S - 1;

	while (true) {
		if ((year % 15 == E - 1) && (year % 19 == M - 1))
			break;
		year += 28;
	}

	printf("%d", year+1);

	return 0;
}