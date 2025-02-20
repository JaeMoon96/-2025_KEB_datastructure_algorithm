#그래프(Graph) 클래스 정의
class Graph:
    def __init__(self, size):
        self.SIZE = size  # 그래프 크기(정점 개수)
        # 인접 행렬(Adjacency Matrix) 초기화: 0으로 채운 2차원 리스트
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

# 그래프를 출력하는 함수
def print_graph(g):
    print(' ', end=' ')
    for v in range(g.SIZE):
        print(name_ary[v], end=' ')  # 정점 이름 출력
    print()
    for row in range(g.SIZE):
        print(name_ary[row], end=' ')  # 현재 행의 정점 이름 출력
        for col in range(g.SIZE):
            print(f"{g.graph[row][col]:2}", end=' ')  # 인접 행렬의 값 출력
        print()
    print()

# 깊이 우선 탐색(DFS)을 이용한 경로 탐색 (재귀 함수)
def dfs(g, current, find_vtx, visited):
    visited.append(current)  # 현재 정점을 방문 처리
    if current == find_vtx:  # 찾고자 하는 정점인지 확인
        return True
    for vertex in range(g.SIZE):  # 모든 정점에 대해 탐색
        if g.graph[current][vertex] != 0 and vertex not in visited:  # 연결된 정점이면서 방문하지 않은 경우
            if dfs(g, vertex, find_vtx, visited):  # 재귀 호출로 탐색
                return True
    return False  # 끝까지 탐색했지만 찾는 정점이 없는 경우

# 특정 정점이 그래프에 존재하는지 확인하는 함수 (DFS 기반)
def find_vertex(g, find_vtx):
    visited = []  # 방문한 정점을 저장할 리스트
    return dfs(g, 0, find_vtx, visited)  # 0번 정점(춘천)에서 시작하여 탐색

# 그래프 생성 및 초기화
G1 = None
name_ary = ['춘천', '서울', '속초', '대전', '광주', '부산']  # 정점(도시) 이름
춘천, 서울, 속초, 대전, 광주, 부산 = 0, 1, 2, 3, 4, 5  # 도시별 인덱스

g_size = 6  # 정점 개수 (도시 개수)
G1 = Graph(g_size)  # 그래프 객체 생성

# 인접 행렬에 간선 추가 (양방향, 가중치 포함)
G1.graph[춘천][서울] = 10; G1.graph[춘천][속초] = 15
G1.graph[서울][춘천] = 10; G1.graph[서울][속초] = 40; G1.graph[서울][대전] = 11; G1.graph[서울][광주] = 50
G1.graph[속초][춘천] = 15; G1.graph[속초][서울] = 40; G1.graph[속초][대전] = 12
G1.graph[대전][서울] = 11; G1.graph[대전][속초] = 12; G1.graph[대전][광주] = 20; G1.graph[대전][부산] = 30
G1.graph[광주][서울] = 50; G1.graph[광주][대전] = 20; G1.graph[광주][부산] = 25
G1.graph[부산][대전] = 30; G1.graph[부산][광주] = 25

# 그래프 출력
print_graph(G1)

# (1) 간선 목록 만들기 [가중치, 시작 정점, 도착 정점]
edge_ary = []
for i in range(g_size):
    for k in range(g_size):
        if G1.graph[i][k] != 0:  # 연결된 간선이 있는 경우
            edge_ary.append([G1.graph[i][k], i, k])  # [가중치, 시작 정점, 도착 정점] 형태로 저장

print(edge_ary, len(edge_ary))  # 간선 목록 및 개수 출력

# (2) 가중치 기준으로 간선 정렬 (내림차순)
edge_ary.sort(reverse=True)

print(edge_ary, len(edge_ary))  # 정렬된 간선 목록 출력

# (3) 중복 간선 제거 (양방향 그래프이므로 중복 제거 필요)
new_ary = []
for i in range(0, len(edge_ary), 2):  # 중복을 제거하려면 2칸씩 건너뛰면서 저장
    new_ary.append(edge_ary[i])

print(new_ary, len(new_ary))  # 중복 제거된 간선 목록 출력

# (4) 크루스칼 알고리즘을 활용한 최소 신장 트리(MST) 생성 과정
index = 0
while len(new_ary) > g_size - 1:  # 최소 신장 트리(MST) 조건: 간선 개수가 '정점 개수 - 1'이 될 때까지
    start = new_ary[index][1]  # 시작 정점
    end = new_ary[index][2]  # 도착 정점
    save_cost = new_ary[index][0]  # 해당 간선의 가중치 저장

    # 그래프에서 현재 간선을 제거 (임시로 삭제하여 연결 상태 확인)
    G1.graph[start][end] = 0
    G1.graph[end][start] = 0

    # 간선을 제거한 후에도 그래프가 연결되어 있는지 확인
    startYN = find_vertex(G1, start)
    endYN = find_vertex(G1, end)

    if startYN and endYN:  # 그래프가 여전히 연결되어 있다면, 해당 간선 삭제 유지
        del new_ary[index]
    else:  # 그래프가 끊어졌다면, 해당 간선을 다시 추가 (삭제 취소)
        G1.graph[start][end] = save_cost
        G1.graph[end][start] = save_cost
        index += 1  # 다음 간선으로 이동

# # (4) 크루스칼 알고리즘 적용 (최소 신장 트리 MST)
# index = 0
# while len(new_ary) > g_size - 1:  # ✅ MST의 조건: 간선 수가 '정점 개수 - 1'이 될 때까지 반복
#     start = new_ary[index][1]  # 시작 정점
#     end = new_ary[index][2]  # 도착 정점
#     save_cost = new_ary[index][0]  # 간선 가중치 저장
#
#     # 간선 제거 (임시 삭제하여 그래프 연결 상태 확인)
#     G1.graph[start][end] = 0
#     G1.graph[end][start] = 0
#
#     # 간선 제거 후 연결성 검사
#     startYN = find_vertex(G1, start)
#     endYN = find_vertex(G1, end)
#
#     if startYN and endYN:  # ✅ 두 정점이 여전히 연결되어 있다면 해당 간선 삭제 유지
#         del new_ary[index]
#     else:  # ✅ 삭제했더니 그래프가 분리됨 -> 간선 복구
#         G1.graph[start][end] = save_cost
#         G1.graph[end][start] = save_cost
#         index += 1  # 다음 간선 확인


# (5) 최소 신장 트리(MST) 출력
print_graph(G1)

