def is_even(n) -> bool:
    """
    짝수 판정 함수
    :param n: 판정할 정수
    :return: 짝수면 True, 홀수면 False
    """
    return not n & 1
#비트연산을 통해 코드를 줄일수있음

   # if n % 2 == 0:
   #      return True
   #  return False

n = int(input())
print(is_even(n))


a = 10
b = 11
# bit operation (2진수로 바꾼후 and or nor로 연산)
print (a & b) #10
print (a | b) #11
print (a ^ b) #11
