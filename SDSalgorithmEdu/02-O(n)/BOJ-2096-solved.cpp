#include <iostream>
#include <algorithm>
using namespace std;
int N;
int a, b, c;
int minarr[2][3];
int maxarr[2][3];
int main() {
	scanf("%d", &N); 
	int white=1,black=0;
	for (int i = 1; i <= N; i++) {
		scanf("%d %d %d", &a, &b, &c);	
		//최소
		minarr[white][0] = a+ min(minarr[black][0], minarr[black][1]);
		minarr[white][1] = b + min(minarr[black][0], min(minarr[black][1], minarr[black][2]));
		minarr[white][2] = c + min(minarr[black][1], minarr[black][2]);
		//최대
		maxarr[white][0] = a + max(maxarr[black][0], maxarr[black][1]);
		maxarr[white][1] = b + max(maxarr[black][0], max(maxarr[black][1], maxarr[black][2]));
		maxarr[white][2] = c + max(maxarr[black][1], maxarr[black][2]);
		
		swap(white, black);
	}
	cout << max(maxarr[black][0], max(maxarr[black][1], maxarr[black][2])) << " "
		<< min(minarr[black][0], min(minarr[black][1], minarr[black][2]));
	return 0;
}