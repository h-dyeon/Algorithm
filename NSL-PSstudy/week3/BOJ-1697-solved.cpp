#include <iostream>
#include <queue>
using namespace std;
int N, X;
//queue<pair<int, int>> q; //좌표&시간
queue<int>q; //좌표
int time[100001]; //시간
int main() {
	scanf("%d %d",  &N, &X);
	if (N == X) {
		cout << 0;
		return 0;
	}
	q.push(N);
	time[N] = 1;
	while (!q.empty()) {
		int now = q.front();
		q.pop();
		
		if (now + 1 == X || now - 1 == X || now * 2 == X) {
			cout << time[now] ;
			return 0;
		}
		for (int i = 0; i < 3; i++) {
			int tmp;
			if (i == 0)tmp = now - 1;
			else if (i == 1)tmp = now + 1;
			else if (i == 2)tmp = now * 2;

			if (tmp >= 0 && tmp <= 100000) {
				if (time[tmp] == 0) {
					q.push(tmp);
					time[tmp] = time[now] + 1;
				}				
			}
		}
	}	
	return 0;
}