#include <iostream>
using namespace std;
int T, N;
int arr[65][65];

bool checkMin(int size, int x,int y) {
	int max[4] = { 0, };
	for (int i = x; i < x+size; i++) {
		for (int j = y; j < y+size; j++) {
			if (i < x+size/2) { 
				if (j < y+size/ 2) {//1번행렬
					if (max[0] < arr[i][j])
						max[0] = arr[i][j];
				}
				else {//2번행렬
					if (max[1] < arr[i][j])
						max[1] = arr[i][j];
				}
			}
			else {
				if (j < y + size / 2) {//3번행렬
					if (max[2] < arr[i][j])
						max[2] = arr[i][j];
				}
				else {//4번행렬
					if (max[3] < arr[i][j])
						max[3] = arr[i][j];
				}
			}
		}
	}
	int MAX = 0, MIN = 99999999;
	for (int i = 0; i < 4; i++) {
		MAX= MAX < max[i] ? max[i] : MAX;
		MIN = MIN > max[i] ? max[i] : MIN;
	}

	if (MAX <= 1.2 * MIN) return true;
	return false;
}
void recursive( int size, int x, int y) {
	if (size == 2)
		return ;
	if (checkMin(size, x, y)) {
		cout << "1";
		recursive(size / 2, x, y);
		recursive(size / 2, x, y + size / 2);
		recursive(size / 2, x + size / 2, y);
		recursive( size / 2, x + size / 2, y + size / 2);
	}
	else {
		cout << "0";
		return;
	}
}
int main() {
	scanf_s("%d", &T);
	for (int i = 1; i <= T; i++) {
		scanf_s("%d", &N);

		//입력
		int max = 0;
		for(int j=1;j<=N;j++)
			for (int k = 1; k <= N; k++) {
				scanf_s("%d", &arr[j][k]);
			}
		//출력
		cout << "#" << i << " ";
		recursive( N, 1, 1);
		cout<< "\n";
	}
}