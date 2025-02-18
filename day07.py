# collections 모듈에서 deque(덱)를 가져옴
# deque는 Python의 기본 리스트보다 빠른 양방향 큐(Queue) 자료구조이다.
# 리스트와 달리, deque는 O(1) 시간에 양 끝에서 데이터를 추가/삭제할 수 있다.
from collections import deque

#  deque 객체 생성 (빈 덱)
# deque는 리스트와 비슷하지만, 빠른 삽입과 삭제가 가능하다.
d = deque()

#  데이터 추가 (오른쪽 끝에 추가됨)
# append()는 리스트의 append()와 동일하게 작동하며, O(1) 시간에 수행된다.
d.append(7)  # 덱: [7]
d.append(-11)  # 덱: [7, -11]
d.append(8)  # 덱: [7, -11, 8]

#  메인 실행 코드 (스크립트가 직접 실행될 때만 동작)
if __name__ == "__main__":

    #  덱의 요소를 하나씩 출력 (FIFO 방식)
    # 덱은 기본적으로 큐(Queue)처럼 동작하며, 처음 넣은 값부터 출력된다.
    for data in d:
        print(data)  # 출력: 7, -11, 8 (입력된 순서대로 출력됨)

    #  deque의 추가 기능 테스트
    print("\n🔹 deque 추가 기능 테스트")

    #  양쪽 끝에서 데이터 추가 가능
    d.append(10)  # 오른쪽 끝에 추가 (덱: [7, -11, 8, 10])
    d.appendleft(5)  # 왼쪽 끝에 추가 (덱: [5, 7, -11, 8, 10])
    print("추가 후 deque:", d)

    #  양쪽 끝에서 데이터 삭제 가능
    d.pop()  # 오른쪽 끝에서 제거 (덱: [5, 7, -11, 8])
    d.popleft()  # 왼쪽 끝에서 제거 (덱: [7, -11, 8])
    print("삭제 후 deque:", d)

    #  deque는 회전(rotate) 기능을 제공하여 O(n) 시간에 요소를 이동할 수 있다.
    d.rotate(1)  # 모든 요소를 오른쪽으로 1칸 회전 (덱: [8, 7, -11])
    print("회전 후 deque (오른쪽 1칸):", d)

    d.rotate(-1)  # 모든 요소를 왼쪽으로 1칸 회전 (덱: [7, -11, 8])
    print("회전 후 deque (왼쪽 1칸):", d)

    # deque는 reverse()를 사용하여 O(n) 시간에 리스트를 뒤집을 수 있다.
    d.reverse()  # 덱을 뒤집기 (덱: [8, -11, 7])
    print("뒤집은 deque:", d)

