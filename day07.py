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

    # 데이터 추가 (7, -11, 8)
    l.append(7)  # 리스트: 7
    l.append(-11)  # 리스트: 7 -> -11
    l.append(8)  # 리스트: 7 -> -11 -> 8

    # 리스트 출력 (__str__ 메서드 호출)
    print(l)  # 출력 결과: 
    # 7
    # -11
    # 8
    # end