# Node 클래스 (연결 리스트의 개별 노드)
class Node:
    def __init__(self, data, next=None):
        """
        개별 노드를 정의하는 클래스
        :param data: 노드가 저장할 값
        :param next: 다음 노드를 가리키는 포인터 (기본값: None)
        """
        self.data = data  # 노드가 저장하는 데이터 값
        self.next = next  # 다음 노드를 가리키는 포인터 (기본값 None)


#  Queue 클래스 (연결 리스트 기반 큐 구현)
class Queue:
    def __init__(self):
        """
        연결 리스트를 이용한 큐(Queue) 구현.
        - self.front: 큐의 맨 앞(front) 노드를 가리키는 포인터
        - self.rear: 큐의 맨 뒤(rear) 노드를 가리키는 포인터
        - self._size: 큐의 현재 크기 저장 (초기값: 0)
        """
        self.front = None  #  큐의 맨 앞 (dequeue 연산 시 변경됨)
        self.rear = None   #  큐의 맨 뒤 (enqueue 연산 시 변경됨)
        self._size = 0  #  큐의 크기 저장

    def enqueue(self, data):
        """
        큐의 맨 뒤(rear)에 데이터를 추가하는 함수 (FIFO: First-In, First-Out)
        :param data: 큐에 추가할 값
        """
        self._size = self._size + 1  #  크기 증가
        node = Node(data)  #  새로운 노드 생성

        if self.rear is None:  #  큐가 비어 있는 경우 (첫 노드 추가)
            self.front = node  #  front와 rear가 동일한 노드를 가리킴
            self.rear = node
        else:  # 🔹 기존 rear 다음에 새로운 노드를 연결
            self.rear.next = node  #  현재 rear의 next를 새 노드로 연결
            self.rear = node  #  rear 포인터를 새로운 노드로 변경 (rear가 증가함)

    def dequeue(self):
        """
        큐의 맨 앞(front) 데이터를 제거하고 반환하는 함수.
        :return: 삭제된 front 노드의 데이터
        :raises IndexError: 큐가 비어 있을 경우 예외 발생
        """
        if self.front is None:  #  큐가 비어 있는 경우 예외 처리
            raise IndexError('dequeue from empty queue')

        self._size = self._size - 1  #  크기 감소
        temp = self.front  #  현재 front 노드를 백업 (반환할 데이터 저장)
        self.front = self.front.next  #  front를 다음 노드로 업데이트 (front가 증가함)

        if self.front is None:  #  front가 None이면 rear도 None으로 설정 (큐가 비어 있음)
            self.real = None  #  rear 포인터 초기화 (오타: self.real → self.rear)

        return temp.data  #  삭제된 front 노드의 데이터 반환

    def size(self) -> int:
        """
        현재 큐의 크기 반환.
        :return: 큐에 저장된 노드 개수
        """
        return self._size  #  현재 큐의 크기 반환


#  실행 코드 (스크립트 실행 시 동작)
if __name__ == "__main__":
    q = Queue()  #  큐 객체 생성

    #  데이터 추가 (enqueue)
    q.enqueue(7)  
    q.enqueue(-11)
    q.enqueue(8)

    print(q.size())  #  현재 큐 크기 출력 (3)

    #  데이터 삭제 (dequeue)
    print(q.dequeue())  #  front 제거 후 데이터 출력 (7)

    print(q.size())  #  현재 큐 크기 출력 (2)

    #  enqueue하면 rear가 늘어나고, dequeue하면 front가 늘어남