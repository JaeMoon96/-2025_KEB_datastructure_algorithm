# 이진 탐색 트리(BST) 삽입, 검색, 삭제 함수를 설계하고 코드로 작성하시오.
# 삭제 함수에는 리프(LEAF) 노드, 자식이 1개인 경우 그리고 자식이 2개인 경우를 고려하시오.
class TreeNode:
    def __init__(self):
        self.left = None  # 왼쪽 자식 노드
        self.data = None  # 현재 노드의 값
        self.right = None  # 오른쪽 자식 노드


# 이진 탐색 트리에 값을 삽입하는 함수 (재귀 방식)
def insert(root, value):
    if root == None or root.data == None:  # 루트가 비어 있거나 초기 값이 없을 경우
        root.data = value  # 루트에 값 할당
        return root

    if value < root.data:  # 삽입할 값이 현재 노드보다 작으면 왼쪽으로 이동
        if root.left == None:
            root.left = TreeNode()  # 왼쪽 노드가 없으면 새 노드 생성
        root.left = insert(root.left, value)  # 재귀적으로 삽입 진행

    else:  # 삽입할 값이 현재 노드보다 크면 오른쪽으로 이동
        if root.right == None:
            root.right = TreeNode()  # 오른쪽 노드가 없으면 새 노드 생성
        root.right = insert(root.right, value)  # 재귀적으로 삽입 진행

    return root  # 최종적으로 루트 노드를 반환


# 트리에서 가장 작은 값을 찾는 함수 (왼쪽으로 끝까지 이동)
def find_min(node):
    while node.left != None:
        node = node.left
    return node


# 이진 탐색 트리에서 특정 값을 삭제하는 함수
    if root == None or root.data == None:  # 트리가 비어 있으면 종료
        return root

    if value < root.data:  # 삭제할 값이 현재 노드보다 작으면 왼쪽 서브트리로 이동
        root.left = delete(root.left, value)

    elif value > root.data:  # 삭제할 값이 현재 노드보다 크면 오른쪽 서브트리로 이동
        root.right = delete(root.right, value)

    else:  # 현재 노드가 삭제할 값과 같으면 삭제 수행
        if root.left == None and root.right == None:  # 자식이 없는 경우 (리프 노드)
            return None  # 노드 삭제

        if root.left is None:  # 왼쪽 자식이 없을 경우 오른쪽 자식을 현재 노드로 변경
            return root.right

        if root.right is None:  # 오른쪽 자식이 없을 경우 왼쪽 자식을 현재 노드로 변경
            return root.left

        # 두 개의 자식이 있는 경우 (오른쪽 서브트리에서 최소값 찾기)
        min_right = find_min(root.right)
        root.data = min_right.data.data  # 최소값을 현재 노드 값으로 변경
        root.right = delete(root.right, min_right.data)  # 최소값을 삭제

    return root  # 변경된 루트 반환


# 이진 탐색 트리에서 특정 값을 검색하는 함수
def search(root, value):
    if root is None or root.data is None:  # 트리가 비어 있으면 종료
        return None

    if value == root.data:  # 찾는 값이 현재 노드의 값과 같으면 반환
        return root
    elif value < root.data:  # 찾는 값이 현재 값보다 작으면 왼쪽으로 이동
        return search(root.left, value)
    else:  # 찾는 값이 현재 값보다 크면 오른쪽으로 이동
        return search(root.right, value)


# 프로그램 실행 코드 (BST 생성 및 메뉴 선택)
if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]  # 초기 삽입할 데이터 리스트
    root = None  # 트리 루트 초기화

    # 첫 번째 노드를 루트로 설정
    node = TreeNode()
    node.data = numbers[0]
    root = node

    # 나머지 숫자들을 반복문을 사용하여 삽입 (반복문 방식)
    for group in numbers[1:]:
        node = TreeNode()  # 새로운 노드 생성
        node.data = group  # 노드에 값 저장
        current = root  # 루트에서 시작

        while True:  # 적절한 위치를 찾을 때까지 반복
            if group < current.data:
                if current.left is None:  # 왼쪽 자식이 비어 있으면 삽입
                    current.left = node
                    break
                current = current.left  # 왼쪽으로 이동
            else:
                if current.right is None:  # 오른쪽 자식이 비어 있으면 삽입
                    current.right = node
                    break
                current = current.right  # 오른쪽으로 이동

    print("BST 구성 완료")  # 트리 생성 완료 메시지 출력

# 사용자 메뉴 시스템 (추가, 삭제, 검색, 종료 기능 제공)
while True:
    menu = input("추가(A), 삭제(D), 검색(S), 종료(Q)를 선택하세요: ")

    if menu == "A":  # 값 추가
        value = int(input("추가할 값을 입력하세요: "))
        root = insert(root, value)

    elif menu == "D":  # 값 삭제
        value = int(input("삭제할 값을 입력하세요: "))
        root = delete(root, value)

    elif menu == "S":  # 값 검색
        value = int(input("검색할 값을 입력하세요: "))
        result = search(root, value)
        if result is not None:
            print(f"{value}을(를) 찾았습니다!\n")
        else:
            print(f"{value}이(가) 존재하지 않습니다.\n")

    elif menu == "Q":  # 프로그램 종료
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 입력입니다. 다시 선택해주세요.\n")