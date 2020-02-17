#include <iostream>
using namespace std;
int arr[3][1001][1001]; //JOI
int N, M, k;//가로,세로,영역개수
char tmp[1001];
int a,b,c,d;

void calc(char JOI,int i,int j) {
	for(int tt=0;tt<3;tt++){
		arr[tt][i][j] = arr[tt][i-1][j] + arr[tt][i][j-1] - arr[tt][i-1][j-1];
	}
	if (JOI == 'J'){ arr[0][i][j]++;}
	else if (JOI == 'O') arr[1][i][j]++;
	else if (JOI == 'I') arr[2][i][j]++;
}

int main() {
	scanf("%d %d", &M, &N);
	scanf("%d", &k);
	for (int i = 1; i <= M; i++) {
		scanf("%s",tmp);
		for (int j = 0; j< N; j++) {
			calc(tmp[j],i,j+1);
		}
	}
	
	for(int i=0;i<k;i++){
		scanf("%d %d %d %d",&a,&b,&c,&d);
		for(int JOI=0;JOI<3;JOI++){
			cout<<arr[JOI][c][d] - arr[JOI][a-1][d] - arr[JOI][c][b-1] + arr[JOI][a-1][b-1]<<" ";
		}
		cout<<"\n";
	}
	return 0;
}