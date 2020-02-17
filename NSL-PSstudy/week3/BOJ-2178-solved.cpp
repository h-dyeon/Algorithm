#include <iostream>
#include <queue>
using namespace std;
int M, N, cnt;
int arr[101][101];
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};
int main() {

	scanf("%d %d",  &N, &M);
	for (int i = 1; i <= N; i++) {
		string str;
		cin >> str;
		for (int j = 0; j < M; j++) {
			if (str.at(j)=='1')
				arr[i][j + 1] = -1;
		}
	}
	
	queue<pair<int, int>> q;
	q.push(make_pair(1, 1));
	arr[1][1] = 1;
	while (!q.empty()) {
		pair<int, int> now = q.front(); q.pop();
		for (int i = 0; i < 4; i++) {
			if (arr[now.first + dx[i]][now.second + dy[i]] == -1) {
				q.push(make_pair(now.first + dx[i], now.second + dy[i]));
				arr[now.first + dx[i]][now.second + dy[i]] = arr[now.first][now.second] + 1;
			}
		}
	}
	cout << arr[N][M];
	return 0;
}