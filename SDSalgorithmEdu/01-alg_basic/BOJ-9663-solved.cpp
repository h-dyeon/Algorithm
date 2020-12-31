#include <iostream>
using namespace std;
int N, answer;
int rup[32];// 위대각선
int rdown[32];//아래로 대각선
int down[32];//세로
void minit() {
	for (int i = 0; i <= 2*N; i++) {
		rup[i] = 0;
		rdown[i] = 0;
		down[i] = 0;
	}
}
void dfs(int r) {
	if (r == N  ) {
		answer++;
		return;
	}
	for (int i = 0; i < N; i++)
		if(down[i]==0)
			if(rup[r+i]==0)
				if (rdown[r  - i+N] == 0) {
					down[i] = 1;
					rup[r+ i] = 1;
					rdown[r - i + N] = 1;

					dfs(r +1);

					down[i] = 0;
					rup[r + i] = 0;
					rdown[r - i + N] = 0;
				}
}
int main()
{
	scanf("%d",&N);
	for (int i = 0; i < N; i++) {
		minit();
		down[i] = 1;
		rup[0+i] = 1;
		rdown[0-i + N] = 1;
		dfs(0+1);
	}
	cout << answer;
	return 0;
}