#include <iostream>
#include <algorithm>
using namespace std;

int dice[6][9];//ABCDEF 순서
int T, M, C, P;
void initDice() {
	int k = 1;
	for (int i = 0; i < 6; i++)
		for (int j = 0; j < 9; j++)
			dice[i][j] = k, k++;
}
void rotateDice(bool clockwise,int side) {
	int tmp[9];
	for (int i = 0; i < 9; i++)
		tmp[i] = dice[side][i];
	if (clockwise) {
		dice[side][0] = tmp[6];
		dice[side][1] = tmp[3];
		dice[side][2] = tmp[0];
		dice[side][3] = tmp[7];
		dice[side][5] = tmp[1];
		dice[side][6] = tmp[8];
		dice[side][7] = tmp[5];
		dice[side][8] = tmp[2];
	}
	else {
		dice[side][0] = tmp[2];
		dice[side][1] = tmp[5];
		dice[side][2] = tmp[8];
		dice[side][3] = tmp[1];
		dice[side][5] = tmp[7];
		dice[side][6] = tmp[0];
		dice[side][7] = tmp[3];
		dice[side][8] = tmp[6];
	}
}

void doDice(int cmd) {
	if (cmd == 1 || cmd == 2 || cmd == 3) { //1,2,3
		int tmp;
		for (int i = 0; i < 3; i++) {
			tmp = dice[0][3*i + cmd-1];
			dice[0][3 * i+cmd-1] = dice[1][3 * i + cmd - 1];
			dice[1][3 * i + cmd - 1] = dice[2][3 * i + cmd - 1];
			dice[2][3 * i + cmd - 1] = dice[3][3 * i + cmd - 1];
			dice[3][3 * i + cmd - 1] = tmp;
		}
	}else if (cmd ==4 || cmd ==5 || cmd == 6) { //4,5,6
		int tmp;
		for (int i = 0; i < 3; i++) {
			tmp = dice[3][3 * i + cmd - 4];
			dice[3][3 * i + cmd - 4] = dice[2][3 * i + cmd - 4];
			dice[2][3 * i + cmd - 4] = dice[1][3 * i + cmd - 4];
			dice[1][3 * i + cmd - 4] = dice[0][3 * i + cmd - 4];
			dice[0][3 * i + cmd - 4] = tmp;
		}
	}
	else if (cmd == 9 || cmd == 8 || cmd == 7) { //7,8,9
		int v = 0;
		if (cmd == 8)v = 3;
		else if (cmd == 7)v = 6;
		int tmp;
		for (int i = 0; i < 3; i++) {
			tmp = dice[4][6 + i - v];
			dice[4][6 + i-v] = dice[1][6 + i - v] ;
			dice[1][6 + i - v] = dice[5][6 + i - v];
			dice[5][6 + i - v] = dice[3][2-i+v];
			dice[3][2 - i +v] = tmp;
		}
	}else if (cmd == 10|| cmd == 11 || cmd == 12) { //10,11,12
		int v = 0;
		if (cmd == 11)v = 3;
		else if (cmd == 10)v = 6;
		int tmp;
		for (int i = 0; i < 3; i++) {
			tmp = dice[3][2 - i + v];
			dice[3][2 - i + v] = dice[5][6 + i - v];
			dice[5][6 + i - v]= dice[1][6 + i - v];
			dice[1][6 + i - v] = dice[4][6 + i - v];
			dice[4][6 + i - v] = tmp;
		}
	}



	if (cmd == 1) rotateDice(false, 4);
	else if (cmd == 3) rotateDice(true, 5);
	else if (cmd == 4) rotateDice(true, 4);
	else if (cmd == 6) rotateDice(false, 5);

	else if (cmd == 7) rotateDice(true, 0);
	else if (cmd == 9) rotateDice(false, 2);
	else if (cmd == 10) rotateDice(false, 0);
	else if (cmd == 12) rotateDice(true, 2);
}
int main(){

	scanf_s("%d", &T);
	for(int i=1;i<=T;i++){
		initDice();
		scanf_s("%d", &M);

		//회전명령코드 수 M만큼 명령을 입력
		while (M--) {
			scanf_s("%d", &C);
			doDice(C);
		}

		//출력
		scanf_s("%d", &P);
		printf("#%d", i);
		for (int d = 0; d < 9; d++) {
			printf(" %d", dice[P - 1][d]);
		}
		printf("\n");
	}
}