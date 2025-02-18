import random  #  난수를 생성하기 위한 random 모듈 불러오기


#  Node 클래스 (연결 리스트의 개별 노드)
class Node:
    def __init__(self, data, next=None):
        """
        개별 노드를 정의하는 클래스
        :param data: 노드가 저장할 값
        :param next: 다음 노드의 주소를 저장하는 포인터 (기본값: None)
        """
        self.data = data  # 노드가 저장하는 데이터 값
        self.next = next  # 다음 노드를 가리키는 포인터 (기본값 None)


#  LinkedList 클래스 (연결 리스트 전체를 관리)
class LinkedList:
    def __init__(self):
        """
        연결 리스트의 초기화
        - self.head: 리스트의 첫 번째 노드를 가리키는 포인터 (초기값: None)
        """
        self.head = None  # 첫 번째 노드 (Head) 저장

    def append(self, data):
        """
        연결 리스트의 끝에 새로운 노드를 추가하는 함수
        :param data: 추가할 데이터 값
        """
        # 리스트가 비어 있다면, 첫 번째 노드로 설정
        if not self.head:
            self.head = Node(data)  # 새로운 노드를 head로 설정
            return  # 함수 종료

        # 리스트가 비어 있지 않다면, 마지막 노드를 찾아 새 노드를 추가
        current = self.head  # 시작점 (Head 노드부터 탐색)
        while current.next:  # 마지막 노드까지 이동 (current.next가 None이 될 때까지)
            current = current.next  # 다음 노드로 이동

        # 마지막 노드(current.next가 None인 상태)에 새 노드 연결
        current.next = Node(data)

    def search(self, target) -> bool:
        """
        특정 값(target)이 리스트에 존재하는지 검색하는 함수
        :param target: 찾고자 하는 값
        :return: 값이 존재하면 True, 없으면 False 반환
        """
        current = self.head  # 첫 번째 노드부터 탐색 시작
        while current:  # 리스트 끝까지 탐색
            if current.data == target:  # 찾는 값과 일치하면 True 반환
                return True
            current = current.next  # 다음 노드로 이동
        return False  # 리스트에 없으면 False 반환

    def remove(self, target):
        """
        연결 리스트에서 특정 값을 가진 노드를 삭제하는 함수
        :param target: 삭제할 값
        """
        # 리스트의 첫 번째 노드(head)가 삭제할 값과 같을 경우
        if self.head and self.head.data == target:
            self.head = self.head.next  # head를 다음 노드로 변경
            print("!")  # 삭제 표시 출력
            return  # 함수 종료

        current = self.head  # 탐색 시작점 (head부터)
        previous = None  # 이전 노드를 저장할 변수

        while current:  # 리스트 끝까지 탐색
            if current.data == target:  # 삭제할 값을 찾은 경우
                previous.next = current.next  # 이전 노드의 next를 현재 노드의 next로 변경 (삭제)
                break  # 삭제 후 루프 종료
            else:  # 삭제할 값을 찾지 못하면 다음 노드로 이동
                previous = current
                current = current.next

    def __str__(self):
        """
        연결 리스트의 모든 노드를 출력하는 함수 (문자열 반환)
        :return: "end" (출력 완료 후 반환할 문자열)
        """
        node = self.head  # 리스트의 첫 번째 노드부터 시작
        while node is not None:  # 노드가 존재하는 동안 반복
            print(node.data)  # 현재 노드의 데이터 출력
            node = node.next  # 다음 노드로 이동
        return "end"  # 모든 노드 출력 후 반환


#  실행 코드 (메인 함수 역할)
if __name__ == "__main__":
    l = LinkedList()  # 연결 리스트 객체 생성

    #  데이터 추가 (7, -11, 8)
    l.append(7)
    l.append(-11)
    l.append(8)
    print("초기 리스트:")
    print(l)  # 리스트 출력

    #  특정 값 삭제 테스트
    print("\n8 삭제 후 리스트:")
    l.remove(8)  # 값 8 삭제
    print(l)  # 삭제 후 리스트 출력

    # 🔹랜덤 숫자 20개를 생성하여 리스트에 추가하는 코드 (현재 주석 처리됨)
    """
    l = LinkedList()
    i = 0
    while i < 20:
        n = random.randint(1, 20)  # 1~20 사이의 랜덤 숫자 생성
        l.append(n)  # 연결 리스트에 추가
        print(n, end=' ')  # 생성된 숫자 출력
        i = i + 1  # 카운터 증가

    print("\n")  # 줄 바꿈

    # 🔹 특정 숫자(10)가 리스트에 존재하는지 검색
    result = l.search(10)  # 값 10이 있는지 탐색
    print("10이 리스트에 존재하는가?", result)  # 검색 결과 출력 (True/False)
    """
