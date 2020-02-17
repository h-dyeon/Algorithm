#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N,M, answer;
vector<pair<int, int>> chicken;
vector<int> chicken_permu;
vector<pair<int, int>> house;
vector<int> houseDistance;
int tmpHouse[250];

void init() {
	for (int i = 0; i < house.size(); i++) {
		tmpHouse[i] = 999999999;
	}
}

int dis(pair<int, int> a, pair<int, int> b) {
	int answer=abs(a.first - b.first) + abs(a.second - b.second);
	return answer;
}

int main()
{
	answer = 999999999;
	//입력
	scanf("%d %d",&N,&M);
	int a;
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			scanf("%d", &a);
			if (a == 1) {
				house.push_back(make_pair(i, j));
			}if (a == 2) {
				chicken.push_back(make_pair(i, j));
			}
			
		}
	}

	//거리계산
	for (int i = 0; i < house.size(); i++) {
		for (int j = 0; j < chicken.size(); j++) {
			houseDistance.push_back(dis(house.at(i), chicken.at(j)));
		}
	}

	//조합
	for (int i = 0; i < chicken.size(); i++) {
		if (i < M)
			chicken_permu.push_back(1);
		else
			chicken_permu.push_back(0);
	}
	sort(chicken_permu.begin(), chicken_permu.end());
	
	//순열조합
	do {
		init();
		for (int i = 0; i < chicken_permu.size(); i++) {
			if (chicken_permu.at(i) == 1) {
				for (int j = 0; j < house.size(); j++) {
					int d= houseDistance.at(j*chicken.size() + i);
					tmpHouse[j] = tmpHouse[j] > d ? d : tmpHouse[j];
				}
			}
		}

		int tmpAnswer = 0;
		for (int i = 0; i < house.size(); i++) {
			tmpAnswer += tmpHouse[i];
		}
		if (answer > tmpAnswer)
			answer = tmpAnswer;
	} while (next_permutation(chicken_permu.begin(), chicken_permu.end()));
	
	cout << answer;
	return 0;
}