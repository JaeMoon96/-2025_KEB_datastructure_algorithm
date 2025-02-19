# 이진 탐색 트리(BST) 삽입, 검색, 삭제 함수를 설계하고 코드로 작성하시오.
# 삭제 함수에는 리프(LEAF) 노드, 자식이 1개인 경우 그리고 자식이 2개인 경우를 고려하시오.

class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None

def insert(root, value):
    if root == None or root.data == None:
        root.data = value
        return root
    if value < root.data:
        if root.left == None:
            root.left = TreeNode()
        root.left = insert(root.left, value)
    else:
        if root.right == None:
            root.right = TreeNode()
        root.right = insert(root.right, value)

    return root

def find_min(node):
    while node.left != None:
        node = node.left
    return node

def delete(root, value2):
    if root == None or root.data == None:
        return root
    if value2 < root.data:
        root.left = delete(root.left, value2)
    elif value2 > root.data:
        root.right = delete(root.right, value2)
    else:
        if root.left == None and root.right == None:
            return None
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        min_right = find_min(root.right)
        root.data = min_right.data.data
        root.right = delete(root.right, min_right.data)

    return root

if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]
    root = None

    node = TreeNode()
    node.data = numbers[0]
    root = node

    for group in numbers[1:]:
        node = TreeNode()
        node.data = group
        current = root
        while True:
            if group < current.data:
                if current.left is None:
                    current.left = node
                    break
                current = current.left  # move
            else:
                if current.right is None:
                    current.right = node
                    break
                current = current.right  # move

    print("BST 구성 완료")


def search(root, value3):
    if root is None or root.data is None:
        return None

    if value3 == root.data:
        return root
    elif value3 < root.data:
        return search(root.left, value3)
    else:
        return search(root.right, value3)

while True:
        menu = input("추가(A), 삭제(D), 검색(S), 종료(Q)를 선택하세요: ")

        if menu == "A":
            value = int(input("추가할 값을 입력하세요: "))
            root = insert(root, value)



        elif menu == "D":
            value = int(input("삭제할 값을 입력하세요: "))
            root = delete(root, value)



        elif menu == "S":
            value = int(input("검색할 값을 입력하세요: "))
            result = search(root, value)
            if result is not None:
                print(f"{value}을(를) 찾았습니다!\n")
            else:
                print(f"{value}이(가) 존재하지 않습니다.\n")

        elif menu == "Q":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 선택해주세요.\n")