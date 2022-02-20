class Solution:
    def countCombinations(self, pieces, positions) -> int:
        self.directions = {
            "rook": [(-1, 0), (1, 0), (0, -1), (0, 1)],
            "bishop": [(-1, -1), (-1, 1), (1, -1), (1, 1)],
            "queen": [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        }

        self.n = len(pieces)
        self.ans = set()
        self.dirs = [0] * self.n

        def setDirections(cur):
            if cur == self.n: # 모든 말의 방향을 지정해줬음.
                pos = [(positions[i][0], positions[i][1]) for i in range(self.n)] # position of pieces
                print(cur, self.dirs,"\t",pos)
                dfs(pos, 0) # 방향만을 지정해줌.
                return

            # 각 말의 모든 방향 조합을 모두 탐색
            # cur 번째의 peice의 모든 방향을 for로 순회하면서 그다음 cur+1번째의 peice도 순회한다.
            for i in range(len(self.directions[pieces[cur]])):
                self.dirs[cur] = self.directions[pieces[cur]][i]
                setDirections(cur + 1)

        def dfs(pos, stopped):
            self.ans.add(tuple(pos)) #가능한 위치 조합을 ans에 저장

            if stopped == (1 << self.n) - 1: # peice들을 다 순회했다는 뜻, 만약 n=2이면 bin(11)즉 모두 탐색했을때 return
                return

            for mask in range(1 << self.n): # peice들의 조합을 bit마스크로 표현해서 순회
                if stopped & mask: continue 

                visit = set()
                new_pos = []
                new_stopped = stopped ^ mask #XOR 연산 (다르면1, 같으면0)
                                            # stopped는 멈춰있을 peice를 의미

                for i in range(self.n):
                    nr, nc = pos[i][0], pos[i][1]

                    if not (new_stopped & (1 << i)): #i번째 peice가 new_stopped에 1이라 되어있으면 멈추는것.
                        nr += self.dirs[i][0] # 멈추지 않는 노드들만 방향대로 1칸 전진
                        nc += self.dirs[i][1]

                    if 1 <= nr < 9 and 1 <= nc < 9 and (nr, nc) not in visit:
                        new_pos.append((nr, nc))
                        visit.add((nr, nc)) # 점령한 좌표는 고려하지 않음.
                                            # => 아니 근데 이미 bishop이 이 좌표에 도달했을때 
                                            # 그렇다고 queen이 못가게 만들면 상하좌우 좌표는 못가게 되는거 아닌가?

                if len(new_pos) == self.n: # 모든 peice의 좌표가 범위내에 있고 이전에 방문한 위치가 아니라면 
                    print("---",pos, new_stopped)
                    dfs(new_pos, new_stopped) #새로운 위치에서 또다시 순회를 시작.

        setDirections(0)

        return len(self.ans)


t=Solution()
print(t.countCombinations(pieces=["bishop","queen"], positions=[[4,3],[2,6]]))

# # rook_dir=((1,0),(-1,0),(0,1),(0,-1))
# # queen_dir=((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1))
# # bishop_dir=((1,1), (1,-1), (-1,1), (-1,-1))

# dirs=[]
# for p in pieces:
#     if p=="bishop": dirs.append(((1,1), (1,-1), (-1,1), (-1,-1)))
#     elif p=="queen" :dirs.append(((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)))
#     elif p=="rook":dirs.append(((1,0),(-1,0),(0,1),(0,-1)))

# poss=[tuple(p) for p in positions]

# print(dirs)
# print(poss)

# visited=[[0 for _ in range(8)] for _ in range(8)]
# for i in range(len(positions)):
#     visited[positions[i][0]][positions[i][1]]=1
# answer=0
# for i in range(len(visited)):
#     answer+=sum(visited[i])
# print(answer)