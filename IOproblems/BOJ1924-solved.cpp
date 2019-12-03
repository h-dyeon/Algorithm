#include <iostream>
using namespace std;
int main() {
	int x, y;
	int months[12] = { 31,28,31,30,31,30,31,31,30,31,30,31 };
	string days[7] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"  };
	scanf_s("%d %d", &x,&y);
	
	int sum = 0;
	for (int i = 0;i < x-1;i++)
		sum += months[i];
	sum += y;

	sum = sum % 7;
	cout << days[sum];
}