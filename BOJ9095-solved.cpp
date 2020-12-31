#include <stdio.h>

int main() {
	int arr[12] = { 0,1,2,4 };
	for (int i = 4; i < 12; i++)
		arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3];
	
	int n;
	scanf_s("%d", &n);
	while (n--) {
		int ans;
		scanf_s("%d", &ans);
		printf("%d\n", arr[ans]);
	}
	return 0;
}