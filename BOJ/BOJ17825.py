##################################22.04.20
def dfs(cnt, sum_):
    global answer
    if cnt == 10:
        answer = max(answer, sum_)
        return
    for i in range(4):
        if horse[i] == (INF, INF):
            continue

        r, c = horse[i]
        step = dice[cnt]
        if c + step >= len(realmap[r]):
            horse[i] = (INF, INF)
            dfs(cnt + 1, sum_)
            horse[i] = (r, c)
        else:
            nr, nc = r, c + step
            if nr == 0:
                if nc == 5:
                    nr, nc = 1, 0
                elif nc == 10:
                    nr, nc = 2, 0
                elif nc == 15:
                    nr, nc = 3, 0

            if realmap[nr][nc]==25 and (nr,nc ) in [(2, 3), (3, 4)]:
                nr, nc = 1,4
            elif realmap[nr][nc]==30 and (nr,nc) in [(2, 4), (3, 5)]:
                nr, nc = 1, 5
            elif realmap[nr][nc] == 35 and (nr, nc) in [(2, 5), (3, 6)]:
                nr, nc = 1, 6
            elif realmap[nr][nc] == 40 and (nr, nc) in [(1, 7), (2, 6), (3, 7)]:
                nr, nc = 0, 20

            if (nr, nc) in horse:
                continue

            horse[i] = (nr, nc)
            dfs(cnt + 1, sum_ + realmap[nr][nc])
            horse[i] = (r, c)




if __name__ == '__main__':
    INF = 1e9
    dice = list(map(int, input().split(' ')))
    horse = [(0, 0), (0, 0), (0, 0), (0, 0)]
    realmap = [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
               [10, 13, 16, 19, 25, 30, 35, 40],
               [20, 22, 24, 25, 30, 35, 40],
               [30, 28, 27, 26, 25, 30, 35, 40]]
    answer = 0

    dfs(0, 0)
    print(answer)