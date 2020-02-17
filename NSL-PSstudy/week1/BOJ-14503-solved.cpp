#include <iostream>
#include <math.h>
using namespace std;
int M, N, Sr, Sc, dir, answer;
int arr[51][51];

//북동남서
int dr[4] = { -1,0,1,0 };
int dc[4] = { 0,1,0,-1 };

int main() {
	scanf("%d %d", &N, &M);
	scanf("%d %d %d", &Sr, &Sc, &dir);
	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++)
			scanf("%d", &arr[i][j]);

	bool status=true,back=true;
	int NowR=Sr,NowC=Sc;//처음 ㅅ작위치
	while(status){
		//현위치 청소
		if (arr[NowR][NowC] == 0) {
			arr[NowR][NowC] = 2;//청소기가 청소한 공간
			answer++;
		}
		//왼쪽으로 탐색진행
		for(int i=0;i<4;i++){
			dir=(dir+3)%4;
			int NextR=NowR+dr[dir];
			int NextC=NowC+dc[dir];
			back=true;
			if (NextR>=0 || NextR<N || NextC>=0 || NextC<M){
				if(arr[NextR][NextC]==0){
					NowR = NextR, NowC = NextC;
					back=false;
					break;
				}
			}			
		}
		//네방향 모두 청소가 이미 되어있거나 벽인 경우 후진
		if(back){
			NowR-=dr[dir];
			NowC-=dc[dir];
			if (NowR<0 || NowR>=N || NowC<0 || NowC>=M) //범위밖
				status=false;
			if(arr[NowR][NowC]==1) //벽
				status=false;
		}
	}
	printf("%d", answer);
}