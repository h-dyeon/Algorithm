#include <iostream>
#include <map>
using namespace std;
int A,B,NN,MM,arr[101][101];
//W,N,E,S
int dx[4]={-1,0,1,0};
int dy[4]={0,1,0,-1};
struct Robot{
	int x,y,dir;
};

int main(){
	map<int,Robot> robots;
	scanf("%d %d",&A,&B);
	scanf("%d %d",&NN,&MM);
	//로봇입력
	for(int i=1;i<=NN;i++){
		Robot tmp; char direction; //로봇, 방향
		scanf("%d %d %c",&tmp.x,&tmp.y, &direction);
		if(direction=='W') tmp.dir=0;
		else if(direction=='N') tmp.dir=1;
		else if(direction=='E') tmp.dir=2;
		else if(direction=='S') tmp.dir=3;
		robots.insert(make_pair(i,tmp));
		arr[tmp.x][tmp.y]=i;
	}
	//명령입력&수행
	bool status=true;
	for(int i=0;i<MM;i++){

		int Rnum; char oper; int iter; //로봇번호,명령종류,반복횟수
		scanf("%d %c %d",&Rnum,&oper, &iter);
		
		if(status){
			if(oper=='L'){	
				robots.at(Rnum).dir=(robots.at(Rnum).dir-iter+100)%4;
			}else if(oper=='R'){
				robots.at(Rnum).dir=(robots.at(Rnum).dir+iter)%4;
			}else if(oper=='F'){
				
				for(int k=0;k<iter;k++){
					int nextX=robots.at(Rnum).x+dx[robots.at(Rnum).dir];
					int nextY=robots.at(Rnum).y+dy[robots.at(Rnum).dir];
					//Robot X crashes into the wall
					if(nextX<=0 ||nextX>A || nextY<=0 || nextY>B){
						printf("Robot %d crashes into the wall",Rnum);
						status=false;
						break;
					}
					//Robot X crashes into robot Y
					if(arr[nextX][nextY]!=0){
						printf("Robot %d crashes into robot %d",Rnum,arr[nextX][nextY]);
						status=false;
						break;
					}
					arr[robots.at(Rnum).x][robots.at(Rnum).y]=0;
					arr[nextX][nextY]=Rnum;
					robots.at(Rnum).x+=dx[robots.at(Rnum).dir];
					robots.at(Rnum).y+=dy[robots.at(Rnum).dir];
				}
			}
		}	}
	if(status)
		cout<<"OK";
}
