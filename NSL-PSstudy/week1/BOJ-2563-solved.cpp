#include <iostream>
using namespace std;

int arr[101][101];
int N;

int main(){
    scanf("%d",&N);
    for(int i=0;i<N;i++){
        int a,b;
        scanf("%d %d",&a,&b);

        for(int j=a;j<a+10;j++){
            for(int k=b;k<b+10;k++){
            arr[j][k]=1;
            }
        }
    }

    int answer=0;
    for(int j=0;j<100;j++){
        for(int k=0;k<100;k++){
            answer+=arr[j][k];    
        }
    }

    printf("%d",answer);

    return 0;
}