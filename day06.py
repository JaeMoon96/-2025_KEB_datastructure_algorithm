def is_even(n) -> bool:
    """
    짝수 판정 함수
    :param n: 판정할 정수
    :return: 짝수면 True, 홀수면 False
    """
    if n % 2 == 0:
        return True
    return False

a = 10
b = 11
# bit operation (2진수로 바꾼후 and or nor로 연산)
print (a & b) #10
print (a | b) #11
print (a ^ b) #1
n = int(input())
print(is_even)