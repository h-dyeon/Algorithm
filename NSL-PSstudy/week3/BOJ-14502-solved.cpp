#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;
int N, M, answer;
int arr[9][9];
int dx[4] = { -1,0,1,0 };
int dy[4] = { 0,-1,0,+1 };
vector<pair<int, int>> permu;
vector<int> idx;
int main() {
	scanf("%d %d",  &N, &M);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			scanf("%d", &arr[i][j]);
			if(arr[i][j]==0)
				permu.push_back(make_pair(i, j));
		}
	}
	for (int i = 0; i < permu.size(); i++) {
		if (i < 3)idx.push_back(1);
		else idx.push_back(0);
	}
	sort(idx.begin(),idx.end());

	do {
		int copyarr[9][9] = { 0, };
		int tmpanswer = 0;
		//새로 지정할 벽 표시
		for (int i = 0; i < idx.size(); i++) {
			if (idx.at(i) == 1) {
				copyarr[permu.at(i).first][permu.at(i).second] = 1;
			}
		}
		//기존 지도 복사
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (copyarr[i][j] != 1)
					copyarr[i][j] = arr[i][j];
			}
		}
		//기존 지도와 비교하면서 바이러스 퍼뜨리기
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (copyarr[i][j] == 2 ) {
					copyarr[i][j] = 3;
					queue<pair<int,int>> q;
					q.push(make_pair(i, j));
					while (!q.empty()) {
						pair<int, int> now = q.front(); q.pop();
						for (int k = 0; k < 4; k++) {
							int nextX = now.first + dx[k];
							int nextY = now.second + dy[k];
							if (nextX >= 0 && nextX < N && nextY>=0 && nextY < M) {
								if (copyarr[nextX][nextY] == 0 || copyarr[nextX][nextY] == 2) {
									copyarr[nextX][nextY] = 3;
									q.push(make_pair(nextX, nextY));
								}
							}							
						}
					}

				}
			}
		}

		//안전영역 구하기
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (copyarr[i][j] == 0) {
					tmpanswer++;
				}
			}
		}
		//갱신하기
		answer = answer < tmpanswer ? tmpanswer : answer;
	} while (next_permutation(idx.begin(), idx.end()));
	cout << answer;
	return 0;
}

/*
//permutation 사용하지 않고 어짜피 벽의 개수는 3개니까
for문으로 더 빠르게 가능
for (int i = 0; i < ZeroCnt; i++) 
		{
			for (int j = i + 1; j < ZeroCnt; j++) 
			{
				for (int k = j + 1; k < ZeroCnt; k++) 
				{
					
					map[zero[i].r][zero[i].c] = 1;
					map[zero[j].r][zero[j].c] = 1;
					map[zero[k].r][zero[k].c] = 1;

					for (int m = 0; m < Vcnt; m++)
					{
						spread(V[m].r, V[m].c);
					}

					cnt = count_zero();
					if (max < cnt)
						max = cnt;

					map_init();
				}
			}
		}
*/