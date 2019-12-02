#include <iostream>
using namespace std;
int main() {
	int  a,b,T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> a >> b;
		printf("Case #%d: %d + %d = %d\n",i+a,a,b,a+b);
	}
	return 0;
}