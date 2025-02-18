def check_bracket(expr: str) -> bool:
    """
    괄호가 올바르게 짝을 이루는지 확인하는 함수.
    :param expr: str - 입력된 문자열
    :return: bool - 올바른 괄호 구조이면 True, 아니면 False
    """

    stack = []  #  여는 괄호를 저장할 스택 (후입선출 LIFO 방식)
    table = {')': '(', ']': '[', '}': '{', '>': '<'}  #  닫는 괄호와 여는 괄호의 매칭 정보

    for char in expr:  # 입력된 문자열을 한 문자씩 순회

        if char in table.values():  #  여는 괄호인지 확인 ("([{<")
            stack.append(char)  #  스택에 추가 (여는 괄호 저장)

        elif char in table.keys():  #  닫는 괄호인지 확인 (")]}>"")
            #  스택이 비어 있거나, 스택의 마지막 요소가 현재 닫는 괄호와 매칭되지 않는다면 False 반환
            if not stack or table[char] != stack.pop():
                return False  #  올바르지 않은 괄호 구조

    return len(stack) == 0  #  스택이 비어 있으면 True, 그렇지 않으면 False 반환


#  실행 코드 (스크립트 실행 시 동작)
if __name__ == "__main__":
    expression = input("Input expression : ")  #  사용자 입력 받기
    print(check_bracket(expression))  #  괄호 검사 후 결과 출력