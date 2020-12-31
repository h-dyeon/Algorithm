#include <iostream>
#include <string>
#include <queue>
using namespace std;
int R, C, answer = 999999999;
pair<int, int> DD, SS; //비버<-고슴도치
queue<pair<int, int>> waterQ;//물
string str;
int arr[51][51]; 
int dr[4] = { 0,1,0,-1 };
int dc[4] = { -1,0,1,0 };
enum {
	emptyplace = 0,	//.
	water = -1,	//*
	rock=-300,	//X
	hedgehog=0,//S
	beaver=-400	//D
};
void bfs() {
	queue<pair<int, int>> q;
	q.push(make_pair(SS.first, SS.second));
	int tmpanswer = 0;

	while (!q.empty()) {
		tmpanswer++;
		//물 범람
		int watersize = waterQ.size();
		for (int i = 0; i < watersize; i++) {
			pair<int, int> nowW = waterQ.front(); waterQ.pop();
			for (int j = 0; j < 4; j++) {
				int nextR = nowW.first + dr[j];
				int nextC = nowW.second + dc[j];
				if (nextR >= 0 && nextR < R && nextC >= 0 && nextC < C) {
					if (arr[nextR][nextC] > water) {
						arr[nextR][nextC] = water;
						waterQ.push(make_pair(nextR, nextC));
					}
				}
			}
		}
		//고슴도치 이동
		int qsize = q.size();
		for (int qq = 0; qq < qsize; qq++) {
			pair<int, int> now = q.front(); q.pop();
			for (int j = 0; j < 4; j++) {
				int nextR = now.first + dr[j];
				int nextC = now.second + dc[j];
				if (nextR >= 0 && nextR < R && nextC >= 0 && nextC < C) {
					//도달하면
					if (nextR == DD.first && nextC == DD.second) {
						answer= tmpanswer;
						return;
					}
					//물 범람 예정인 구역을 피해서 , 이미 갔던 곳은 지나친다
					if (arr[nextR][nextC] >= emptyplace && arr[nextR][nextC] !=tmpanswer) {
						arr[nextR][nextC] = tmpanswer;
						q.push(make_pair(nextR, nextC));
					}
				}
			}
		}
	}
	//DD위치 도달불가
	return;
}
int main() {
	cin >> R >> C;
	for (int i = 0; i < R; i++) {
		cin >> str;
		for (int j = 0; j < C; j++) {
			if (str[j] == '.') {
				arr[i][j] = emptyplace;
			}
			else if (str[j] == '*') {
				arr[i][j] = water;
				waterQ.push(make_pair(i, j));
			}
			else if (str[j] == 'X') {
				arr[i][j] = rock;
			}
			else if (str[j] == 'D') {
				arr[i][j] = beaver;
				DD.first = i, DD.second = j;
			}
			else if (str[j] == 'S') {
				arr[i][j] = hedgehog;
				SS.first = i, SS.second = j;
			}
		}
	}
	bfs();
	if (answer == 999999999)
		cout << "KAKTUS\n";
	else
		cout << answer << "\n";
	return 0;
}
