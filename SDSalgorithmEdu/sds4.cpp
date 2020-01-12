/*#include <iostream>
#include <map>
#include <stack>
using namespace std;
int T, N;
int arr[200002];//컴퓨터 저장
map<int, int> five0;//특정x번 컴퓨터에 0이 몇개 연결 되었는가?
int muri[200002];//무리 개수
int sum;//케이블 총길이
stack<int> muri2;

int main() {
	scanf_s("%d", &T);
	for (int i = 1; i <= T; i++) {
		//초기화
		fill_n(arr, 200002, 0);
		fill_n(muri, 200002, 0);
		sum = 0;
		five0.clear();
		while (!muri2.empty())
			muri2.pop();

		//입력
		scanf_s("%d", &N);
		for (int j = 1; j <= N; j++) {
			scanf_s("%d", &arr[j]);
			if (arr[j] == 1)
				five0.insert(make_pair(j, 0));
		}

		//계산
		for (int k = N; k > 0; k--) {
			muri[k] = muri[k + 1] + 1; //오른쪽 컴퓨터의 무리 값에서 +1
			if (arr[k] == 0) {//0을 확인중일때
							   				
				for (int b = k + 1; b <= N; b++) {
					if (arr[b] == 1 && five0.find(b)->second == 5) {
						break;
					}
					if (arr[b] == 1) {//0번 컴퓨터와 1번 컴퓨터를 연결
						five0.find(b)->second++;
						sum = sum + (b-k);//케이블 길이 더하기

						fill_n(muri, b, muri[b]);
						//for (int connected = k; connected < b; connected++)
						//	muri[connected] = muri[b];
					}
				}
			}
		}

		//출력
		printf("#%d %d %d\n", i, sum, muri[1]);
	}
}*/

#include <iostream>
#include <map>
using namespace std;
int T, N;
int sum;//케이블 총길이
map<int, int> zeros;//0번 컴퓨터들 (0번컴퓨터의 위치, 무리값)

int main() {
	//five0.find(five0.begin)->
	scanf_s("%d", &T);
	for (int i = 1; i <= T; i++) {
		sum = 0;
		zeros.clear();

		//입력
		scanf_s("%d", &N);
		int tmp;
		for (int j = 1; j <= N; j++) {
			scanf_s("%d", &tmp);
			if (tmp == 1) {
				//케이블길이를 더한다
				//zeros공간에 있는 컴퓨터와(key)값과 현재번호j와의 차를 모두 더한다.
				if (!zeros.empty()) {
					map<int, int>::iterator it;
					for (it = zeros.begin(); it != zeros.end(); it++) {
						sum = sum + j - it->first;
						it->second = zeros.begin()->second;
					}
				}
			}
			else {
				//zeros 공간에 0번컴퓨터가 5개가 넘지않도록 관리한다.
				//몇번인지, 무리값을 pair로 추가하되
				//무리값은 가장 앞에 있는 컴퓨터의 무리값+1을 한다.
				if (zeros.size() == 5)
					zeros.erase(zeros.begin()->first); //맨 앞의 0을 제거
				if (zeros.empty())
					zeros.insert(make_pair(j, j));
				else
					zeros.insert(make_pair(j, zeros.rbegin()->second + 1));
			}
		}
		//출력
		printf("#%d %d %d\n", i, sum, zeros.rbegin()->second);
	}
}