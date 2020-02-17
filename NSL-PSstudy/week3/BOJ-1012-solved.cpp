#include <iostream>
#include <queue>
using namespace std;
int T, M, N, K;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};
int main() {
	scanf("%d", &T);
	while (T--) {
		scanf("%d %d %d",  &M, &N, &K);
		int arr[51][51] = { 0, };
		queue<pair<int, int>> tmp;
		int cnt = 0;

		for (int i = 0; i < K; i++) {
			int x, y;
			scanf("%d %d", &x, &y);
			arr[x][y] = -1;
		}

		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
				if (arr[i][j] == -1) {//새로운 배추
					tmp.push(make_pair(i, j));
					cnt++;
				}
				while (!tmp.empty()) {
					pair<int, int> now = tmp.front();
					tmp.pop();
					arr[now.first][now.second] = cnt;
					for (int k = 0; k < 4; k++) {
						if (arr[now.first + dx[k]][now.second + dy[k]] == -1) {
							tmp.push(make_pair(now.first + dx[k], now.second + dy[k]));
							arr[now.first + dx[k]][now.second + dy[k]] = cnt;
						}
					}
				}
			}
		}
		cout << cnt<<"\n";
	}
	return 0;
}