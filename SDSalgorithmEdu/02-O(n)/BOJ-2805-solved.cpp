#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;
vector < ll > trees;
ll N, M, high, low,mid;
ll sum(int mid)
{
	ll answer = 0;
	for (ll t : trees) {
		if (t > mid)
			answer += t - mid;
	}
	return answer;
}
int main() {
	scanf("%lld %lld", &N, &M);
	high = 0;
	ll t;
	for (int i = 0; i < N; i++) {
		scanf("%lld", &t);
		trees.push_back(t);
		high = high < t ? t : high;
	}
	
	low = 0;
	mid = low;
	do {
		ll llsum = sum(mid);
		if (llsum == M) {
			cout << mid;
			return 0;
		}
		else if (llsum > M) {
			low = mid;
			mid = (low + high) / 2;
		}
		else if (llsum < M) {
			high = mid;
			mid = (low + high) / 2;
		}
	} while (mid != low);
	cout << mid;
	return 0;
}