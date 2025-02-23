#수업시간에 설명(큐(데크), 원형링크드리스트)한 방법 외의 방법으로 문제를 해결하고 깃허브에 업로드 하시오.

def josephus(N, K):
    result = []
    index = 0
    people = list(range(1, N + 1))

    while len(people) > 0:
        index = (index + K - 1) % len(people)
        result.append(people.pop(index))

    print(f"<{', '.join(map(str, result))}>")

N, K = map(int, input().split())

if 1 <= K <= N <= 5000:
    josephus(N, K)